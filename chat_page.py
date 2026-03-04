import os
from PySide6.QtWidgets import QWidget, QToolButton, QLabel
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile


class ChatPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        loader = QUiLoader()

        base_dir = os.path.dirname(__file__)
        ui_path = os.path.join(base_dir, "form_chat.ui")

        file = QFile(ui_path)
        file.open(QFile.ReadOnly)

        # ⭐关键：不要传 self 做 parent
        self.root = loader.load(file)   # 独立页面
        file.close()

        # 把加载的 root 塞进当前 ChatPage 的布局
        from PySide6.QtWidgets import QVBoxLayout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.root)

        # 找控件（用你截图里的名字）
        self.back_button = self.root.findChild(QToolButton, "mainButton")
        self.title_label = self.root.findChild(QLabel, "label")

    def bind_back(self, callback):
        if self.back_button:
            self.back_button.clicked.connect(callback)

    def set_title(self, title: str):
        if self.title_label:
            self.title_label.setText(title)
