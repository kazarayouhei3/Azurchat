# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QToolButton, QWidget)
import rc_pic

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(380, 680)
        Widget.setStyleSheet(u"QWidget{\n"
"    background: transparent;\n"
"}")
        self.gridLayout = QGridLayout(Widget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Widget)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet(u"background:#EBF3FF;")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.AzurChat = QWidget(self.widget)
        self.AzurChat.setObjectName(u"AzurChat")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.AzurChat.sizePolicy().hasHeightForWidth())
        self.AzurChat.setSizePolicy(sizePolicy1)
        self.AzurChat.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamilies([u"PingFang SC"])
        font.setBold(True)
        font.setItalic(False)
        font.setStyleStrategy(QFont.PreferDefault)
        self.AzurChat.setFont(font)
        self.AzurChat.setAutoFillBackground(False)
        self.AzurChat.setStyleSheet(u"background-color: #FFFFFF;\n"
"border-bottom-left-radius: 20px;\n"
"border-bottom-right-radius: 20px;\n"
"")
        self.gridLayout_3 = QGridLayout(self.AzurChat)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(10, 0, 10, 0)
        self.quit_button = QToolButton(self.AzurChat)
        self.quit_button.setObjectName(u"quit_button")
        self.quit_button.setStyleSheet(u"\n"
"        QToolButton {\n"
"            border: none;\n"
"            padding: 2px;\n"
"        }\n"
"\n"
"        QToolButton:hover {\n"
"            background-color: #e6e6e6;\n"
"            border-radius: 4px;\n"
"        }\n"
"\n"
"        QToolButton:pressed {\n"
"            background-color: #d0d0d0;\n"
"        }\n"
"\n"
"        /* \u5173\u952e\uff1a\u5e72\u6389\u4e0b\u62c9\u7bad\u5934 */\n"
"        QToolButton::menu-indicator {\n"
"            image: none;\n"
"        }\n"
"        ")
        icon = QIcon()
        icon.addFile(u":/icon/quit.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.quit_button.setIcon(icon)
        self.quit_button.setIconSize(QSize(20, 20))

        self.gridLayout_3.addWidget(self.quit_button, 0, 4, 1, 1)

        self.label = QLabel(self.AzurChat)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(15)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.label.setFont(font1)

        self.gridLayout_3.addWidget(self.label, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)

        self.toolButton = QToolButton(self.AzurChat)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setMinimumSize(QSize(30, 30))
        self.toolButton.setMaximumSize(QSize(30, 30))
        self.toolButton.setStyleSheet(u"\n"
"        QToolButton {\n"
"            border: none;\n"
"            padding: 2px;\n"
"        }\n"
"\n"
"        /* \u5173\u952e\uff1a\u5e72\u6389\u4e0b\u62c9\u7bad\u5934 */\n"
"        QToolButton::menu-indicator {\n"
"            image: none;\n"
"        }")
        icon1 = QIcon()
        icon1.addFile(u":/icon/head.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton.setIcon(icon1)
        self.toolButton.setIconSize(QSize(15, 15))

        self.gridLayout_3.addWidget(self.toolButton, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.AzurChat, 1, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(12)
        sizePolicy2.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy2)
        self.stackedWidget.setStyleSheet(u"")
        self.mainPage = QWidget()
        self.mainPage.setObjectName(u"mainPage")
        self.gridLayout_6 = QGridLayout(self.mainPage)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.list = QListWidget(self.mainPage)
        self.list.setObjectName(u"list")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(10)
        sizePolicy3.setHeightForWidth(self.list.sizePolicy().hasHeightForWidth())
        self.list.setSizePolicy(sizePolicy3)
        self.list.setStyleSheet(u"QListWidget {\n"
"    border: none;          /* \u53bb\u5916\u6846 */\n"
"    outline: none;         /* \u53bb\u7126\u70b9\u6846\uff08\u5f88\u5173\u952e\uff09 */\n"
"    background: transparent;     /* \u7edf\u4e00\u80cc\u666f */\n"
"}")

        self.gridLayout_6.addWidget(self.list, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.mainPage)
        self.contact = QWidget()
        self.contact.setObjectName(u"contact")
        self.gridLayout_9 = QGridLayout(self.contact)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.contact)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_10 = QGridLayout(self.widget_5)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.widget_5)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy4)
        self.gridLayout_11 = QGridLayout(self.widget_6)
        self.gridLayout_11.setSpacing(4)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(6, 6, 6, 6)
        self.contactButton = QPushButton(self.widget_6)
        self.contactButton.setObjectName(u"contactButton")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(1)
        sizePolicy5.setHeightForWidth(self.contactButton.sizePolicy().hasHeightForWidth())
        self.contactButton.setSizePolicy(sizePolicy5)
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei"])
        font2.setPointSize(15)
        font2.setBold(False)
        self.contactButton.setFont(font2)
        self.contactButton.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 10px 10px 10px 15px;\n"
"    text-align: left;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #e6e6e6;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #d0d0d0;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icon/friend.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.contactButton.setIcon(icon2)

        self.gridLayout_11.addWidget(self.contactButton, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.widget_6, 0, 0, 1, 1)

        self.contactList = QWidget(self.widget_5)
        self.contactList.setObjectName(u"contactList")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(10)
        sizePolicy6.setHeightForWidth(self.contactList.sizePolicy().hasHeightForWidth())
        self.contactList.setSizePolicy(sizePolicy6)

        self.gridLayout_10.addWidget(self.contactList, 1, 0, 1, 1)


        self.gridLayout_9.addWidget(self.widget_5, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.contact)
        self.setting = QWidget()
        self.setting.setObjectName(u"setting")
        self.gridLayout_7 = QGridLayout(self.setting)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.setting)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_8 = QGridLayout(self.widget_4)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.azurButton = QPushButton(self.widget_4)
        self.azurButton.setObjectName(u"azurButton")
        font3 = QFont()
        font3.setPointSize(14)
        self.azurButton.setFont(font3)
        self.azurButton.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    padding-left: 15px;   /* \u63a7\u5236\u6574\u4f53\u5f80\u5de6\u8d34 */\n"
"    text-align: left;     /* \u6587\u5b57\u5de6\u5bf9\u9f50 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #e6e6e6;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #d0d0d0;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icon/area.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.azurButton.setIcon(icon3)

        self.gridLayout_8.addWidget(self.azurButton, 1, 0, 1, 1)

        self.settingButton = QPushButton(self.widget_4)
        self.settingButton.setObjectName(u"settingButton")
        font4 = QFont()
        font4.setFamilies([u"Microsoft YaHei UI"])
        font4.setPointSize(14)
        font4.setBold(False)
        self.settingButton.setFont(font4)
        self.settingButton.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    padding-left: 15px;   /* \u63a7\u5236\u6574\u4f53\u5f80\u5de6\u8d34 */\n"
"    text-align: left;     /* \u6587\u5b57\u5de6\u5bf9\u9f50 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #e6e6e6;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #d0d0d0;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/new/prefix1/set.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingButton.setIcon(icon4)

        self.gridLayout_8.addWidget(self.settingButton, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.widget_4, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.setting)

        self.gridLayout_2.addWidget(self.stackedWidget, 2, 0, 1, 1)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy1.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy1)
        font5 = QFont()
        font5.setFamilies([u"PingFang SC"])
        self.widget_3.setFont(font5)
        self.widget_3.setStyleSheet(u"background:white;")
        self.gridLayout_4 = QGridLayout(self.widget_3)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget_3)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(2)
        sizePolicy7.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy7)
        self.widget_2.setStyleSheet(u"    background-color: #D7DDEA;")
        self.gridLayout_5 = QGridLayout(self.widget_2)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.chat = QToolButton(self.widget_2)
        self.chat.setObjectName(u"chat")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy8.setHorizontalStretch(1)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.chat.sizePolicy().hasHeightForWidth())
        self.chat.setSizePolicy(sizePolicy8)
        self.chat.setStyleSheet(u"QToolButton {\n"
"    border: none;\n"
"    color: #666;\n"
"    padding: 6px 10px;\n"
"    border-bottom-left-radius: 20px;\n"
"    border-bottom-right-radius: 20px;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    color: #1677FF;\n"
"}\n"
"\n"
"/* \u2b50 \u63d0\u9ad8\u4f18\u5148\u7ea7 */\n"
"QToolButton:checked {\n"
"    background-color: #EBF3FF;\n"
"    color: #1677FF;\n"
"}")
        self.chat.setIconSize(QSize(20, 20))
        self.chat.setCheckable(True)
        self.chat.setChecked(False)
        self.chat.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.chat.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)

        self.gridLayout_5.addWidget(self.chat, 1, 0, 1, 1)

        self.phone = QToolButton(self.widget_2)
        self.phone.setObjectName(u"phone")
        sizePolicy8.setHeightForWidth(self.phone.sizePolicy().hasHeightForWidth())
        self.phone.setSizePolicy(sizePolicy8)
        self.phone.setStyleSheet(u"QToolButton {\n"
"    border: none;\n"
"    color: #666;\n"
"    padding: 5px;\n"
"    qproperty-iconSize: 20px 20px;\n"
"}\n"
"\n"
"/* \u274c hover \u4e0d\u518d\u6539\u80cc\u666f */\n"
"QToolButton:hover {\n"
"    color: #1677FF;   /* \u2b50\u53ea\u6539\u6587\u5b57\u989c\u8272 */\n"
"}\n"
"\n"
"/* \u2705 \u9009\u4e2d\u624d\u6539\u80cc\u666f */\n"
"QToolButton:checked {\n"
"    background-color: #EBF3FF;\n"
"    color: #1677FF;\n"
"    border-bottom-left-radius: 20px;\n"
"    border-bottom-right-radius: 20px;\n"
"}")
        self.phone.setCheckable(True)
        self.phone.setChecked(False)

        self.gridLayout_5.addWidget(self.phone, 1, 2, 1, 1)

        self.my = QToolButton(self.widget_2)
        self.my.setObjectName(u"my")
        sizePolicy8.setHeightForWidth(self.my.sizePolicy().hasHeightForWidth())
        self.my.setSizePolicy(sizePolicy8)
        self.my.setStyleSheet(u"QToolButton {\n"
"    border: none;\n"
"\n"
"    color: #666;\n"
"    padding: 5px;\n"
"    qproperty-iconSize: 20px 20px;\n"
"    border-bottom-right-radius: 20px;\n"
"}\n"
"\n"
"/* \u274c hover \u4e0d\u518d\u6539\u80cc\u666f */\n"
"QToolButton:hover {\n"
"    color: #1677FF;   /* \u2b50\u53ea\u6539\u6587\u5b57\u989c\u8272 */\n"
"}\n"
"\n"
"/* \u2705 \u9009\u4e2d\u624d\u6539\u80cc\u666f */\n"
"QToolButton:checked {\n"
"    background-color: #EBF3FF;\n"
"    color: #1677FF;\n"
"    border-bottom-left-radius: 20px;\n"
"    border-bottom-right-radius: 20px;\n"
"}")
        self.my.setCheckable(True)
        self.my.setChecked(True)

        self.gridLayout_5.addWidget(self.my, 1, 3, 1, 1)

        self.widget_7 = QWidget(self.widget_2)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy9.setHorizontalStretch(1)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy9)
        self.gridLayout_12 = QGridLayout(self.widget_7)
        self.gridLayout_12.setSpacing(5)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(5, 5, 5, 5)
        self.chatButton = QToolButton(self.widget_7)
        self.chatButton.setObjectName(u"chatButton")
        sizePolicy8.setHeightForWidth(self.chatButton.sizePolicy().hasHeightForWidth())
        self.chatButton.setSizePolicy(sizePolicy8)
        self.chatButton.setMaximumSize(QSize(16777215, 16777215))
        self.chatButton.setStyleSheet(u"QToolButton {\n"
"    border: none;\n"
"    color: #666;\n"
"    padding: 6px 12px;\n"
"    border-radius: 12px;   /* \u2b50 \u5fc5\u987b\u6709 */\n"
"    qproperty-iconSize: 20px 20px;\n"
"}\n"
"QToolButton::hover {\n"
"    color: #1677FF;\n"
"}\n"
"\n"
"/* \u2b50 hover \u51fa\u73b0\u201c\u6d45\u84dd\u5757\u201d */\n"
"QToolButton:hover:!checked {\n"
"    color: #1677FF;\n"
"    background-color: #C9D1E3;   /* \u2b50 \u5173\u952e */\n"
"}")
        self.chatButton.setCheckable(False)
        self.chatButton.setChecked(False)
        self.chatButton.setAutoRepeat(False)
        self.chatButton.setAutoExclusive(False)

        self.gridLayout_12.addWidget(self.chatButton, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.widget_7, 1, 1, 1, 1)


        self.gridLayout_4.addWidget(self.widget_2, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_3, 3, 0, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(Widget)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.quit_button.setText("")
        self.label.setText(QCoreApplication.translate("Widget", u"AzurChat", None))
        self.toolButton.setText("")
        self.contactButton.setText(QCoreApplication.translate("Widget", u"\u52a0\u597d\u53cb", None))
        self.azurButton.setText(QCoreApplication.translate("Widget", u"\u6211\u7684\u6e2f\u533a", None))
        self.settingButton.setText(QCoreApplication.translate("Widget", u"\u8bbe\u7f6e", None))
        self.chat.setText("")
        self.phone.setText("")
        self.my.setText("")
        self.chatButton.setText("")
    # retranslateUi

