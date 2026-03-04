from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap


class ChatItem(QWidget):
    def __init__(self, name, message, time_text, avatar_path="", parent=None):
        super().__init__(parent)

        # ===== 外层：QListWidget 会管理 ChatItem 的位置，但不会管 content 在里面怎么动 =====
        outer_layout = QHBoxLayout(self)
        outer_layout.setContentsMargins(0, 0, 0, 0)
        outer_layout.setSpacing(0)

        # ===== 内层：真正的内容容器（动画目标）=====
        self.content = QWidget(self)
        outer_layout.addWidget(self.content)

        main_layout = QHBoxLayout(self.content)
        main_layout.setContentsMargins(12, 8, 12, 8)
        main_layout.setSpacing(10)

        # 头像
        self.avatar = QLabel()
        self.avatar.setFixedSize(44, 44)
        self.avatar.setStyleSheet("background:#ddd; border-radius:22px;")
        if avatar_path:
            self.avatar.setPixmap(QPixmap(avatar_path))
            self.avatar.setScaledContents(True)

        main_layout.addWidget(self.avatar)

        # 中间文字区域
        text_layout = QVBoxLayout()
        text_layout.setSpacing(2)

        self.name_label = QLabel(name)
        self.name_label.setStyleSheet("font-size:14px; font-weight:600;")

        self.msg_label = QLabel(message)
        self.msg_label.setStyleSheet("font-size:12px; color:#777;")

        text_layout.addWidget(self.name_label)
        text_layout.addWidget(self.msg_label)

        main_layout.addLayout(text_layout, 1)

        # 时间
        self.time_label = QLabel(time_text)
        self.time_label.setStyleSheet("font-size:11px; color:#999;")
        self.time_label.setAlignment(Qt.AlignRight | Qt.AlignTop)

        main_layout.addWidget(self.time_label)
