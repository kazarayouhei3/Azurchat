import os

from PySide6.QtWidgets import (
    QWidget, QLineEdit, QVBoxLayout, QScrollArea, QToolButton, QSizePolicy
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Signal, Qt

from db import is_friend, get_groups
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

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setStyleSheet("border:none; background:transparent;")

        outer_layout = QVBoxLayout(self.container)
        outer_layout.setContentsMargins(0, 0, 0, 0)
        outer_layout.addWidget(self.scroll)

        self.inner = QWidget()
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.inner.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.layout = QVBoxLayout(self.inner)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.layout.setAlignment(Qt.AlignTop)

        self.scroll.setWidget(self.inner)

        # ===== 数据 =====
        data = get_groups()
        self.groups = []

        for group in data:
            g = GroupWidget(group["name"])

            # ⭐关键：接收点击
            g.item_signal.connect(self.on_item_selected)

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
        self.popup = Suggest(self.root)
        self.popup.setFixedWidth(self.search.width() - 20)
        self.popup.selected.connect(self.on_add_friend)

        self.search.textChanged.connect(self.show_suggest)

        self.search.installEventFilter(self)
        self.installEventFilter(self)

    def on_item_selected(self, fid):
        # 清空所有 group 的选中
        for group in self.groups:
            if group.current_selected:
                w = group.current_selected
                w.setProperty("selected", False)
                w.style().unpolish(w)
                w.style().polish(w)
                group.current_selected = None

        # 再执行原逻辑
        self.on_add_friend(fid)
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

        width = self.search.width()
        self.popup.setFixedWidth(width)

        pos = self.search.mapTo(self.root, self.search.rect().bottomLeft())
        self.popup.move(pos.x(), pos.y() + 6)

        self.popup.show()
        self.popup.raise_()
        self.popup.activateWindow()

    def on_hide(self):
        if self.popup:
            self.popup.hide()
    def closeEvent(self, event):
        if self.popup:
            self.popup.hide()
        self.search.clear()  # 可选：顺便清空输入
        super().closeEvent(event)
    # ===== 更新列表 UI =====
    def update_group_item(self, friend_id):
        for group in self.groups:
            group.set_added(friend_id)

    # ===== 添加好友 =====
    def on_add_friend(self, friend_id):
        if self.popup:
            self.popup.hide()
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

    def eventFilter(self, obj, event):
        from PySide6.QtCore import QEvent

        if event.type() == QEvent.MouseButtonPress:
            # 点击的不是搜索框和popup
            if not self.search.geometry().contains(self.search.mapFromGlobal(event.globalPosition().toPoint())):
                if self.popup and self.popup.isVisible():
                    self.popup.hide()

        return super().eventFilter(obj, event)