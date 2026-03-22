import os
from PySide6.QtWidgets import QWidget, QPushButton, QToolButton, QVBoxLayout, QScrollArea
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Signal, QSize, Qt, QEvent
from PySide6.QtGui import QIcon

from db import get_friends_list
from fr_widget import GroupWidget

class Fr(QWidget):

    signal = Signal()
    my_signal = Signal()
    chat_signal = Signal()
    c_signal = Signal()

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

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(self.root)

        # ===== 按钮 =====
        self.quit_button = self.root.findChild(QToolButton, "quit_button")
        self.chat = self.root.findChild(QToolButton, "chat")
        self.phone = self.root.findChild(QToolButton, "phone")
        self.my = self.root.findChild(QToolButton, "my")
        self.fr_button = self.root.findChild(QPushButton, "fr")

        self.quit_button.clicked.connect(self.signal.emit)
        self.chat.clicked.connect(self.chat_signal.emit)
        self.my.clicked.connect(self.my_signal.emit)
        self.fr_button.clicked.connect(self.c_signal.emit)

        # ===== 导航按钮 =====
        self.init_nav_button(self.chat, ":/icon/talk.svg", ":/icon/talk_select.svg", "聊天", False)
        self.init_nav_button(self.phone, ":/icon/phone.svg", ":/icon/phone_select.svg", "通讯录", True)
        self.init_nav_button(self.my, ":/icon/my.svg", ":/icon/my_select.svg", "我的", False)

        # ===== 容器 =====
        self.container = self.root.findChild(QWidget, "frList")

        self.scroll = QScrollArea(self.container)
        self.scroll.setWidgetResizable(True)
        self.scroll.setStyleSheet("border:none; background:transparent;")

        outer_layout = QVBoxLayout(self.container)
        outer_layout.setContentsMargins(0, 0, 0, 0)
        outer_layout.setSpacing(0)
        outer_layout.addWidget(self.scroll)

        self.inner = QWidget()
        self.layout = QVBoxLayout(self.inner)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.scroll.setWidget(self.inner)
        self.layout.setAlignment(Qt.AlignTop)


    # ===== 核心：加载好友 =====
    def load_data(self, username):
        # 清空旧UI
        for i in reversed(range(self.layout.count())):
            item = self.layout.itemAt(i).widget()
            if item:
                item.setParent(None)

        friends = get_friends_list(username)

        g = GroupWidget("朋友")

        for item in friends:
            g.add_item(item["id"], item["name"], item["avatar"], show_add=False)

        self.layout.addWidget(g)


    def init_nav_button(self, btn, icon_normal, icon_active, text, state):
        btn._icon_normal = icon_normal
        btn._icon_active = icon_active

        btn.setText(text)
        btn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        if state:
            btn.setIcon(QIcon(icon_active))
        else:
            btn.setIcon(QIcon(icon_normal))
            btn.installEventFilter(self)

        btn.setIconSize(QSize(20, 20))

    def eventFilter(self, obj, event):
        if hasattr(obj, "_icon_normal"):
            if event.type() == QEvent.Enter:
                obj.setIcon(QIcon(obj._icon_active))
            elif event.type() == QEvent.Leave:
                obj.setIcon(QIcon(obj._icon_normal))
        return super().eventFilter(obj, event)