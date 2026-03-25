import os
from PySide6.QtWidgets import QWidget, QPushButton, QToolButton
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Signal, QEvent, QSize, Qt
from PySide6.QtGui import QIcon

from qap import Toast


class ChatCommand(QWidget):
    chat_signal = Signal()
    phone_signal = Signal()
    set_signal = Signal()
    def __init__(self, parent=None):
        super().__init__(parent)

        loader = QUiLoader()

        base_dir = os.path.dirname(__file__)
        ui_path = os.path.join(base_dir, "form_info.ui")

        file = QFile(ui_path)
        file.open(QFile.ReadOnly)

        self.root = loader.load(file)
        file.close()

        self.root.setParent(self)

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
            False
        )

        self.init_nav_button(
            self.my,
            ":/icon/my.svg",
            ":/icon/my_select.svg",
            "我的",
            True
        )

        self.chat.clicked.connect(self.chat_signal.emit)
        self.phone.clicked.connect(self.phone_signal.emit)
        self.push_button = self.root.findChild(QPushButton, "pushButton")
        self.push_button.clicked.connect(self.on_clicked)

    def on_clicked(self):
        Toast("等等吧", self)
        self.set_signal.emit()

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

