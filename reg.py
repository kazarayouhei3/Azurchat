import os
from PySide6.QtWidgets import (
    QWidget, QToolButton, QLabel,
    QLineEdit, QPushButton,
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QSize, Qt

from PySide6.QtGui import QIcon
from PySide6.QtCore import Signal

import threading
from PySide6.QtCore import QTimer
import rc_pic
from db import register_user
from qap import Toast


class Reg(QWidget):
    signal = Signal()
    b_signal = Signal()
    def __init__(self, parent=None):
        super().__init__(parent)

        # ===== 1️⃣ 加载 UI =====
        loader = QUiLoader()
        base_dir = os.path.dirname(__file__)
        ui_path = os.path.join(base_dir, "reg.ui")

        file = QFile(ui_path)
        file.open(QFile.ReadOnly)
        self.root = loader.load(file)
        file.close()

        # 把 UI 根挂到当前页面
        self.root.setParent(self)

        self.user = self.root.findChild(QLineEdit, "user")
        self.password = self.root.findChild(QLineEdit, "password")

        self.user.setPlaceholderText("请输入用户名")
        self.password.setPlaceholderText("请输入密码")

        self.login_button = self.root.findChild(QPushButton, "loginButton")

        self.login_button.clicked.connect(self.handle_login)


        self.back_button = self.root.findChild(QToolButton, "menuButton")

        self.back_button.clicked.connect(self.b_signal.emit)

        icon_path = os.path.join(base_dir, "go.png")
        self.back_button.setIcon(QIcon(icon_path))
        self.back_button.setIconSize(QSize(24, 24))
        self.back_button.setFixedSize(30, 30)
        self.back_button.setToolButtonStyle(Qt.ToolButtonIconOnly)

    def handle_login(self):
        username = self.user.text().strip()
        password = self.password.text().strip()

        if not username or not password:
            Toast("用户名或密码不能为空", self)
            return

        if len(username) < 8 or len(password) < 8:
            Toast("用户名或密码长度不能少于8位", self)
            return

        result = register_user(username, password)

        if result == "created":
            Toast("注册成功", self)
            QTimer.singleShot(1000, self.signal.emit)

        elif result == "exist":
            Toast("用户名已存在", self)

        self.user.clear()
        self.password.clear()


