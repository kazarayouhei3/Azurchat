import os
from PySide6.QtWidgets import (
    QWidget, QToolButton, QLabel,
    QHBoxLayout, QListWidget,
    QListWidgetItem, QLineEdit, QPushButton
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QSize, Qt, Signal, QTimer
from PySide6.QtGui import QIcon, QPixmap, QPainter, QPainterPath

import threading
from datetime import datetime

from db import get_messages_by_fid, insert_message, update_conversation_last, get_conv_id
from qap import get_round_pixmap
from use_api import Chat


class ChatPage(QWidget):
    ai_reply_signal = Signal(object)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.chat_history = {}
        self.chat_engines = {}
        self.is_loading = False

        # ===== UI加载 =====
        loader = QUiLoader()
        base_dir = os.path.dirname(__file__)
        ui_path = os.path.join(base_dir, "form_chat.ui")

        file = QFile(ui_path)
        file.open(QFile.ReadOnly)
        self.root = loader.load(file)
        file.close()
        self.root.setParent(self)

        # ===== 控件 =====
        self.back_button = self.root.findChild(QToolButton, "mainButton")
        self.title_label = self.root.findChild(QLabel, "chara")
        self.list = self.root.findChild(QListWidget, "listWidget")

        if self.back_button:
            icon_path = os.path.join(base_dir, "go.png")
            self.back_button.setIcon(QIcon(icon_path))
            self.back_button.setIconSize(QSize(24, 24))
            self.back_button.setFixedSize(30, 30)

        if self.list:
            self.list.setStyleSheet("""
                QListWidget {
                    border: none;
                    background-color: #EEF2F6;
                    padding: 10px;
                }

                QScrollBar:vertical {
                    background: transparent;
                    width: 8px;
                    margin: 4px 2px 4px 0px;
                }

                QScrollBar::handle:vertical {
                    background: rgba(0, 0, 0, 0.2);
                    border-radius: 4px;
                    min-height: 30px;
                }

                QScrollBar::handle:vertical:hover {
                    background: rgba(0, 0, 0, 0.4);
                }

                QScrollBar::add-line:vertical,
                QScrollBar::sub-line:vertical {
                    height: 0px;
                }

                QScrollBar::add-page:vertical,
                QScrollBar::sub-page:vertical {
                    background: transparent;
                }
            """)

        self.original_title = ""
        self.input = self.root.findChild(QLineEdit, "lineEdit")
        self.send_btn = self.root.findChild(QPushButton, "pushButton")

        if self.send_btn:
            self.send_btn.clicked.connect(self.send_message)

        self.last_message_time = None
        self.chat_engine = None

        self.ai_reply_signal.connect(self.show_reply)

    # =============================
    # 发送消息
    # =============================
    def send_message(self):
        if not self.chat_engine:
            return None

        if self.is_loading:  # ⭐⭐⭐关键防护⭐⭐⭐
            return

        text = self.input.text().strip()
        if not text:
            return

        self.input.clear()

        conv_id = get_conv_id(self.current_user, self.current_fid)
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        insert_message(conv_id, "user", text)

        update_conversation_last(
            username=self.current_user,
            friend_id=self.current_fid,
            last_message=text
        )

        self.add_right_message(text, now_str)

        self.show_typing_in_title()

        engine = self.chat_engine
        current_fid = self.current_fid

        thread = threading.Thread(
            target=self.ask_ai,
            args=(text, current_fid, engine),
            daemon=True
        )
        thread.start()
    # =============================
    # AI调用
    # =============================
    def ask_ai(self, text, fid, engine):
        try:
            reply = engine.chat(text)
        except Exception as e:
            reply = f"请求失败：{str(e)}"

        self.ai_reply_signal.emit((fid, reply))

    def show_reply(self, data):
        fid, reply = data

        # ⭐⭐⭐关键3：不再延迟⭐⭐⭐
        self._final_reply(reply)

    def _final_reply(self, reply):
        if self.title_label:
            self.title_label.setText(self.original_title)

        conv_id = get_conv_id(self.current_user, self.current_fid)
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        insert_message(conv_id, "assistant", reply)

        update_conversation_last(
            username=self.current_user,
            friend_id=self.current_fid,
            last_message=reply
        )

        self.add_left_message(reply, now_str)

    def set_chat(self, username, fid, name, prompt, avatar):
        # ⭐ 当前用户 / 会话
        self.current_user = username
        self.current_name = name
        self.current_fid = fid

        # ⭐ 头像（你用QPixmap就保留）
        self.current_avatar = QPixmap(avatar)

        # ⭐ 设置标题
        self.set_title(name)

        # ⭐ 创建或复用聊天引擎
        if fid not in self.chat_engines:
            self.chat_engines[fid] = Chat(prompt)

        self.chat_engine = self.chat_engines[fid]

        # ⭐ 加载历史消息
        self.load_chat(fid)

        # ⭐ 重置时间（避免时间错乱）
        self.last_message_time = None


    # =============================
    # 加载聊天记录
    # =============================
    def load_chat(self, fid):
        self.is_loading = True
        self.list.clear()

        # ⭐拿到 conv_id（关键！！）
        conv_id = get_conv_id(self.current_user, self.current_fid)

        if not conv_id:
            self.is_loading = False
            return

        messages = get_messages_by_fid(conv_id)

        for sender, text, time_str in messages:
            if sender == "user":
                self.add_right_message(text, time_str)
            else:
                self.add_left_message(text, time_str)

        self.is_loading = False

    # =============================
    # 左气泡（AI）
    # =============================
    def add_left_message(self, text, time_str=None):
        self.check_and_add_time(time_str)

        item = QListWidgetItem()

        bubble = QLabel(text)
        bubble.setWordWrap(True)
        bubble.setMaximumWidth(300)
        bubble.setStyleSheet("background:white; padding:8px; border-radius:10px;")

        layout = QHBoxLayout()

        # ⭐ 头像
        avatar_label = QLabel()
        avatar_label.setFixedSize(36, 36)

        pix = get_round_pixmap(self.current_avatar, 36)

        if not pix.isNull():
            avatar_label.setPixmap(pix)

        layout.addWidget(avatar_label)
        layout.addWidget(bubble)
        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)

        self.list.addItem(item)
        self.list.setItemWidget(item, widget)
        item.setSizeHint(widget.sizeHint())

        self.list.scrollToBottom()

        if not self.is_loading:
            self.chat_history.setdefault(self.current_fid, []).append(("left", text))

    # =============================
    # 右气泡（用户）
    # =============================
    def add_right_message(self, text, time_str=None):
        self.check_and_add_time(time_str)

        item = QListWidgetItem()

        bubble = QLabel(text)
        bubble.setWordWrap(True)
        bubble.setMaximumWidth(380)
        bubble.setStyleSheet("background:#95EC69; padding:8px; border-radius:10px;")

        layout = QHBoxLayout()
        layout.addStretch()
        layout.addWidget(bubble)

        widget = QWidget()
        widget.setLayout(layout)

        self.list.addItem(item)
        self.list.setItemWidget(item, widget)
        item.setSizeHint(widget.sizeHint())

        self.list.scrollToBottom()

        if not self.is_loading:
            self.chat_history.setdefault(self.current_fid, []).append(("right", text))

    # =============================
    # 时间
    # =============================
    def add_time_label(self, text):
        item = QListWidgetItem()
        label = QLabel(text)
        label.setAlignment(Qt.AlignCenter)

        self.list.addItem(item)
        self.list.setItemWidget(item, label)
        item.setSizeHint(label.sizeHint())

        if not self.is_loading:
            self.chat_history.setdefault(self.current_fid, []).append(("time", text))

    def check_and_add_time(self, time_str=None):
        if time_str:
            try:
                msg_time = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                msg_time = datetime.now()
        else:
            msg_time = datetime.now()

        if not self.last_message_time:
            self.add_time_label(msg_time.strftime("%H:%M"))
        else:
            if (msg_time - self.last_message_time).total_seconds() >= 60:
                self.add_time_label(msg_time.strftime("%H:%M"))

        self.last_message_time = msg_time
    # =============================
    # 其他
    # =============================
    def set_title(self, title):
        self.original_title = title
        if self.title_label:
            self.title_label.setText(title)

    def show_typing_in_title(self):
        if self.title_label:
            self.title_label.setText("对方正在输入...")

    def bind_back(self, callback):
        if self.back_button:
            self.back_button.clicked.connect(callback)

    def bind_open_chara(self, callback):
        tool_button = self.root.findChild(QToolButton, "menu")
        if tool_button:
            tool_button.clicked.connect(callback)