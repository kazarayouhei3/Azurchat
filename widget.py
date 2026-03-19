# This Python file uses the following encoding: utf-8
import sys
from datetime import datetime

from PySide6.QtWidgets import (
    QApplication, QWidget, QMenu, QToolButton,
    QListWidgetItem, QStackedLayout, QSplashScreen
)
from PySide6.QtCore import QSize, QTimer, QPropertyAnimation, QEasingCurve, QPoint

from ui_form import Ui_Widget

from chat_item import ChatItem
from chat_page import ChatPage
from PySide6.QtCore import Qt, QEvent
from chat_info import ChatCommand
from PySide6.QtGui import QPixmap, QIcon
from chara import Chara
from login import Login
from reg import Reg
from fr import Fr

from db import init_db,  get_conversations_with_avatar


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        init_db()
        # ===== 主列表页 =====
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)

        # ===== stack 结构（同窗口切换）=====
        old_layout = self.layout()

        self.page_list = QWidget()
        self.page_list.setLayout(old_layout)

        self.info = ChatCommand()

        self.login = Login()

        self.page_chat = None

        self.reg = Reg()
        self.fr = Fr()

        self.stack = QStackedLayout(self)
        self.stack.setContentsMargins(0, 0, 0, 0)
        self.stack.addWidget(self.page_list)  # index 0


        self.setLayout(self.stack)

        self.page_chara = Chara()
        self.stack.addWidget(self.page_chara)  # index 2
        self.stack.addWidget(self.info)  # index 3
        self.stack.addWidget(self.login)  # index 4
        self.stack.addWidget(self.reg)  # index 5
        self.stack.addWidget(self.fr)  # index 5

        self.stack.setCurrentWidget(self.login)

        self.ui.quit_button.clicked.connect(self.close)

        self.login.signal.connect(self.after_login)

        self.login.reg_signal.connect(
            lambda: self.stack.setCurrentWidget(self.reg)
        )

        self.reg.b_signal.connect(
            lambda: self.stack.setCurrentWidget(self.login)
        )

        self.reg.signal.connect(
            lambda: self.stack.setCurrentWidget(self.login)
        )

        # 点击会话进入聊天页
        self.ui.list.itemClicked.connect(self.open_chat_in_place)

        # ===== 动画数据 =====
        self._anims = []
        self._play_index = 0


        self._chat_data = [
            ("希佩尔", "", datetime.now().strftime("%H:%M"), ":/new/prefix3/icon/hipper.png"),
            ("企业", " ", datetime.now().strftime("%H:%M"), ":/new/prefix3/icon/enterprise.png"),
            ("塔什干", " ", datetime.now().strftime("%H:%M"), ":/new/prefix3/icon/Tashkent.png"),
        ]

        self.drag_bar = self.ui.AzurChat


        self.init_nav_button(
            self.ui.chat,
            ":/icon/talk.svg",
            ":/icon/talk_select.svg",
            "聊天",
            True
        )
        self.init_nav_button(
            self.ui.phone,
            ":/icon/phone.svg",
            ":/icon/phone_select.svg",
            "通讯录",
            False
        )

        self.init_nav_button(
            self.ui.my,
            ":/icon/my.svg",
            ":/icon/my_select.svg",
            "我的",
            False
        )

        self.ui.phone.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.fr)
        )
        self.ui.my.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.info)
        )

        self.fr.chat_signal.connect(
            lambda: self.stack.setCurrentWidget(self.page_list)
        )
        self.fr.my_signal.connect(
            lambda: self.stack.setCurrentWidget(self.info)
        )
        self.fr.signal.connect(self.close)

        self.info.chat_signal.connect(
            lambda: self.stack.setCurrentWidget(self.page_list)
        )

        self.info.phone_signal.connect(
            lambda: self.stack.setCurrentWidget(self.fr)
        )


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

    def eventFilter(self, obj, event):

        if hasattr(obj, "_icon_normal"):

            if event.type() == QEvent.Enter:
                if not obj.isChecked():
                    obj.setIcon(QIcon(obj._icon_active))

            elif event.type() == QEvent.Leave:
                    if not obj.isChecked():
                        obj.setIcon(QIcon(obj._icon_normal))

        return super().eventFilter(obj, event)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._drag_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if self._drag_pos and (event.buttons() & Qt.LeftButton):
            delta = event.globalPosition().toPoint() - self._drag_pos
            self.move(self.pos() + delta)

            self._drag_pos = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):
        self._drag_pos = None

    def start_intro_anim(self):
        self.ui.list.clear()  # ❗必须加
        self._play_index = 0
        self.play_next_one()

    def play_next_one(self):
        if self._play_index >= len(self._chat_data):
            return

        name, msg, time_text, avatar_path = self._chat_data[self._play_index]
        self._play_index += 1

        item_widget = ChatItem(name, msg, time_text, avatar_path)

        item = QListWidgetItem(self.ui.list)
        item.setSizeHint(QSize(0, 64))
        self.ui.list.addItem(item)
        self.ui.list.setItemWidget(item, item_widget)

        self.ui.list.scrollToBottom()

        # ❗延迟执行动画（关键）
        QTimer.singleShot(0, lambda: self.run_anim(item_widget))

    def run_anim(self, item_widget):
        target = item_widget

        # ❗确保拿到的是最终布局位置
        end_pos = target.pos()

        start_pos = QPoint(end_pos.x() + 300, end_pos.y())
        overshoot = QPoint(end_pos.x() - 10, end_pos.y())

        target.move(start_pos)

        anim1 = QPropertyAnimation(target, b"pos", self)
        anim1.setDuration(300)
        anim1.setStartValue(start_pos)
        anim1.setEndValue(overshoot)
        anim1.setEasingCurve(QEasingCurve.OutExpo)

        anim2 = QPropertyAnimation(target, b"pos", self)
        anim2.setDuration(150)
        anim2.setStartValue(overshoot)
        anim2.setEndValue(end_pos)
        anim2.setEasingCurve(QEasingCurve.OutCubic)

        anim1.finished.connect(anim2.start)

        # ❗下一个人延迟
        anim2.finished.connect(lambda: QTimer.singleShot(300, self.play_next_one))

        self._anims.extend([anim1, anim2])
        anim1.start()

    def after_login(self):

        if not self.page_chat:
            self.page_chat = ChatPage()

            self.stack.addWidget(self.page_chat)

            self.page_chat.bind_back(
                lambda: self.stack.setCurrentWidget(self.page_list)
            )

            self.page_chat.bind_open_chara(
                lambda: self.stack.setCurrentWidget(self.page_chara)
            )

        self.stack.setCurrentWidget(self.page_list)
        QTimer.singleShot(100, self.start_intro_anim)

    # ===== 切换聊天页 =====
    def open_chat_in_place(self, item: QListWidgetItem):
        w = self.ui.list.itemWidget(item)
        role = w.name_label.text() if w else "聊天"

        # ⭐ 关键：传角色
        self.page_chat.set_role(role)

        # 设置标题
        self.page_chat.set_title(role)

        # 切页面
        self.stack.setCurrentWidget(self.page_chat)

    def load_chat_data(self, username):
        data = get_conversations_with_avatar(username)

        self._chat_data = [
            (name, msg or "", t or "", avatar or "")
            for name, msg, t, avatar in data
        ]

    def bind_open_info(self, callback):
        tool_button = self.root.findChild(QToolButton, "menu")
        if tool_button:
            tool_button.clicked.connect(callback)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(":/new/prefix1/azur.ico"))
    # ===== 加载图 =====
    splash_pix = QPixmap("logo.png")  # 你的加载图
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.show()
    app.processEvents()  # 刷新界面
    # ===== 模拟加载时间 =====
    QTimer.singleShot(1500, splash.close)  # 1.5秒后关闭
    # ===== 主窗口 =====
    widget = Widget()
    QTimer.singleShot(1500, widget.show)
    sys.exit(app.exec())
