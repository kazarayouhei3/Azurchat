import os

from PySide6.QtWidgets import (
    QWidget, QLineEdit, QVBoxLayout, QScrollArea, QToolButton, QSizePolicy, QLabel, QPushButton
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Signal, Qt

from db import is_friend, get_groups
from fr_widget import GroupWidget
from search import Suggest
class Setting(QWidget):
    signal = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        loader = QUiLoader()
        base_dir = os.path.dirname(__file__)
        ui_path = os.path.join(base_dir, "setting_dialog.ui")

        file = QFile(ui_path)
        file.open(QFile.ReadOnly)
        self.root = loader.load(file)
        file.close()

        self.root.setParent(self)

        # ⭐ 缓存控件
        self.label = self.root.findChild(QLabel, "label")
        self.line = self.root.findChild(QLineEdit, "line")
        self.button = self.root.findChild(QPushButton, "button")

        # ⭐ 绑定按钮
        self.button.clicked.connect(self.handle_ok)

    def set_data(self, title, value):
        if self.label:
            self.label.setText(title)

        if self.line:
            self.line.setText(value)

    def handle_ok(self):
        self.signal.emit()
        self.close()