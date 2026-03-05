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
import sqlite3

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

        result = self.register_user(username, password)

        if result == "created":
            Toast("注册成功", self)
            QTimer.singleShot(1000, self.signal.emit)

        elif result == "exist":
            Toast("用户名已存在", self)

        self.user.clear()
        self.password.clear()

    def register_user(self, username, password):
        conn = sqlite3.connect("chat.db")
        cursor = conn.cursor()

        cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE,
                    password TEXT
                )
            """)

        # 先查是否存在
        cursor.execute(
                "SELECT id FROM users WHERE username=?",
                (username,)
            )
        result = cursor.fetchone()

        if result is not None:
            conn.close()
            return "exist"

            # 不存在 → 创建
        cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, password)
            )
        conn.commit()
        conn.close()

        return "created"



class Toast(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)

        self.setStyleSheet("""
            QLabel {
                background-color: rgba(0, 0, 0, 180);
                color: white;
                padding: 10px 20px;
                border-radius: 8px;
                font-size: 14px;
            }
        """)

        self.adjustSize()
        self.move(
            (parent.width() - self.width()) // 2,
            parent.height() // 3
        )

        self.setGraphicsEffect(QGraphicsOpacityEffect(self))
        self.opacity_effect = self.graphicsEffect()

        self.animation = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.animation.setDuration(300)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.setEasingCurve(QEasingCurve.OutCubic)

        self.show()
        self.animation.start()

        # 1.5 秒后开始淡出
        QTimer.singleShot(1500, self.fade_out)

    def fade_out(self):
        self.animation = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.animation.setDuration(500)
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.setEasingCurve(QEasingCurve.OutCubic)
        self.animation.finished.connect(self.close)
        self.animation.start()
