import os

from PySide6.QtCore import Signal, QFile, Qt
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QWidget, QToolButton, QLabel, QLineEdit, QGraphicsDropShadowEffect, QPushButton

from db import get_user_profile, update_user_signature
from qap import get_round_pixmap


class My(QWidget):
    signal = Signal()
    personcordsignal  = Signal()
    def __init__(self, parent=None):
        super().__init__(parent)

        # ===== UI加载 =====
        loader = QUiLoader()
        base_dir = os.path.dirname(__file__)
        ui_path = os.path.join(base_dir, "person.ui")

        file = QFile(ui_path)
        file.open(QFile.ReadOnly)
        self.root = loader.load(file)
        file.close()
        self.root.setParent(self)
        self.root.setFocusPolicy(Qt.StrongFocus)
        self.quit_button = self.root.findChild(QToolButton, "quit_button")
        self.quit_button.clicked.connect(self.signal.emit)
        self.personcordButton = self.root.findChild(QPushButton, "personcordButton")
        self.personcordButton.clicked.connect(self.personcordsignal.emit)

    def set_user_info(
            self,
            nickname,
            avatar,
            level,
            exp,
            signature,
            region=None,
            birthday=None
    ):
        """
        个人主页显示函数
        """

        # ===== 找控件 =====
        self.name_label = self.root.findChild(QLabel, "name")
        self.avatar_label = self.root.findChild(QLabel, "head")
        self.level_label = self.root.findChild(QLabel, "rank")  # 你这个叫 rank，但实际是等级
        self.signature_edit = self.root.findChild(QLineEdit, "lineEdit")

        # ===== 显示昵称 =====
        if self.name_label:
            self.name_label.setText(nickname)

        # ===== 显示等级 =====
        if self.level_label:
            self.level_label.setText(f"Lv.{level}")

        # ===== 显示签名 =====
        if self.signature_edit:
            self.signature_edit.setText(signature)

        if not hasattr(self, "_binded_signature"):
            self.signature_edit.editingFinished.connect(self.save_signature)
            self._binded_signature = True

        # ===== 显示头像 =====
        if self.avatar_label:
            pixmap = get_round_pixmap(
                avatar,
                size=60
            )
            self.avatar_label.setPixmap(pixmap)

    def load_user(self, username):
        self.username = username   # ⭐必须有

        profile = get_user_profile(username)

        if profile:
            self.old_signature = profile.get("signature", "")
            self.set_user_info(**profile)
        return profile

    def save_signature(self):

        text = self.signature_edit.text().strip()

        # 默认文案处理（可选）
        if not text:
            text = ""

        if hasattr(self, "username") and self.username:
            update_user_signature(self.username, text)