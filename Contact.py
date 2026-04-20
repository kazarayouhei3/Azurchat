from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QScrollArea, QSizePolicy
from PySide6.QtCore import Signal, Qt

from fr_widget import GroupWidget
from add_friend import Add_Friend
from friend import Friend

from db import (
    get_friends_list,
    addFriend,
    add_conversation,
    get_conv_id,
    insert_message,
    update_conversation_last,
    get_prompt_by_id
)

import threading
from use_api import Chat
from PySide6.QtCore import QTimer

class Contact(QWidget):
    add_success = Signal()
    open_add_page = Signal(object)
    open_confirm_page = Signal(object)
    ai_reply_signal = Signal(str, str)

    def __init__(self, contact_page):
        super().__init__()

        self.page = contact_page
        self.current_user = None
        self.page_add = None
        self.page_confirm = None
        self._current_friend = None

        self.ai_reply_signal.connect(self.handle_ai_reply)

        self._init_ui()

    # ================= UI =================
    def _init_ui(self):
        self.btn_add = self.page.findChild(QPushButton, "contactButton")
        self.btn_add.clicked.connect(self.open_add)

        self.container = self.page.findChild(QWidget, "contactList")

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setFrameShape(QScrollArea.NoFrame)
        self.scroll.setStyleSheet("border:none; background:transparent;")

        layout = self.container.layout()
        if layout is None:
            layout = QVBoxLayout(self.container)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(self.scroll)

        self.inner = QWidget()
        self.layout = QVBoxLayout(self.inner)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.layout.setAlignment(Qt.AlignTop)

        self.scroll.setWidget(self.inner)

    # ================= 用户 =================
    def set_user(self, username):
        self.current_user = username
        self.load_data()

    # ================= 列表 =================
    def load_data(self):
        if not self.current_user:
            return

        while self.layout.count():
            item = self.layout.takeAt(0)
            w = item.widget()
            if w:
                w.deleteLater()

        data = get_friends_list(self.current_user)

        group = GroupWidget("朋友")
        group.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)

        for f in data:
            group.add_item(f["id"], f["name"], f["avatar"], show_add=False)

        self.layout.addWidget(group)
        self.layout.addStretch()

    # ================= 打开 Add =================
    def open_add(self):
        if not self.page_add:
            self.page_add = Add_Friend(self.current_user)
            self.page_add.add_request.connect(self.open_confirm)

        self.open_add_page.emit(self.page_add)

    # ================= 打开确认 =================
    def open_confirm(self, fid, name, avatar):
        self._current_friend = (fid, name, avatar)

        if not self.page_confirm:
            self.page_confirm = Friend()

            self.page_confirm.signal.connect(self.page_confirm.close)
            self.page_confirm.b_signal.connect(self.page_confirm.close)

            if not hasattr(self.page_confirm, "_binded"):
                self.page_confirm.a_signal.connect(self.confirm_add)
                self.page_confirm._binded = True

        self.page_confirm.reset()
        self.page_confirm.set_user_info(name, avatar)

        self.open_confirm_page.emit(self.page_confirm)

    # ================= AI =================
    def ask_ai(self, fid, text):
        try:
            prompt = get_prompt_by_id(fid)
            engine = Chat(prompt)
            reply = engine.chat(text)
        except Exception as e:
            reply = f"AI错误: {str(e)}"

        self.ai_reply_signal.emit(fid, reply)

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

        QTimer.singleShot(0, self.notify_chat_update)

    def notify_chat_update(self):
        parent = self.parent()

        while parent:
            if hasattr(parent, "page_chat"):
                break
            parent = parent.parent()

        if parent and parent.page_chat:
            chat_page = parent.page_chat

            if chat_page.current_fid:
                chat_page.load_chat(chat_page.current_fid)

    # ================= 添加好友（完整复刻 Fr）=================
    def confirm_add(self):
        if not self.current_user or not self._current_friend:
            return

        fid, name, avatar = self._current_friend

        # ⭐ 昵称逻辑（你原来的）
        input_name = self.page_confirm.get_input_name()
        nickname = input_name if input_name else name

        # ⭐ 验证消息（关键！你之前被我改错了）
        verify_msg = self.page_confirm.get_verify_msg()

        success = addFriend(self.current_user, fid, name, nickname, avatar)
        if not success:
            return

        add_conversation(self.current_user, fid, name, nickname, avatar)

        conv_id = get_conv_id(self.current_user, fid)

        if verify_msg and conv_id:
            # ✅ 用户消息
            insert_message(conv_id, "user", verify_msg)

            update_conversation_last(
                username=self.current_user,
                friend_id=fid,
                last_message=verify_msg
            )

            # ✅ ⭐线程调用 AI（你原来的核心）
            thread = threading.Thread(
                target=self.ask_ai,
                args=(fid, verify_msg),
                daemon=True
            )
            thread.start()

        # UI恢复
        self.page_confirm.reset()
        self.page_confirm.close()

        if self.page_add:
            self.page_add.update_group_item(fid)

        self.add_success.emit()
        self.load_data()