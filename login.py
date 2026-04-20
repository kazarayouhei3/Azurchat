import os

from PySide6.QtWidgets import (
    QWidget, QToolButton,
    QLineEdit, QPushButton,
    QGraphicsBlurEffect
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QPoint, Signal, Qt, QUrl
from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QDesktopServices

from custom import CustomMenu
from db import check_user, check_api
from qap import Toast
from reg import Reg
from api_dialog import API
from PySide6.QtWidgets import QStackedLayout


class Login(QWidget):
    signal = Signal(str)   # ⭐ 只负责把用户名发出去

    def __init__(self, parent=None):
        super().__init__(parent)

        # ===== 无边框 =====
        self.setWindowFlags(Qt.FramelessWindowHint)

        # ===== 加载 UI =====
        loader = QUiLoader()
        base_dir = os.path.dirname(__file__)
        ui_path = os.path.join(base_dir, "login.ui")

        file = QFile(ui_path)
        file.open(QFile.ReadOnly)
        self.root = loader.load(file)
        file.close()

        # ===== 注册页 =====
        self.reg_page = Reg()

        # ===== 页面栈 =====
        self.stack = QStackedLayout()
        self.stack.setContentsMargins(0, 0, 0, 0)

        self.stack.addWidget(self.root)
        self.stack.addWidget(self.reg_page)

        self.setLayout(self.stack)
        self.stack.setCurrentWidget(self.root)

        self.resize(380, 680)

        # ===== 控件绑定 =====
        self.user = self.root.findChild(QLineEdit, "user")
        self.password = self.root.findChild(QLineEdit, "password")
        self.login_button = self.root.findChild(QPushButton, "loginButton")
        self.reg_btn = self.root.findChild(QPushButton, "reg")
        self.que = self.root.findChild(QPushButton, "que")
        self.menu_button = self.root.findChild(QToolButton, "menuButton")

        self.user.setPlaceholderText("请输入用户名")
        self.password.setPlaceholderText("请输入密码")

        # ===== 事件 =====
        self.login_button.clicked.connect(self.handle_login)

        self.reg_btn.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.reg_page)
        )
        self.reg_page.b_signal.connect(
            lambda: self.stack.setCurrentWidget(self.root)
        )
        self.reg_page.signal.connect(
            lambda: self.stack.setCurrentWidget(self.root)
        )

        self.que.clicked.connect(
            lambda: QDesktopServices.openUrl(QUrl("https://www.baidu.com"))
        )

        self.init_menu()

    # ===== 菜单 =====
    def init_menu(self):
        self.menu = CustomMenu(self)

        self.menu.about_btn.clicked.connect(self.show_about)
        self.menu.exit_btn.clicked.connect(self.close)

        self.menu_button.clicked.connect(self.show_menu)

    def show_menu(self):
        pos = self.menu_button.mapToGlobal(
            self.menu_button.rect().bottomLeft() + QPoint(0, 6)
        )
        self.menu.move(pos)
        self.menu.show()

    def show_about(self):
        QMessageBox.about(
            self,
            "关于",
            "AzurChat v1.0\n\n基于 PySide6 开发"
        )

    # ===== 拖拽窗口 =====
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._drag_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            delta = event.globalPosition().toPoint() - self._drag_pos
            self.move(self.pos() + delta)
            self._drag_pos = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):
        self._drag_pos = None

    # ===== 登录逻辑 =====
    def handle_login(self):
        username = self.user.text().strip()
        password = self.password.text().strip()

        if not username or not password:
            Toast("用户名或密码不能为空", self)
            return

        if len(username) < 8 or len(password) < 8:
            Toast("用户名或密码长度不能少于8位", self)
            return

        result = check_user(username, password)

        if result == "not_exist":
            Toast("用户不存在", self)

        elif result == "success":
            api_ok = check_api(username)

            if api_ok:
                Toast("登录成功", self)
                self.signal.emit(username)   # ⭐核心：只发信号
            else:
                self.open_api_dialog(username)

        elif result == "wrong_password":
            Toast("密码错误", self)

        self.user.clear()
        self.password.clear()

    # ===== API弹窗 =====
    def open_api_dialog(self, username):
        self.blur = QGraphicsBlurEffect()
        self.blur.setBlurRadius(15)
        self.root.setGraphicsEffect(self.blur)

        self.api = API(parent=self, username=username)
        self.api.setGeometry(0, 0, self.width(), self.height())

        self.api.signal.connect(self.close_api_dialog)
        self.api.show()

    def close_api_dialog(self):
        self.root.setGraphicsEffect(None)
        self.api.close()