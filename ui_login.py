# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QToolButton,
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

        self.menuButton = QToolButton(self.AzurChat)
        self.menuButton.setObjectName(u"menuButton")
        self.menuButton.setStyleSheet(u"\n"
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
        icon.addFile(u":/new/prefix1/caidan.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuButton.setIcon(icon)
        self.menuButton.setIconSize(QSize(20, 20))

        self.gridLayout_3.addWidget(self.menuButton, 0, 0, 1, 1)

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


        self.gridLayout_2.addWidget(self.AzurChat, 1, 0, 1, 1)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        font2 = QFont()
        font2.setFamilies([u"PingFang SC"])
        self.widget_3.setFont(font2)
        self.widget_3.setStyleSheet(u"")
        self.gridLayout_4 = QGridLayout(self.widget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(12)
        self.gridLayout_4.setContentsMargins(0, 12, 0, 0)
        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(9)
        sizePolicy1.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy1)
        self.gridLayout_5 = QGridLayout(self.widget_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(-1, -1, -1, 9)
        self.loginButton = QPushButton(self.widget_4)
        self.loginButton.setObjectName(u"loginButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(5)
        sizePolicy2.setHeightForWidth(self.loginButton.sizePolicy().hasHeightForWidth())
        self.loginButton.setSizePolicy(sizePolicy2)
        self.loginButton.setMaximumSize(QSize(300, 50))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.loginButton.setFont(font3)
        self.loginButton.setStyleSheet(u"QPushButton#loginButton {\n"
"    background-color: #8FB9D6;\n"
"    color: white;\n"
"    border-radius: 25px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#loginButton:hover {\n"
"    background-color: #3B82F6;\n"
"}\n"
"\n"
"QPushButton#loginButton:pressed {\n"
"    background-color: #1D4ED8;\n"
"}\n"
"")

        self.gridLayout_5.addWidget(self.loginButton, 0, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(80, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_5, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_3, 1, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(80, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_6, 0, 2, 1, 1)


        self.gridLayout_4.addWidget(self.widget_4, 2, 0, 1, 1)

        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(5)
        sizePolicy3.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy3)

        self.gridLayout_4.addWidget(self.widget_5, 0, 0, 1, 1)

        self.widget_2 = QWidget(self.widget_3)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy3.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy3)
        self.gridLayout_6 = QGridLayout(self.widget_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer, 1, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_3, 4, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_4, 4, 2, 1, 1)

        self.password = QLineEdit(self.widget_2)
        self.password.setObjectName(u"password")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(10)
        sizePolicy4.setHeightForWidth(self.password.sizePolicy().hasHeightForWidth())
        self.password.setSizePolicy(sizePolicy4)
        font4 = QFont()
        font4.setPointSize(10)
        self.password.setFont(font4)
        self.password.setStyleSheet(u"    background-color: white;\n"
"    border-radius: 20px;\n"
"    padding: 10px;\n"
"border: 1px solid #E0E0E0;")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.password.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.password, 4, 1, 1, 1)

        self.user = QLineEdit(self.widget_2)
        self.user.setObjectName(u"user")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(2)
        sizePolicy5.setVerticalStretch(10)
        sizePolicy5.setHeightForWidth(self.user.sizePolicy().hasHeightForWidth())
        self.user.setSizePolicy(sizePolicy5)
        self.user.setFont(font4)
        self.user.setStyleSheet(u"    background-color: white;\n"
"    border-radius: 20px;\n"
"   padding: 10px;\n"
"border: 1px solid #E0E0E0;")
        self.user.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.user, 2, 1, 1, 1)


        self.gridLayout_4.addWidget(self.widget_2, 1, 0, 1, 1)

        self.widget_6 = QWidget(self.widget_3)
        self.widget_6.setObjectName(u"widget_6")
        self.gridLayout_7 = QGridLayout(self.widget_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_8, 0, 3, 1, 1)

        self.reg = QPushButton(self.widget_6)
        self.reg.setObjectName(u"reg")
        self.reg.setStyleSheet(u"QPushButton#reg {\n"
"    background: transparent;\n"
"    border: none;\n"
"    color: #2563EB;\n"
"}\n"
"\n"
"QPushButton#reg:hover {\n"
"    color: #1D4ED8;\n"
"    text-decoration: underline;\n"
"}")

        self.gridLayout_7.addWidget(self.reg, 0, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_7, 0, 0, 1, 1)

        self.que = QPushButton(self.widget_6)
        self.que.setObjectName(u"que")
        self.que.setStyleSheet(u"QPushButton{\n"
"    background: transparent;\n"
"    border: none;\n"
"    color: #2563EB;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #1D4ED8;\n"
"    text-decoration: underline;\n"
"}")

        self.gridLayout_7.addWidget(self.que, 0, 2, 1, 1)


        self.gridLayout_4.addWidget(self.widget_6, 3, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_3, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.menuButton.setText("")
        self.label.setText(QCoreApplication.translate("Widget", u"AzurChat", None))
        self.loginButton.setText(QCoreApplication.translate("Widget", u"\u767b\u5f55", None))
        self.password.setText("")
        self.reg.setText(QCoreApplication.translate("Widget", u"\u6307\u6325\u5b98\u6ce8\u518c", None))
        self.que.setText(QCoreApplication.translate("Widget", u"\u95ee\u9898\u53cd\u9988", None))
    # retranslateUi

