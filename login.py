import os
from PySide6.QtWidgets import (
    QWidget, QToolButton, QLabel,
    QHBoxLayout, QListWidget,
    QListWidgetItem, QSizePolicy,
    QLineEdit, QPushButton,
    QMenu, QApplication
)

from api_dialog import API

from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QPropertyAnimation, QEasingCurve
from PySide6.QtWidgets import QGraphicsOpacityEffect, QMessageBox, QGraphicsBlurEffect
from PySide6.QtCore import Signal

from PySide6.QtCore import QTimer
import json

import sqlite3

from PySide6.QtGui import QDesktopServices
from PySide6.QtCore import QUrl, Qt

class Login(QWidget):
    signal = Signal(str)
    reg_signal = Signal()
    def __init__(self, parent=None):
        super().__init__(parent)

        # ===== 1️⃣ 加载 UI =====
        loader = QUiLoader()
        base_dir = os.path.dirname(__file__)
        ui_path = os.path.join(base_dir, "login.ui")

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

        self.reg = self.root.findChild(QPushButton, "reg")
        self.reg.setCursor(Qt.PointingHandCursor)
        self.reg.clicked.connect(self.reg_signal.emit)


        self.que = self.root.findChild(QPushButton, "que")
        self.que.setCursor(Qt.PointingHandCursor)

        self.que.clicked.connect(
            lambda: QDesktopServices.openUrl(QUrl("https://www.baidu.com"))
        )

        self.menu_button = self.root.findChild(QToolButton, "menuButton")

        self.init_menu()

    def init_menu(self):
        self.menu = QMenu()
        self.menu.setWindowFlags(
        Qt.Popup | Qt.FramelessWindowHint | Qt.NoDropShadowWindowHint
        )
        about_action = self.menu.addAction("关于")
        self.menu.addSeparator()
        exit_action = self.menu.addAction("退出")
        exit_action.triggered.connect(QApplication.quit)

        self.menu_button.setPopupMode(QToolButton.InstantPopup)
        self.menu_button.setMenu(self.menu)

        about_action.triggered.connect(self.show_about)
        self.menu.setStyleSheet("""
        QMenu {
                background: white;
                border-radius: 12px;
                padding: 6px;
        }

        QMenu::item {
            padding: 8px 24px;
            border-radius: 8px;
            color: #4B5563;
        }

        QMenu::item:selected {
            background-color: #F3E8FF;
            color: #7C3AED;
        }

        QMenu::separator {
            height: 1px;
            background: #F3E8FF;
            margin: 6px 12px;
        }
         """)

    def show_about(self):
        QMessageBox.about(
                self,
                "关于",
                "AzurChat v1.0\n\n基于 PySide6 开发"
            )

    def handle_login(self):
        username = self.user.text().strip()
        password = self.password.text().strip()

        if not username or not password:
            Toast("用户名或密码不能为空", self)
            return

        if len(username) < 8 or len(password) < 8:
            Toast("用户名或密码长度不能少于8位", self)
            return

        result = self.check_user(username, password)

        if result == "not_exist":
            Toast("用户不存在", self)

        elif result == "success":
            api_ok = self.check_api(username)

            if api_ok:
                Toast("登录成功", self)
                self.signal.emit()
            else:
                self.open_api_dialog(username)

        elif result == "wrong_password":
            Toast("密码错误", self)

        self.user.clear()
        self.password.clear()

    def open_api_dialog(self, username):

        # 添加模糊
        self.blur = QGraphicsBlurEffect()
        self.blur.setBlurRadius(15)
        self.root.setGraphicsEffect(self.blur)

        # 创建 API 页面
        self.api = API(parent=self, username=username)

        # 覆盖 Login
        self.api.setGeometry(0, 0, self.width(), self.height())

        # 关闭信号
        self.api.signal.connect(self.close_api_dialog)

        self.api.show()

    def close_api_dialog(self):

        # 移除模糊
        self.root.setGraphicsEffect(None)

        self.api.close()
    def check_api(self, username):

        conn = sqlite3.connect("chat.db")
        cursor = conn.cursor()

        cursor.execute(
        "SELECT api, url FROM users WHERE username=?",
        (username,)
        )

        result = cursor.fetchone()
        conn.close()

        # 没有 API
        if result is None:
            return False

        api = result[0]
        url = result[1]

        if not api or not url:
            return False

        # 检查 API 是否可用
        return True

    def check_user(self, username, password):
        conn = sqlite3.connect("chat.db")
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT,
            api TEXT,
            url TEXT
        )
        """)

        cursor.execute(
                "SELECT password FROM users WHERE username=?",
                (username,)
            )
        result = cursor.fetchone()

        # 用户不存在
        if result is None:
            conn.close()
            return "not_exist"

        # 用户存在 → 校验密码
        stored_password = result[0]
        if stored_password == password:
            conn.close()
            return "success"
        else:
            conn.close()
            return "wrong_password"

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
