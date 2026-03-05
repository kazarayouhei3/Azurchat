# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_chat.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QToolButton, QWidget)
import rc_pic

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(380, 680)
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
        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.mainButton = QToolButton(self.AzurChat)
        self.mainButton.setObjectName(u"mainButton")
        self.mainButton.setEnabled(True)
        self.mainButton.setStyleSheet(u"\n"
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
"")
        icon = QIcon()
        icon.addFile(u":/new/prefix1/go.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.mainButton.setIcon(icon)

        self.gridLayout_3.addWidget(self.mainButton, 0, 0, 1, 1)

        self.label = QLabel(self.AzurChat)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"PingFang SC"])
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.label.setFont(font1)

        self.gridLayout_3.addWidget(self.label, 0, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)

        self.menu = QToolButton(self.AzurChat)
        self.menu.setObjectName(u"menu")
        self.menu.setStyleSheet(u"\n"
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
        icon1 = QIcon()
        icon1.addFile(u":/new/prefix1/caidan.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menu.setIcon(icon1)

        self.gridLayout_3.addWidget(self.menu, 0, 4, 1, 1)


        self.gridLayout_2.addWidget(self.AzurChat, 1, 0, 1, 1)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        font2 = QFont()
        font2.setFamilies([u"PingFang SC"])
        self.widget_3.setFont(font2)
        self.widget_3.setStyleSheet(u"")
        self.gridLayout_4 = QGridLayout(self.widget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.listWidget = QListWidget(self.widget_3)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setStyleSheet(u" border: 0px;")

        self.gridLayout_4.addWidget(self.listWidget, 0, 0, 1, 1)

        self.widget_2 = QWidget(self.widget_3)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 50))
        self.widget_2.setMaximumSize(QSize(16777215, 50))
        self.widget_2.setStyleSheet(u"background-color: white;")
        self.gridLayout_5 = QGridLayout(self.widget_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.lineEdit = QLineEdit(self.widget_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"    background-color: white;\n"
"    border-radius: 12px;\n"
"    padding: 8px;\n"
"border: 1px solid #E0E0E0;")

        self.gridLayout_5.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.widget_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(30, 30))
        self.pushButton.setStyleSheet(u"border: 0px;")
        icon2 = QIcon()
        icon2.addFile(u":/new/prefix1/send.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon2)

        self.gridLayout_5.addWidget(self.pushButton, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.widget_2, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_3, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.mainButton.setText("")
        self.label.setText(QCoreApplication.translate("Widget", u"\u5e0c\u4f69\u5c14", None))
        self.menu.setText("")
        self.pushButton.setText("")
    # retranslateUi

