import os
from PySide6.QtWidgets import (
    QWidget, QToolButton, QLabel,
    QHBoxLayout, QListWidget,
    QListWidgetItem, QLineEdit, QPushButton
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QSize, Qt, Signal, QTimer
from PySide6.QtGui import QIcon

import threading
from datetime import datetime
from use_api import Chat


class ChatPage(QWidget):
    ai_reply_signal = Signal(object)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.role = None
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
    # ⭐ 切换角色
    # =============================
    def set_role(self, role):
        self.role = role

        # 👉 复用Chat实例（保证上下文）
        if role not in self.chat_engines:
            self.chat_engines[role] = Chat(role)

        self.chat_engine = self.chat_engines[role]

        self.load_chat(role)
        self.last_message_time = None

    # =============================
    # 发送消息
    # =============================
    def send_message(self):
        if not self.chat_engine:
            return

        text = self.input.text().strip()
        if not text:
            return

        self.input.clear()

        self.add_right_message(text)

        QTimer.singleShot(800, self.show_typing_in_title)

        current_role = self.role

        thread = threading.Thread(
            target=self.ask_ai,
            args=(text, current_role),
            daemon=True
        )
        thread.start()

    # =============================
    # AI调用
    # =============================
    def ask_ai(self, text, role):
        try:
            reply = self.chat_engines[role].chat(text)
        except Exception as e:
            reply = f"请求失败：{str(e)}"

        self.ai_reply_signal.emit((role, reply))

    def show_reply(self, data):
        role, reply = data

        if role != self.role:
            return

        QTimer.singleShot(1500, lambda: self._final_reply(reply))

    def _final_reply(self, reply):
        if self.title_label:
            self.title_label.setText(self.original_title)

        self.add_left_message(reply)

    # =============================
    # 加载聊天记录
    # =============================
    def load_chat(self, role):
        self.is_loading = True
        self.list.clear()

        history = self.chat_history.get(role, [])

        for msg_type, text in history:
            if msg_type == "left":
                self.add_left_message(text)
            elif msg_type == "right":
                self.add_right_message(text)
            elif msg_type == "time":
                self.add_time_label(text)

        self.is_loading = False

    # =============================
    # 左气泡（AI）
    # =============================
    def add_left_message(self, text):
        self.check_and_add_time()

        item = QListWidgetItem()

        bubble = QLabel(text)
        bubble.setWordWrap(True)
        bubble.setMaximumWidth(300)
        bubble.setStyleSheet("background:white; padding:8px; border-radius:10px;")

        layout = QHBoxLayout()
        layout.addWidget(bubble)
        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)

        self.list.addItem(item)
        self.list.setItemWidget(item, widget)
        item.setSizeHint(widget.sizeHint())

        self.list.scrollToBottom()

        if not self.is_loading:
            self.chat_history.setdefault(self.role, []).append(("left", text))

    # =============================
    # 右气泡（用户）
    # =============================
    def add_right_message(self, text):
        self.check_and_add_time()

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
            self.chat_history.setdefault(self.role, []).append(("right", text))

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
            self.chat_history.setdefault(self.role, []).append(("time", text))

    def check_and_add_time(self):
        now = datetime.now()

        if not self.last_message_time:
            self.add_time_label(now.strftime("%H:%M"))
        else:
            if (now - self.last_message_time).total_seconds() >= 60:
                self.add_time_label(now.strftime("%H:%M"))

        self.last_message_time = now

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