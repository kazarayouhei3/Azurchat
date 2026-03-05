# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_chara.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QToolButton, QWidget)
import rc_pic

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(380, 680)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(Widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Widget)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.widget.setStyleSheet(u"background-color: #EEF2F6;")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.AzurChat = QWidget(self.widget)
        self.AzurChat.setObjectName(u"AzurChat")
        sizePolicy.setHeightForWidth(self.AzurChat.sizePolicy().hasHeightForWidth())
        self.AzurChat.setSizePolicy(sizePolicy)
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

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)

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
        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy2)
        self.gridLayout_6 = QGridLayout(self.widget_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.chara = QWidget(self.widget_4)
        self.chara.setObjectName(u"chara")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.chara.sizePolicy().hasHeightForWidth())
        self.chara.setSizePolicy(sizePolicy3)
        self.gridLayout_8 = QGridLayout(self.chara)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_3 = QLabel(self.chara)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_8.addWidget(self.label_3, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.chara, 0, 0, 1, 1)

        self.widget_6 = QWidget(self.widget_4)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(5)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy4)
        self.gridLayout_7 = QGridLayout(self.widget_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_2 = QLabel(self.widget_6)
        self.label_2.setObjectName(u"label_2")
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(15)
        font3.setBold(True)
        self.label_2.setFont(font3)

        self.gridLayout_7.addWidget(self.label_2, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.widget_6, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.widget_4, 0, 0, 1, 1)

        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(2)
        sizePolicy5.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy5)

        self.gridLayout_4.addWidget(self.widget_5, 2, 0, 1, 1)

        self.widget_2 = QWidget(self.widget_3)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.gridLayout_5 = QGridLayout(self.widget_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(0)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_7 = QWidget(self.widget_2)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy2.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy2)
        self.gridLayout_9 = QGridLayout(self.widget_7)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(0)
        self.gridLayout_9.setContentsMargins(3, 0, 3, 0)
        self.top = QPushButton(self.widget_7)
        self.top.setObjectName(u"top")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(1)
        sizePolicy6.setHeightForWidth(self.top.sizePolicy().hasHeightForWidth())
        self.top.setSizePolicy(sizePolicy6)
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        self.top.setFont(font4)
        self.top.setStyleSheet(u"QPushButton {\n"
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
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icon/top.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.top.setIcon(icon1)

        self.gridLayout_9.addWidget(self.top, 1, 0, 1, 1)

        self.mem = QPushButton(self.widget_7)
        self.mem.setObjectName(u"mem")
        sizePolicy6.setHeightForWidth(self.mem.sizePolicy().hasHeightForWidth())
        self.mem.setSizePolicy(sizePolicy6)
        self.mem.setFont(font4)
        self.mem.setStyleSheet(u"QPushButton {\n"
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
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icon/mem.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.mem.setIcon(icon2)

        self.gridLayout_9.addWidget(self.mem, 0, 0, 1, 1)

        self.del = QPushButton(self.widget_7)
        self.del.setObjectName(u"del")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(5)
        sizePolicy7.setHeightForWidth(self.del.sizePolicy().hasHeightForWidth())
        self.del.setSizePolicy(sizePolicy7)
        self.del.setFont(font4)
        self.del.setStyleSheet(u"QPushButton {\n"
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
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icon/del.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.del.setIcon(icon3)

        self.gridLayout_9.addWidget(self.del, 2, 0, 1, 1)


        self.gridLayout_5.addWidget(self.widget_7, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 200, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout_5.addItem(self.verticalSpacer, 2, 0, 1, 1)


        self.gridLayout_4.addWidget(self.widget_2, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_3, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.mainButton.setText("")
        self.label.setText(QCoreApplication.translate("Widget", u"\u597d\u53cb\u4fe1\u606f", None))
        self.label_3.setText("")
        self.label_2.setText(QCoreApplication.translate("Widget", u"\u5e0c\u4f69\u5c14", None))
        self.top.setText(QCoreApplication.translate("Widget", u"\u8bbe\u4e3a\u7f6e\u9876", None))
        self.mem.setText(QCoreApplication.translate("Widget", u"\u56de\u5fc6\u5f80\u6614", None))
        self.del.setText(QCoreApplication.translate("Widget", u"\u5220\u9664\u56de\u5fc6", None))
    # retranslateUi

