# widget.py
import sys
from PySide6.QtWidgets import QApplication, QWidget, QStackedLayout

from list_page import ListPage
from chat_page import ChatPage
from chat_info import ChatCommand


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # ===== 两个页面 =====
        self.page_list = ListPage()
        self.page_chat = ChatPage()

        # ===== Stack 布局（不改页面尺寸）=====
        self.stack = QStackedLayout()
        self.stack.setContentsMargins(0, 0, 0, 0)
        self.stack.addWidget(self.page_list)  # index 0
        self.stack.addWidget(self.page_chat)  # index 1

        self.setLayout(self.stack)
        self.stack.setCurrentIndex(0)

        # ===== 页面信号绑定 =====
        # 返回按钮
        self.page_chat.bind_back(lambda: self.stack.setCurrentIndex(0))

        # 点击列表进入聊天页
        self.page_list.list.itemClicked.connect(self.open_chat)

        # “我的信息”菜单
        self.page_list.me_action.triggered.connect(self.open_info)

    # ===== 切换聊天页 =====
    def open_chat(self, item):
        w = self.page_list.list.itemWidget(item)
        title = w.name_label.text() if w else "聊天"
        self.page_chat.set_title(title)
        self.stack.setCurrentIndex(1)

    # ===== 打开信息页 =====
    def open_info(self):
        self.infoWin = ChatCommand(self)
        self.infoWin.show()
        self.infoWin.raise_()
        self.infoWin.activateWindow()


