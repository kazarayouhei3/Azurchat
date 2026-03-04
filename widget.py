# This Python file uses the following encoding: utf-8
import sys
from datetime import datetime

from PySide6.QtWidgets import (
    QApplication, QWidget, QMenu, QToolButton,
    QListWidgetItem, QStackedLayout
)
from PySide6.QtCore import QSize, QTimer, QPropertyAnimation, QEasingCurve, QPoint

from ui_form import Ui_Widget
from form2 import InfoWindow
from chat_item import ChatItem
from chat_page import ChatPage


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # ===== 主列表页 =====
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # ===== stack 结构（同窗口切换）=====
        old_layout = self.layout()

        self.page_list = QWidget()
        self.page_list.setLayout(old_layout)

        self.page_chat = ChatPage()

        self.stack = QStackedLayout(self)
        self.stack.setContentsMargins(0, 0, 0, 0)
        self.stack.addWidget(self.page_list)  # index 0
        self.stack.addWidget(self.page_chat)  # index 1

        self.setLayout(self.stack)
        self.stack.setCurrentIndex(0)

        # ⭐ 绑定返回按钮（通过 ChatPage 提供的方法）
        self.page_chat.bind_back(lambda: self.stack.setCurrentIndex(0))

        # ===== menu =====
        menu = QMenu(self)
        menu.addAction("通讯录")
        me_action = menu.addAction("我的信息")
        menu.addSeparator()
        exit_action = menu.addAction("退出")
        exit_action.triggered.connect(self.close)

        self.ui.toolButton.setPopupMode(QToolButton.InstantPopup)
        self.ui.toolButton.setMenu(menu)
        self.ui.toolButton.setStyleSheet("""
        QToolButton {
            border: none;
            padding: 2px;
        }

        QToolButton:hover {
            background-color: #e6e6e6;
            border-radius: 4px;
        }

        QToolButton:pressed {
            background-color: #d0d0d0;
        }

        /* 关键：干掉下拉箭头 */
        QToolButton::menu-indicator {
            image: none;
        }
        """)
        me_action.triggered.connect(self.open_info)

        # 点击会话进入聊天页
        self.ui.list.itemClicked.connect(self.open_chat_in_place)

        # ===== 动画数据 =====
        self._anims = []
        self._play_index = 0

        self._chat_data = [
            ("希佩尔", "你这家伙！！！", datetime.now().strftime("%H:%M")),
            ("碧蓝交友群", "赤城：呵呵呵", datetime.now().strftime("%H:%M")),
        ]

        QTimer.singleShot(1000, self.start_intro_anim)

    # ===== 动画 =====
    def start_intro_anim(self):
        self._play_index = 0
        self.play_next_one()

    def play_next_one(self):
        if self._play_index >= len(self._chat_data):
            return

        name, msg, time_text = self._chat_data[self._play_index]
        self._play_index += 1

        item_widget = ChatItem(name, msg, time_text)

        item = QListWidgetItem(self.ui.list)
        item.setSizeHint(QSize(0, 64))
        self.ui.list.addItem(item)
        self.ui.list.setItemWidget(item, item_widget)

        self.ui.list.scrollToBottom()

        target = item_widget.content
        item_widget.show()

        end_pos = target.pos()
        start_pos = QPoint(end_pos.x() + 260, end_pos.y())
        overshoot = QPoint(end_pos.x() - 12, end_pos.y())

        target.move(start_pos)

        anim1 = QPropertyAnimation(target, b"pos", self)
        anim1.setDuration(350)
        anim1.setStartValue(start_pos)
        anim1.setEndValue(overshoot)
        anim1.setEasingCurve(QEasingCurve.OutExpo)

        anim2 = QPropertyAnimation(target, b"pos", self)
        anim2.setDuration(200)
        anim2.setStartValue(overshoot)
        anim2.setEndValue(end_pos)
        anim2.setEasingCurve(QEasingCurve.OutCubic)

        anim1.finished.connect(anim2.start)
        anim2.finished.connect(lambda: QTimer.singleShot(180, self.play_next_one))

        self._anims.extend([anim1, anim2])
        anim1.start()

    # ===== 切换聊天页 =====
    def open_chat_in_place(self, item: QListWidgetItem):
        w = self.ui.list.itemWidget(item)
        title = w.name_label.text() if w else "聊天"

        # 通过 ChatPage 提供的 set_title 方法设置标题
        self.page_chat.set_title(title)

        # 切换页面
        self.stack.setCurrentIndex(1)

    # ===== 信息页 =====
    def open_info(self):
        if not hasattr(self, "infoWin"):
            self.infoWin = InfoWindow(self)
        self.infoWin.show()
        self.infoWin.raise_()
        self.infoWin.activateWindow()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
