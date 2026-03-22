import os

from PySide6.QtGui import QPixmap, QPainterPath, QPainter
from PySide6.QtWidgets import (
    QWidget, QPushButton, QToolButton, QVBoxLayout, QHBoxLayout, QLabel
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Qt, QRectF
from PySide6.QtCore import Signal

class Friend(QWidget):
    signal = Signal()
    a_signal = Signal()
    b_signal = Signal()
    def __init__(self, parent=None):
        super().__init__(parent)

        loader = QUiLoader()
        base_dir = os.path.dirname(__file__)
        ui_path = os.path.join(base_dir, "friend.ui")

        file = QFile(ui_path)
        file.open(QFile.ReadOnly)
        self.root = loader.load(file)
        file.close()
        self.root.setParent(self)
        self.quit_button = self.root.findChild(QToolButton, "quit_button")
        self.quit_button.clicked.connect(self.signal.emit)
        self.enter_button = self.root.findChild(QPushButton, "enter")
        self.enter_button.clicked.connect(self.a_signal.emit)
        self.quit = self.root.findChild(QPushButton, "quit")
        self.quit.clicked.connect(self.b_signal.emit)

        self.container = self.root.findChild(QWidget, "friend_a")

        # 如果 UI 里没 layout，就手动加
        self.layout = QVBoxLayout(self.container)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(5)

        # ===== 信息行（头像 + 名字）=====
        self.info_widget = QWidget()
        info_layout = QHBoxLayout(self.info_widget)
        info_layout.setContentsMargins(20, 20, 20, 20)
        info_layout.setSpacing(10)

        # ===== 头像 =====
        self.avatar_label = QLabel()
        self.avatar_label.setFixedSize(60, 60)
        self.avatar_label.setStyleSheet("border-radius:30px; background:#ddd;")

        # ===== 名字 =====
        self.name_label = QLabel()
        self.name_label.setStyleSheet("font-size:16px; font-weight:bold;")

        info_layout.addWidget(self.avatar_label)
        info_layout.addWidget(self.name_label)
        info_layout.addStretch()

        # ⭐ 加到 friend_a 里
        self.layout.addWidget(self.info_widget)

    def get_round_pixmap(self, path, size=60):
        src = QPixmap(path)

        if src.isNull():
            return QPixmap()

        # 等比例裁剪填充
        src = src.scaled(
            size, size,
            Qt.KeepAspectRatioByExpanding,
            Qt.SmoothTransformation
        )

        result = QPixmap(size, size)
        result.fill(Qt.transparent)

        painter = QPainter(result)
        painter.setRenderHint(QPainter.Antialiasing)

        path_circle = QPainterPath()
        path_circle.addEllipse(QRectF(0, 0, size, size))
        painter.setClipPath(path_circle)

        painter.drawPixmap(0, 0, src)
        painter.end()

        return result

    def set_user_info(self, name, avatar):
        self.name_label.setText(name)

        pix = self.get_round_pixmap(avatar, 60)

        if not pix.isNull():
            self.avatar_label.setPixmap(pix)
