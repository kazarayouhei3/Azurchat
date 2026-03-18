import os
from PySide6.QtWidgets import QWidget, QPushButton, QToolButton, QTreeWidget, QTreeWidgetItem, QAbstractItemView, QVBoxLayout
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Signal, QSize, Qt, QEvent
from PySide6.QtGui import QIcon, QColor, QBrush
from PySide6.QtWidgets import QScrollArea

from fr_widget import GroupWidget


class Fr(QWidget):

    signal = Signal()
    my_signal = Signal()
    chat_signal = Signal()


    def __init__(self, parent=None):
        super().__init__(parent)
        loader = QUiLoader()

        base_dir = os.path.dirname(__file__)
        ui_path = os.path.join(base_dir, "fr.ui")

        file = QFile(ui_path)
        file.open(QFile.ReadOnly)
        self.root = loader.load(file)
        file.close()

        self.root.setParent(self)

        self.quit_button = self.root.findChild(QToolButton, "quit_button")

        self.quit_button.clicked.connect(self.signal.emit)

        self.chat = self.root.findChild(QToolButton, "chat")
        self.phone = self.root.findChild(QToolButton, "phone")
        self.my = self.root.findChild(QToolButton, "my")

        self.init_nav_button(
            self.chat,
            ":/icon/talk.svg",
            ":/icon/talk_select.svg",
            "聊天",
            False
        )
        self.init_nav_button(
            self.phone,
            ":/icon/phone.svg",
            ":/icon/phone_select.svg",
            "通讯录",
            True
        )

        self.init_nav_button(
            self.my,
            ":/icon/my.svg",
            ":/icon/my_select.svg",
            "我的",
            False
        )

        self.chat.clicked.connect(self.chat_signal.emit)
        self.my.clicked.connect(self.my_signal.emit)

        self.data = [
            {
                "name": "朋友",
                "items": []
            },
            {
                "name": "家人",
                "items": []
            }
        ]
        self.container = self.root.findChild(QWidget, "frList")

        # ===== Scroll =====
        self.scroll = QScrollArea(self.container)
        self.scroll.setWidgetResizable(True)
        self.scroll.setStyleSheet("border:none; background:transparent;")

        outer_layout = QVBoxLayout(self.container)
        outer_layout.setContentsMargins(0, 0, 0, 0)
        outer_layout.setSpacing(0)
        outer_layout.addWidget(self.scroll)

        # ===== inner =====
        self.inner = QWidget()
        self.layout = QVBoxLayout(self.inner)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.scroll.setWidget(self.inner)

        # ===== 渲染数据 =====
        for group in self.data:
            g = GroupWidget(group["name"])

            for item in group["items"]:
                g.add_item(item)

            self.layout.addWidget(g)

        self.layout.addStretch()

    def on_item_clicked(self, name):
        self.chat_signal.emit(name)

    def init_nav_button(self, btn, icon_normal, icon_active, text, state):
        btn._icon_normal = icon_normal
        btn._icon_active = icon_active

        btn.setText(text)

        btn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        if state:
            btn.setIcon(QIcon(icon_active))
            btn.setIconSize(QSize(20, 20))
        else:
            btn.setIcon(QIcon(icon_normal))
            btn.setIconSize(QSize(20, 20))
            btn.installEventFilter(self)

