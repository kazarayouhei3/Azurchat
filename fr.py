import os
import threading

from PySide6.QtWidgets import (
    QWidget, QPushButton, QToolButton, QVBoxLayout, QScrollArea,
    QStackedLayout
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Signal, QSize, Qt, QEvent
from PySide6.QtGui import QIcon

from db import get_friends_list, add_friend, add_conversation, update_conversation_last, insert_message, get_conv_id, \
    get_prompt_by_id
from fr_widget import GroupWidget
from add_friend import Add_Friend
from friend import Friend
from use_api import Chat


class Fr(QWidget):
    signal = Signal()
    my_signal = Signal()
    chat_signal = Signal()
    add_success = Signal()
    ai_reply_signal = Signal(str, str)
    def __init__(self, parent=None):
        super().__init__(parent)

        self.current_user = None
        self.pending_friend = None

        self.stack = QStackedLayout(self)
        self.stack.setContentsMargins(0, 0, 0, 0)

        self._build_list_page()
        self._build_sub_pages()

        self.stack.setCurrentWidget(self.list_page)

        self.ai_reply_signal.connect(self.handle_ai_reply)

    def _build_list_page(self):
        loader = QUiLoader()
        base_dir = os.path.dirname(__file__)
        ui_path = os.path.join(base_dir, "fr.ui")

        file = QFile(ui_path)
        file.open(QFile.ReadOnly)
        self.list_page = loader.load(file)
        file.close()

        self.stack.addWidget(self.list_page)

        self.quit_button = self.list_page.findChild(QToolButton, "quit_button")
        self.chat = self.list_page.findChild(QToolButton, "chat")
        self.phone = self.list_page.findChild(QToolButton, "phone")
        self.my = self.list_page.findChild(QToolButton, "my")
        self.fr_button = self.list_page.findChild(QPushButton, "fr")

        self.quit_button.clicked.connect(self.signal.emit)
        self.chat.clicked.connect(self.chat_signal.emit)
        self.my.clicked.connect(self.my_signal.emit)
        self.fr_button.clicked.connect(self.open_add_friend)

        self.init_nav_button(self.chat, ":/icon/talk.svg", ":/icon/talk_select.svg", "聊天", False)
        self.init_nav_button(self.phone, ":/icon/phone.svg", ":/icon/phone_select.svg", "通讯录", True)
        self.init_nav_button(self.my, ":/icon/my.svg", ":/icon/my_select.svg", "我的", False)

        self.container = self.list_page.findChild(QWidget, "frList")

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
        self.layout.setAlignment(Qt.AlignTop)

        self.scroll.setWidget(self.inner)

    def _build_sub_pages(self):
        self.add_friend_page = Add_Friend(username="")
        self.friend_page = Friend()

        self.stack.addWidget(self.add_friend_page)
        self.stack.addWidget(self.friend_page)

        self.add_friend_page.add_request.connect(self.open_confirm_page)
        self.add_friend_page.q_signal.connect(self.back_to_list)

        self.friend_page.signal.connect(self.back_to_list)
        self.friend_page.b_signal.connect(self.back_to_list)
        self.friend_page.a_signal.connect(self.confirm_add)

    def notify_chat_update(self):
        parent = self.parent()

        # 找 Widget
        while parent:
            if hasattr(parent, "page_chat"):
                break
            parent = parent.parent()

        if parent and parent.page_chat:
            chat_page = parent.page_chat

            # 如果当前就在这个聊天
            if chat_page.current_fid:
                chat_page.load_chat(chat_page.current_fid)

    def handle_ai_reply(self, fid, reply):
        conv_id = get_conv_id(self.current_user, fid)

        if not conv_id:
            return

        insert_message(conv_id, "assistant", reply)

        update_conversation_last(
            username=self.current_user,
            friend_id=fid,
            last_message=reply
        )

        # ✅ ⭐关键：通知主界面刷新
        from PySide6.QtCore import QTimer

        QTimer.singleShot(0, self.notify_chat_update)


    def set_user(self, username):
        self.current_user = username

        # Add_Friend 里也要用 username
        self.stack.removeWidget(self.add_friend_page)
        self.add_friend_page.deleteLater()

        self.add_friend_page = Add_Friend(username=username)
        self.stack.insertWidget(1, self.add_friend_page)

        self.add_friend_page.add_request.connect(self.open_confirm_page)
        self.add_friend_page.q_signal.connect(self.back_to_list)

        self.load_data(username)

    def load_data(self, username):
        self.current_user = username

        for i in reversed(range(self.layout.count())):
            item = self.layout.itemAt(i).widget()
            if item:
                item.setParent(None)

        friends = get_friends_list(username)

        g = GroupWidget("朋友")
        for item in friends:
            g.add_item(item["id"], item["name"], item["avatar"], show_add=False)

        self.layout.addWidget(g)

    def open_add_friend(self):
        self.stack.setCurrentWidget(self.add_friend_page)

    def open_confirm_page(self, friend_id, name, avatar):
        self.pending_friend = (friend_id, name, avatar)

        self.friend_page.reset()
        self.friend_page.set_user_info(name, avatar)

        self.stack.setCurrentWidget(self.friend_page)

    def confirm_add(self):
        if not self.current_user or not self.pending_friend:
            return

        fid, name, avatar = self.pending_friend

        input_name = self.friend_page.get_input_name()
        nickname = input_name if input_name else name

        verify_msg = self.friend_page.get_verify_msg()

        success = add_friend(self.current_user, fid, name, nickname, avatar)

        if success:
            add_conversation(self.current_user, fid, name, nickname, avatar)

            conv_id = get_conv_id(self.current_user, fid)

            if verify_msg and conv_id:
                # ✅ 先存用户消息
                insert_message(conv_id, "user", verify_msg)

                update_conversation_last(
                    username=self.current_user,
                    friend_id=fid,
                    last_message=verify_msg
                )

                # ✅ 开线程调用AI（关键🔥）
                thread = threading.Thread(
                    target=self.ask_ai,
                    args=(fid, verify_msg),
                    daemon=True
                )
                thread.start()

            self.friend_page.reset()
            self.add_success.emit()

        self.add_friend_page.update_group_item(fid)
        self.load_data(self.current_user)
        self.stack.setCurrentWidget(self.list_page)

    def ask_ai(self, fid, text):
        from db import get_prompt_by_id

        prompt = get_prompt_by_id(fid)

        try:
            engine = Chat(prompt)
            reply = engine.chat(text)
        except Exception as e:
            reply = f"AI错误: {str(e)}"

        # 回主线程
        self.ai_reply_signal.emit(fid, reply)

    def back_to_list(self):
        if self.current_user:
            self.load_data(self.current_user)
        self.stack.setCurrentWidget(self.list_page)

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