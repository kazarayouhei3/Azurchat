from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout
from PySide6.QtGui import QPainter, QPainterPath, QPixmap
from PySide6.QtCore import Qt, QRectF
import rc_head
from qap import get_round_pixmap


class ChatItem(QWidget):
    def __init__(self, fid, name, message, time_text, avatar_path, parent=None):
        super().__init__(parent)

        self.fid = fid
        self.name = name
        self.message = message
        self.time_text = time_text
        self.avatar = avatar_path
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
        self.avatar_label = QLabel()
        self.avatar_label.setFixedSize(44, 44)
        self.avatar_label.setStyleSheet("background:#ddd; border-radius:22px;")
        pix = get_round_pixmap(self.avatar, 44)

        if not pix.isNull():
            self.avatar_label.setPixmap(pix)

        main_layout.addWidget(self.avatar_label)

        # 中间文字区域
        text_layout = QVBoxLayout()
        text_layout.setSpacing(2)

        self.name_label = QLabel(self.name)
        self.name_label.setStyleSheet("font-size:14px; font-weight:600;")

        self.msg_label = QLabel(self.message)
        self.msg_label.setStyleSheet("font-size:12px; color:#777;")

        text_layout.addWidget(self.name_label)
        text_layout.addWidget(self.msg_label)

        main_layout.addLayout(text_layout, 1)

        # 时间
        self.time_label = QLabel(self.time_text)
        self.time_label.setStyleSheet("font-size:11px; color:#999;")
        self.time_label.setAlignment(Qt.AlignRight | Qt.AlignTop)

        main_layout.addWidget(self.time_label)
