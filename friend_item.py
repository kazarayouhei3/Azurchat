from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout
from PySide6.QtGui import QPixmap

class FriendItem(QWidget):
    def __init__(self, name):
        super().__init__()

        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 5, 10, 5)

        avatar = QLabel()
        avatar.setFixedSize(30, 30)

        # 先用默认图（别纠结路径）
        avatar = QLabel()
        avatar.setFixedSize(30, 30)

        # ⭐ 用样式代替图片
        avatar.setStyleSheet("""
            background-color: #409EFF;
            border-radius: 15px;
        """)

        name_label = QLabel(name)

        layout.addWidget(avatar)
        layout.addWidget(name_label)
        layout.addStretch()