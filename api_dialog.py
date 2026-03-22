import os
import requests
from PySide6.QtWidgets import (
    QWidget, QToolButton, QLabel,
    QHBoxLayout, QListWidget,
    QListWidgetItem, QSizePolicy,
    QLineEdit, QPushButton,
    QMenu, QApplication,QComboBox
)

from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QSize, Qt, QPropertyAnimation, QEasingCurve, QPoint
from PySide6.QtWidgets import QGraphicsOpacityEffect, QMessageBox
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Signal
from PySide6.QtCore import QTimer
import sqlite3
import rc_pic
import json

from db import update_user_api
import rc_pic
class API(QWidget):
    signal = Signal()
    reg_signal = Signal()
    def __init__(self, parent=None, username = None):
        super().__init__(parent)

        # ===== 1️⃣ 加载 UI =====
        loader = QUiLoader()
        base_dir = os.path.dirname(__file__)
        ui_path = os.path.join(base_dir, "api_dialog.ui")

        file = QFile(ui_path)
        file.open(QFile.ReadOnly)
        self.root = loader.load(file)
        file.close()

        # 把 UI 根挂到当前页面
        self.root.setParent(self)
        self.username = username
        self.url = self.root.findChild(QLineEdit, "url")
        self.api = self.root.findChild(QLineEdit, "API")

        self.url.setPlaceholderText("请输入url")
        self.api.setPlaceholderText("请输入API")

        self.login_button = self.root.findChild(QPushButton, "loginButton")

        self.login_button.clicked.connect(self.hand_model)

        self.login = self.root.findChild(QPushButton, "login")

        self.login.clicked.connect(self.hand_login)

        self.model = self.root.findChild(QPushButton, "model")
        self.model.clicked.connect(self.handle_model)

        self.comboBox = self.root.findChild(QComboBox, "comboBox")
        self.comboBox.setPlaceholderText("请选择模型")

    def hand_login(self):
        self.signal.emit()

    def hand_model(self):
        model = self.comboBox.currentText()

        if not model:
            Toast("请先选择模型", self)
            return

        data = {}

        # 加入 model
        data["username"] = self.username
        data["model"] = model

        # 写回 config
        with open("config.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        self.signal.emit()
        self.close()

    def get_models(self, api, base_url):

        url = base_url.rstrip("/") + "/models"

        headers = {
            "Authorization": f"Bearer {api}"
        }

        try:

            r = requests.get(url, headers=headers, timeout=10)

            if r.status_code == 200:

                data = r.json()
                return [m["id"] for m in data["data"]]

            else:
                return None

        except:
            return None

    def handle_model(self):

        api = self.api.text().strip()
        url = self.url.text().strip()

        if not api or not url:
            Toast("API或URL不能为空", self)
            return

        models = self.get_models(api, url)

        if not models:
            Toast("API或URL错误", self)
            return

        # 填充模型
        self.comboBox.clear()
        for m in models:
            self.comboBox.addItem(m)


        # 保存 API 和 URL
        update_user_api(self.username, api, url)

        Toast("模型加载成功", self)

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
