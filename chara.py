import os
from PySide6.QtWidgets import QWidget, QPushButton, QToolButton, QLabel
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Signal, QSize, Qt, QRectF
from PySide6.QtGui import QIcon, QPixmap, QPainter, QPainterPath

from qap import Toast, get_round_pixmap


class Chara(QWidget):

    back_signal = Signal()
    mem_signal = Signal()
    top_signal = Signal()
    del_signal = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        loader = QUiLoader()

        base_dir = os.path.dirname(__file__)
        ui_path = os.path.join(base_dir, "form_chara.ui")

        file = QFile(ui_path)
        file.open(QFile.ReadOnly)
        self.root = loader.load(file)
        file.close()

        self.root.setParent(self)

        # 如果有返回按钮
        self.back_button = self.root.findChild(QToolButton, "mainButton")


        self.back_button.clicked.connect(self.back_signal.emit)
        self.name = self.root.findChild(QLabel, "name")
        self.pix = self.root.findChild(QLabel, "pix")


        self.mem_button = self.root.findChild(QPushButton, "mem")
        self.top_button = self.root.findChild(QPushButton, "top")
        self.del_button = self.root.findChild(QPushButton, "del")

        self.mem_button.clicked.connect(self.on_mem_clicked)
        self.top_button.clicked.connect(self.on_top_clicked)
        self.del_button.clicked.connect(self.on_del_clicked)

        # ===== 3️⃣ 设置返回按钮图标 =====
        icon_path = os.path.join(base_dir, "go.png")
        self.back_button.setIcon(QIcon(icon_path))
        self.back_button.setIconSize(QSize(24, 24))
        self.back_button.setFixedSize(30, 30)
        self.back_button.setToolButtonStyle(Qt.ToolButtonIconOnly)

    def set_chara_info(self, name, avatar):
        if self.name:
            self.name.setText(name)


        if self.pix and avatar:
            pix = get_round_pixmap(avatar, 36)
            self.pix.setPixmap(pix)
            self.pix.setFixedSize(36, 36)

    def on_mem_clicked(self):
        Toast("等等吧", self)
        self.mem_signal.emit()

    def on_top_clicked(self):
        Toast("等等吧", self)
        self.top_signal.emit()

    def on_del_clicked(self):
        Toast("等等吧", self)
        self.del_signal.emit()
