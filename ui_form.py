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
    QListWidgetItem, QSizePolicy, QSpacerItem, QToolButton,
    QWidget)
import rc_pic

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(380, 680)
        Widget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(Widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Widget)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet(u"background-color: #EEF2F6;")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.AzurChat = QWidget(self.widget)
        self.AzurChat.setObjectName(u"AzurChat")
        self.AzurChat.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamilies([u"PingFang SC"])
        font.setBold(True)
        font.setItalic(False)
        font.setStyleStrategy(QFont.PreferDefault)
        self.AzurChat.setFont(font)
        self.AzurChat.setAutoFillBackground(False)
        self.AzurChat.setStyleSheet(u"background-color: #F5F9FC;")
        self.gridLayout_3 = QGridLayout(self.AzurChat)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, 12, -1, -1)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.label = QLabel(self.AzurChat)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"PingFang SC"])
        font1.setPointSize(15)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.label.setFont(font1)

        self.gridLayout_3.addWidget(self.label, 0, 2, 1, 1)

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


        self.gridLayout_2.addWidget(self.AzurChat, 1, 0, 1, 1)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        font2 = QFont()
        font2.setFamilies([u"PingFang SC"])
        self.widget_3.setFont(font2)
        self.widget_3.setStyleSheet(u"")
        self.gridLayout_4 = QGridLayout(self.widget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(6)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.list = QListWidget(self.widget_3)
        self.list.setObjectName(u"list")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(10)
        sizePolicy1.setHeightForWidth(self.list.sizePolicy().hasHeightForWidth())
        self.list.setSizePolicy(sizePolicy1)
        self.list.setStyleSheet(u"QListWidget {\n"
"    border: none;\n"
"    outline: none;\n"
"    background-color: #EEF2F6;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background: transparent;\n"
"}")
        self.list.setLineWidth(0)

        self.gridLayout_4.addWidget(self.list, 0, 0, 1, 1)

        self.widget_2 = QWidget(self.widget_3)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy2)
        self.widget_2.setStyleSheet(u"")
        self.gridLayout_5 = QGridLayout(self.widget_2)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.my = QToolButton(self.widget_2)
        self.my.setObjectName(u"my")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.my.sizePolicy().hasHeightForWidth())
        self.my.setSizePolicy(sizePolicy3)
        self.my.setStyleSheet(u"QToolButton {\n"
"            border: none;\n"
"            background: transparent;\n"
"            color: #666;\n"
"            border-top: 2px solid #E5E7EB;\n"
"            background-color: #DCE3EA;\n"
"        }\n"
"")

        self.gridLayout_5.addWidget(self.my, 0, 2, 1, 1)

        self.chat = QToolButton(self.widget_2)
        self.chat.setObjectName(u"chat")
        sizePolicy3.setHeightForWidth(self.chat.sizePolicy().hasHeightForWidth())
        self.chat.setSizePolicy(sizePolicy3)
        self.chat.setStyleSheet(u"QToolButton {\n"
"            border: none;\n"
"            background: transparent;\n"
"            color: #666;\n"
"        }\n"
"")
        self.chat.setIconSize(QSize(30, 30))
        self.chat.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.chat.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)

        self.gridLayout_5.addWidget(self.chat, 0, 0, 1, 1)

        self.phone = QToolButton(self.widget_2)
        self.phone.setObjectName(u"phone")
        sizePolicy3.setHeightForWidth(self.phone.sizePolicy().hasHeightForWidth())
        self.phone.setSizePolicy(sizePolicy3)
        self.phone.setStyleSheet(u"QToolButton {\n"
"            border: none;\n"
"\n"
"            color: #666;\n"
"            border-top: 2px solid #E5E7EB;\n"
"            background-color: #DCE3EA;\n"
"        }\n"
"")

        self.gridLayout_5.addWidget(self.phone, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.widget_2, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_3, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText(QCoreApplication.translate("Widget", u"AzurChat", None))
        self.quit_button.setText("")
        self.my.setText("")
        self.chat.setText("")
        self.phone.setText("")
    # retranslateUi

