import os

from PySide6.QtWidgets import (
    QWidget, QPushButton, QToolButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Qt, QRectF, Signal

from qap import get_round_pixmap


class Friend(QWidget):
    signal = Signal()      # 左上角返回
    a_signal = Signal()    # 确认
    b_signal = Signal()    # 取消

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

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(self.root)

        self.quit_button = self.root.findChild(QToolButton, "quit_button")
        self.enter_button = self.root.findChild(QPushButton, "enter")
        self.quit = self.root.findChild(QPushButton, "quit")
        self.name_edit = self.root.findChild(QLineEdit, "name")
        self.line = self.root.findChild(QLineEdit, "line")
        self.quit_button.clicked.connect(self.signal.emit)
        self.enter_button.clicked.connect(self.a_signal.emit)
        self.quit.clicked.connect(self.b_signal.emit)

        self.container = self.root.findChild(QWidget, "friend_a")

        if self.container.layout():
            self.layout = self.container.layout()
        else:
            self.layout = QVBoxLayout(self.container)
            self.layout.setContentsMargins(0, 0, 0, 0)
            self.layout.setSpacing(5)

        self.info_widget = QWidget()
        info_layout = QHBoxLayout(self.info_widget)
        info_layout.setContentsMargins(20, 20, 20, 20)
        info_layout.setSpacing(10)

        self.avatar_label = QLabel()
        self.avatar_label.setFixedSize(60, 60)
        self.avatar_label.setStyleSheet("border-radius:30px; background:#ddd;")

        self.name_label = QLabel()
        self.name_label.setStyleSheet("font-size:16px; font-weight:bold;")

        info_layout.addWidget(self.avatar_label)
        info_layout.addWidget(self.name_label)
        info_layout.addStretch()

        self.layout.addWidget(self.info_widget)


    def set_user_info(self, name, avatar):
        self.name_label.setText(name)

        pix = get_round_pixmap(avatar, 60)
        if not pix.isNull():
            self.avatar_label.setPixmap(pix)
        else:
            self.avatar_label.clear()


        self.name_edit.clear()
        self.name_edit.setPlaceholderText(name)

    def get_input_name(self):
        return self.name_edit.text().strip()

    def get_verify_msg(self):

        return self.line.text().strip()

    def reset(self):
        if self.name_edit:
            self.name_edit.clear()

        if self.line:
            self.line.clear()