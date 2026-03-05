import os
from PySide6.QtWidgets import QWidget, QPushButton, QToolButton, QLabel
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Signal, QSize, Qt, QRectF
from PySide6.QtGui import QIcon, QPixmap, QPainter, QPainterPath

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

        avatar_label = self.root.findChild(QLabel, "label_3")
        if avatar_label:
            size = 36

            # 1️⃣ 读取并等比填充
            src = QPixmap(":/new/prefix1/head.png").scaled(
                size, size,
                Qt.KeepAspectRatioByExpanding,
                Qt.SmoothTransformation
            )

            # 2️⃣ 创建透明画布
            result = QPixmap(size, size)
            result.fill(Qt.transparent)

            # 3️⃣ 开始绘制
            painter = QPainter(result)
            painter.setRenderHint(QPainter.Antialiasing)

            # ⭐ 圆形裁剪
            path_circle = QPainterPath()
            path_circle.addEllipse(QRectF(0, 0, size, size))
            painter.setClipPath(path_circle)

            # 4️⃣ 画图
            painter.drawPixmap(0, 0, src)
            painter.end()

            # 5️⃣ 设置到 QLabel
            avatar_label.setPixmap(result)
            avatar_label.setFixedSize(size, size)

        self.mem_button = self.root.findChild(QPushButton, "mem")
        self.top_button = self.root.findChild(QPushButton, "top")
        self.del_button = self.root.findChild(QPushButton, "del")

        self.mem_button.clicked.connect(self.mem_signal.emit)
        self.top_button.clicked.connect(self.top_signal.emit)
        self.del_button.clicked.connect(self.del_signal.emit)

        # ===== 3️⃣ 设置返回按钮图标 =====
        icon_path = os.path.join(base_dir, "go.png")
        self.back_button.setIcon(QIcon(icon_path))
        self.back_button.setIconSize(QSize(24, 24))
        self.back_button.setFixedSize(30, 30)
        self.back_button.setToolButtonStyle(Qt.ToolButtonIconOnly)
