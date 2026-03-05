import os
from PySide6.QtWidgets import (
    QWidget, QToolButton, QLabel,
    QHBoxLayout, QListWidget,
    QListWidgetItem, QSizePolicy,
    QLineEdit, QPushButton,
    QMenu
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QSize, Qt, QPropertyAnimation, QEasingCurve, QPoint
from PySide6.QtWidgets import QGraphicsOpacityEffect
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Signal

import threading
from PySide6.QtCore import QTimer
from use_api import Chat

from datetime import datetime

class ChatPage(QWidget):
    ai_reply_signal = Signal(str)
    def __init__(self, parent=None):
        super().__init__(parent)

        # ===== 1️⃣ 加载 UI =====
        loader = QUiLoader()
        base_dir = os.path.dirname(__file__)
        ui_path = os.path.join(base_dir, "form_chat.ui")

        file = QFile(ui_path)
        file.open(QFile.ReadOnly)
        self.root = loader.load(file)
        file.close()

        # 把 UI 根挂到当前页面
        self.root.setParent(self)

        # ===== 2️⃣ 获取 UI 控件 =====
        self.back_button = self.root.findChild(QToolButton, "mainButton")
        self.title_label = self.root.findChild(QLabel, "label")
        self.list = self.root.findChild(QListWidget, "listWidget")

        # ===== 3️⃣ 设置返回按钮图标 =====
        if self.back_button:
            icon_path = os.path.join(base_dir, "go.png")
            self.back_button.setIcon(QIcon(icon_path))
            self.back_button.setIconSize(QSize(24, 24))
            self.back_button.setFixedSize(30, 30)
            self.back_button.setToolButtonStyle(Qt.ToolButtonIconOnly)

        tool_button = self.root.findChild(QToolButton, "toolButton")

        if tool_button:
            tool_button.setPopupMode(QToolButton.InstantPopup)


        # ===== 4️⃣ 配置 listWidget =====
        if self.list:
            self.list.setUniformItemSizes(False)
            self.list.setVerticalScrollMode(QListWidget.ScrollPerPixel)
            self.list.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

            self.list.setStyleSheet("""
                QListWidget {
                    border: none;
                    outline: none;
                    background-color: #EEF2F6;
                    padding: 10px;
                }
                QListWidget::item:selected {
                    background: transparent;
                }
            """)
        self.original_title = ""
        self.input = self.root.findChild(QLineEdit, "lineEdit")
        self.send_btn = self.root.findChild(QPushButton, "pushButton")
        if self.send_btn:
            self.send_btn.clicked.connect(self.send_message)
        self.last_message_time = None
        self.chat_engine = Chat()

        self.ai_reply_signal.connect(self.show_reply)

    def send_message(self):
        text = self.input.text().strip()
        if not text:
            return

    # 1️⃣ 清空输入框
        self.input.clear()

    # 2️⃣ 显示右侧用户消息
        self.add_right_message(text)

    # 3️⃣ 添加一个“思考中...”占位
        QTimer.singleShot(800, self.show_typing_in_title)

    # 4️⃣ 开线程调用AI（防止UI卡死）
        thread = threading.Thread(
        target=self.ask_ai,
        args=(text,),
        daemon=True
        )
        thread.start()

    def ask_ai(self, text):
        print("线程启动")

        try:
            reply = self.chat_engine.chat(text)
        except Exception as e:
            reply = f"请求失败：{str(e)}"

        self.ai_reply_signal.emit(reply)

    def show_reply(self, reply):
        QTimer.singleShot(1500, lambda: self._final_reply(reply))

    def _final_reply(self, reply):
            # 删除最后一个“正在输入”
        if self.title_label:
            self.title_label.setText(self.original_title)

        self.add_left_message(reply)

    def add_left_message(self, text: str):
        self.check_and_add_time()
        if not self.list:
            return

        item = QListWidgetItem()

        bubble_widget = QWidget()
        layout = QHBoxLayout(bubble_widget)
        layout.setContentsMargins(10, 5, 50, 5)
        layout.setSpacing(8)

        avatar = QLabel()
        pixmap = QPixmap(":/new/prefix1/head.png").scaled(36, 36)
        avatar.setPixmap(pixmap)
        avatar.setFixedSize(36, 36)

        bubble = QLabel(text)
        bubble.setWordWrap(True)
        bubble.setMaximumWidth(300)

        bubble.setStyleSheet("""
            QLabel {
                background-color: white;
                border-radius: 12px;
                padding: 8px 20px;
                font-size: 14px;
            }
        """)

        layout.addWidget(avatar)
        layout.addWidget(bubble)
        layout.addStretch()

        self.list.addItem(item)
        self.list.setItemWidget(item, bubble_widget)

        bubble_widget.adjustSize()
        item.setSizeHint(bubble_widget.sizeHint())

        self.list.scrollToBottom()

        opacity = QGraphicsOpacityEffect()
        bubble_widget.setGraphicsEffect(opacity)
        opacity.setOpacity(0)

        fade_anim = QPropertyAnimation(opacity, b"opacity")
        fade_anim.setDuration(300)
        fade_anim.setStartValue(0)
        fade_anim.setEndValue(1)
        fade_anim.setEasingCurve(QEasingCurve.OutCubic)

        # 2️⃣ 位置动画
        pos_anim = QPropertyAnimation(bubble_widget, b"pos")
        pos_anim.setDuration(300)
        start_pos = bubble_widget.pos() - QPoint(30, 0)
        end_pos = bubble_widget.pos()

        bubble_widget.move(start_pos)

        pos_anim.setStartValue(start_pos)
        pos_anim.setEndValue(end_pos)
        pos_anim.setEasingCurve(QEasingCurve.OutCubic)

        # 防止被垃圾回收
        self._fade_anim = fade_anim
        self._pos_anim = pos_anim

        fade_anim.start()
        pos_anim.start()
    # =============================
    # 右侧气泡
    # =============================
    def add_right_message(self, text: str):
        self.check_and_add_time()
        if not self.list:
            return

        item = QListWidgetItem()

        bubble_widget = QWidget()
        layout = QHBoxLayout(bubble_widget)
        layout.setContentsMargins(50, 5, 10, 5)

        bubble = QLabel(text)
        bubble.setWordWrap(True)
        bubble.setMaximumWidth(380)

        bubble.setStyleSheet("""
            QLabel {
                background-color: #95EC69;
                border-radius: 12px;
                padding: 8px 20px;
                font-size: 14px;
            }
        """)

        layout.addStretch()
        layout.addWidget(bubble)

        self.list.addItem(item)
        self.list.setItemWidget(item, bubble_widget)

        bubble_widget.adjustSize()
        item.setSizeHint(bubble_widget.sizeHint())

        self.list.scrollToBottom()

    # =============================
    # 绑定按钮
    # =============================
    def bind_back(self, callback):
        if self.back_button:
            self.back_button.clicked.connect(callback)
    def set_title(self, title: str):
        if self.title_label:
            self.original_title = title
            self.title_label.setText(title)
    def add_time_label(self, time_text: str):
        item = QListWidgetItem()

        label = QLabel(time_text)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("""
                    QLabel {
                        color: gray;
                        font-size: 12px;
                        padding: 4px;
                    }
                """)

        self.list.addItem(item)
        self.list.setItemWidget(item, label)
        item.setSizeHint(label.sizeHint())

    def check_and_add_time(self):
        now = datetime.now()

        if self.last_message_time is None:
                # 第一条消息
            self.add_time_label(now.strftime("%H:%M"))
        else:
            delta = (now - self.last_message_time).total_seconds()
            if delta >= 60:
                self.add_time_label(now.strftime("%H:%M"))

        self.last_message_time = now

    def show_typing_in_title(self):
        if self.title_label:
            self.title_label.setText("对方正在输入...")

    def bind_open_chara(self, callback):
        tool_button = self.root.findChild(QToolButton, "menu")
        if tool_button:
            tool_button.clicked.connect(callback)
