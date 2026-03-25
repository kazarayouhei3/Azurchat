import os

from PySide6.QtWidgets import (
    QWidget, QLineEdit, QVBoxLayout, QScrollArea, QToolButton
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Signal

from db import add_friend, is_friend, get_groups
from fr_widget import GroupWidget
from search import Suggest

class Add_Friend(QWidget):
    signal = Signal()
    q_signal = Signal()
    add_request = Signal(str, str, str)

    def __init__(self, username, parent=None):
        super().__init__(parent)

        self.username = username

        loader = QUiLoader()
        base_dir = os.path.dirname(__file__)
        ui_path = os.path.join(base_dir, "add_friend.ui")

        file = QFile(ui_path)
        file.open(QFile.ReadOnly)
        self.root = loader.load(file)
        file.close()

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(self.root)

        # ===== 搜索 =====
        self.search = self.root.findChild(QLineEdit, "search")
        self.search.setPlaceholderText("搜索朋友")

        self.quit_button = self.root.findChild(QToolButton, "quit_button")
        self.quit_button.clicked.connect(self.q_signal.emit)

        # ===== Scroll =====
        self.container = self.root.findChild(QWidget, "friend_widget")

        self.scroll = QScrollArea(self.container)
        self.scroll.setWidgetResizable(True)
        self.scroll.setStyleSheet("border:none; background:transparent;")

        outer_layout = QVBoxLayout(self.container)
        outer_layout.setContentsMargins(0, 0, 0, 0)
        outer_layout.addWidget(self.scroll)

        self.inner = QWidget()
        self.layout = QVBoxLayout(self.inner)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.scroll.setWidget(self.inner)

        # ===== 数据 =====
        data = get_groups()
        self.groups = []

        for group in data:
            g = GroupWidget(group["name"])

            # ⭐关键：接收点击
            g.item_signal.connect(self.on_add_friend)

            for item in group["items"]:
                g.add_item(item["id"], item["name"], item["avatar"])

            self.layout.addWidget(g)
            self.groups.append(g)

        for group in self.groups:
            for i in range(group.content_layout.count()):
                item = group.content_layout.itemAt(i).widget()
                if not item:
                    continue

                friend_id = item.property("friend_id")

                if is_friend(self.username, friend_id):
                    group.set_added(friend_id)
        self.layout.addStretch()

        # ===== Suggest =====
        self.popup = Suggest(self)
        self.popup.setFixedWidth(self.search.width() - 20)
        self.popup.selected.connect(self.on_add_friend)

        self.search.textChanged.connect(self.show_suggest)

    # ===== 搜索 =====
    def show_suggest(self, text):
        text = text.strip()

        if not text:
            self.popup.hide()
            return

        result = []

        for group in self.groups:
            for i in range(group.content_layout.count()):
                item = group.content_layout.itemAt(i).widget()
                if not item:
                    continue

                name = item.property("name")
                avatar = item.property("avatar")
                friend_id = item.property("friend_id")

                if name and text in name:
                    result.append({
                        "id": friend_id,
                        "name": name,
                        "avatar": avatar,
                        "added": is_friend(self.username, friend_id)
                    })

        if not result:
            self.popup.hide()
            return

        self.popup.set_data(result[:10])
        self.popup.setFixedWidth(self.search.width())

        pos = self.search.mapToGlobal(self.search.rect().bottomLeft())

        self.popup.move(pos.x(), pos.y() + 6)
        self.popup.setFixedWidth(self.search.width())

        self.popup.show()
        self.popup.raise_()

        self.search.setFocus()
    # ===== 更新列表 UI =====
    def update_group_item(self, friend_id):
        for group in self.groups:
            group.set_added(friend_id)

    # ===== 添加好友 =====
    def on_add_friend(self, friend_id):
        # ⭐关键：如果已添加，直接不处理
        if is_friend(self.username, friend_id):
            return

        for group in self.groups:
            for i in range(group.content_layout.count()):
                item = group.content_layout.itemAt(i).widget()
                if not item:
                    continue

                if item.property("friend_id") == friend_id:
                    name = item.property("name")
                    avatar = item.property("avatar")
                    self.add_request.emit(friend_id, name, avatar)
                    return