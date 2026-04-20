# This Python file uses the following encoding: utf-8
from datetime import datetime, timedelta

from PySide6.QtWidgets import (
    QApplication, QWidget, QToolButton,
    QListWidgetItem, QStackedLayout, QSplashScreen, QPushButton,
    QVBoxLayout
)
from PySide6.QtCore import QSize, QTimer, QPropertyAnimation, QEasingCurve, QPoint

from personcord import Personcord
from qap import Toast
from setting_dialog import Setting
from ui_form import Ui_Widget

from chat_item import ChatItem
from chat_page import ChatPage
from PySide6.QtCore import Qt, QEvent

from PySide6.QtGui import QPixmap, QIcon

from Contact import Contact
from my import My
import rc_pic

from db import get_conversations_with_avatar, get_prompt_by_id, get_user_profile


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # ===== 主列表页 =====
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)

        # ===== 新增：代码里补一层全局页面管理，不动 ui =====
        old_layout = self.layout()
        if old_layout is None:
            raise RuntimeError("setupUi 后没有拿到根布局")

        # 取出原来 layout 里的所有子项，暂存
        items = []
        while old_layout.count():
            item = old_layout.takeAt(0)
            items.append(item)

        # home_page：承载原来整页 UI
        self.home_page = QWidget(self)
        self.home_page.setObjectName("home_page")

        home_layout = QVBoxLayout(self.home_page)
        home_layout.setContentsMargins(0, 0, 0, 0)
        home_layout.setSpacing(0)

        # 把原来布局里的内容放进 home_page
        for item in items:
            if item.widget():
                item.widget().setParent(self.home_page)
                home_layout.addWidget(item.widget())
            elif item.layout():
                home_layout.addLayout(item.layout())
            elif item.spacerItem():
                home_layout.addItem(item.spacerItem())

        # 删掉原来挂在 self 上的空布局
        QWidget().setLayout(old_layout)

        # 全局 stack：管理 home_page / chat_page / add_friend_page ...
        self.global_stack = QStackedLayout()
        self.global_stack.setContentsMargins(0, 0, 0, 0)
        self.global_stack.setSpacing(0)
        self.global_stack.addWidget(self.home_page)

        self.setLayout(self.global_stack)

        self.contact = Contact(self.ui.contact)
        self.contact.open_confirm_page.connect(self.bind_confirm_page_signal)
        self.contact.open_add_page.connect(self.bind_add_page_signal)


        self.page_chat = None

        self.ui.quit_button.clicked.connect(self.close)

        self.contact.add_success.connect(self.on_add_friend_success)
        # 点击会话进入聊天页
        self.ui.list.itemClicked.connect(self.open_chat_in_place)

        self.person_btn = self.ui.toolButton

        self.person_btn.clicked.connect(self.open_person_from_top)

        self.my = My()
        self.my.signal.connect(self.back_from_my)
        self.my.personcordsignal.connect(self.back_from_personcord)

        self.personcord = Personcord()
        self.personcord.signal.connect(self.back_my)
        self.global_stack.addWidget(self.personcord)

        self.setting_page = Setting()
        self.global_stack.addWidget(self.setting_page)

        # ===== 动画数据 =====
        self._anims = []
        self._play_index = 0

        self._chat_data = []

        self.drag_bar = self.ui.AzurChat
        self.current_user = None

        self.init_nav_button(
            self.ui.chat,
            ":/icon/talk.svg",
            ":/icon/talk_select.svg",
            "聊天",
            True
        )
        self.init_nav_button(
            self.ui.chatButton,
            ":/icon/talk.svg",
            ":/icon/talk_select.svg",
            "聊天",
            False  # ⭐ 默认不选中
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
        self.home_stack = self.ui.stackedWidget
        self.ui.chat.clicked.connect(
            lambda: self.nav(self.ui.chat, self.ui.mainPage)
        )

        self.ui.phone.clicked.connect(
            lambda: self.nav(self.ui.phone, self.ui.contact)
        )

        self.ui.my.clicked.connect(
            lambda: self.nav(self.ui.my, self.ui.setting)
        )
        self.ui.chatButton.clicked.connect(
            lambda: self.nav(self.ui.chatButton, self.ui.mainPage)
        )
        self.setting_btn = self.ui.setting.findChild(QPushButton, "settingButton")
        self.setting_btn.clicked.connect(self.on_setting_clicked)
        self.setting_btn.installEventFilter(self)

        self._last_chat_ids = []

    def show_add_page(self, page):
        if hasattr(page, "on_hide"):
            page.on_hide()

        if self.global_stack.indexOf(page) == -1:
            self.global_stack.addWidget(page)

        self.global_stack.setCurrentWidget(page)

    def show_confirm_page(self, page):
        if hasattr(page, "on_hide"):
            page.on_hide()

        if self.global_stack.indexOf(page) == -1:
            self.global_stack.addWidget(page)

        self.global_stack.setCurrentWidget(page)

    def open_person_from_top(self):
        if self.global_stack.indexOf(self.my) == -1:
            self.global_stack.addWidget(self.my)

        self.global_stack.setCurrentWidget(self.my)

    def back_from_my(self):
        # 回到主页
        self.global_stack.setCurrentWidget(self.home_page)
    def back_my(self):
        # 回到主页
        self.global_stack.setCurrentWidget(self.my)
    def back_from_personcord(self):
        # 回到主页
        self.global_stack.setCurrentWidget(self.personcord)
    def bind_confirm_page_signal(self, page):
        if hasattr(page, "on_hide"):
            page.on_hide()

        if self.global_stack.indexOf(page) == -1:
            self.global_stack.addWidget(page)

        # ⭐ 返回
        page.signal.connect(
            lambda: self.global_stack.setCurrentWidget(self.home_page)
        )

        page.b_signal.connect(
            lambda: self.global_stack.setCurrentWidget(self.home_page)
        )

        self.global_stack.setCurrentWidget(page)
    def bind_add_page_signal(self, page):
        if self.global_stack.indexOf(page) == -1:
            self.global_stack.addWidget(page)

        # ⭐ 关键：绑定返回
        if not hasattr(page, "_binded"):
            page.q_signal.connect(
                lambda: self.global_stack.setCurrentWidget(self.home_page)
            )
            page._binded = True

        self.global_stack.setCurrentWidget(page)

    def on_setting_clicked(self):

        Toast("等等吧", self)
    def nav(self, target_btn, target_page):
        for btn in [self.ui.chat, self.ui.chatButton, self.ui.phone, self.ui.my]:
            btn.setChecked(False)
            btn.setIcon(QIcon(btn._icon_normal))

        # 当前按钮选中
        target_btn.setChecked(True)
        target_btn.setIcon(QIcon(target_btn._icon_active))

        # 切页面
        self.home_stack.setCurrentWidget(target_page)

    def on_add_friend_success(self):
        self.refresh_chat_list()
        self.nav(self.ui.chat, self.ui.mainPage)
        self.global_stack.setCurrentWidget(self.home_page)

    def init_nav_button(self, btn, icon_normal, icon_active, text, state):
        btn._icon_normal = icon_normal
        btn._icon_active = icon_active

        btn.setText(text)
        btn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        btn.setCheckable(True)  # ⭐关键1
        btn.installEventFilter(self)  # ⭐关键2（所有按钮）

        if state:
            btn.setChecked(True)  # ⭐关键3
            btn.setIcon(QIcon(icon_active))
        else:
            btn.setChecked(False)
            btn.setIcon(QIcon(icon_normal))

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

        fid, name, msg, time_text, avatar_path, prompt = self._chat_data[self._play_index]
        self._play_index += 1

        item_widget = ChatItem(fid, name, msg, time_text, avatar_path)

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

    def after_login(self, username):
        self.current_user = username

        self.load_chat_data(self.current_user)
        self.contact.set_user(self.current_user)

        record = self.my.load_user(self.current_user)
        self.personcord.get_user(record)

        if not self.page_chat:
            self.page_chat = ChatPage()
            self.global_stack.addWidget(self.page_chat)

            self.page_chat.bind_back(
                lambda: self.back_to_list_and_refresh()
            )

        QTimer.singleShot(100, self.start_intro_anim)

    def open_chara_page(self):
        name = self.page_chat.current_name
        avatar = self.page_chat.current_avatar

        self.page_chara.set_chara_info(name, avatar)

        if self.global_stack.indexOf(self.page_chara) == -1:
            self.global_stack.addWidget(self.page_chara)

        self.global_stack.setCurrentWidget(self.page_chara)

    def back_to_list_and_refresh(self):
        self.refresh_chat_list()  # 先刷新列表
        self.nav(self.ui.chat, self.ui.mainPage)  # 主页内部回到聊天列表 tab
        self.global_stack.setCurrentWidget(self.home_page)  # 全局层回到主页

    def back_to_fr(self):
        self.contact.load_data()
        self.home_stack.setCurrentWidget(self.ui.contact)
        self.global_stack.setCurrentWidget(self.home_page)

    # ===== 切换聊天页 =====
    def open_chat_in_place(self, item: QListWidgetItem):
        w = self.ui.list.itemWidget(item)

        if not w:
            return

        fid = w.fid
        name = w.name_label.text()
        prompt = get_prompt_by_id(fid)
        avatar = w.avatar

        if not self.page_chat:
            self.page_chat = ChatPage()
            self.global_stack.addWidget(self.page_chat)
            self.page_chat.bind_back(
                lambda: self.back_to_list_and_refresh()
            )

        self.page_chat.set_chat(
            self.current_user,
            fid,
            name,
            prompt,
            avatar
        )

        self.global_stack.setCurrentWidget(self.page_chat)

    def render_static(self):
        for fid, name, msg, time_text, avatar_path, prompt in self._chat_data:
            item_widget = ChatItem(fid, name, msg, time_text, avatar_path)

            item = QListWidgetItem(self.ui.list)
            item.setSizeHint(QSize(0, 64))
            self.ui.list.addItem(item)
            self.ui.list.setItemWidget(item, item_widget)

        self.ui.list.scrollToBottom()

    def load_chat_data(self, username):
        data = get_conversations_with_avatar(username)

        self._chat_data = [
            (
                item["id"],
                item["name"],
                item["last_message"] or "",
                self.format_list_time(item["last_time"]) or "",
                item["avatar"] or "",
                item["prompt"] or ""  # ⭐加这个
            )
            for item in data
        ]

    def refresh_chat_list(self):
        self.ui.list.clear()

        old_ids = self._last_chat_ids.copy()

        self.load_chat_data(self.current_user)

        new_ids = [item[0] for item in self._chat_data]  # fid列表

        # ✅ 判断是否有新内容
        has_new = new_ids != old_ids

        self._last_chat_ids = new_ids

        if has_new:
            self.start_intro_anim()  # ✅ 只有变化才动画
        else:
            self.render_static()  # ✅ 否则直接渲染

    def format_list_time(self, time_str):
        if not time_str:
            return ""

        dt = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
        now = datetime.now()

        if dt.date() == now.date():
            return dt.strftime("%H:%M")
        elif dt.date() == now.date() - timedelta(days=1):
            return "昨天"
        elif dt.year == now.year:
            return dt.strftime("%m-%d")
        else:
            return dt.strftime("%Y-%m-%d")

    def bind_open_info(self, callback):
        tool_button = self.root.findChild(QToolButton, "menu")
        if tool_button:
            tool_button.clicked.connect(callback)
