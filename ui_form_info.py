# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_info.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QPushButton, QSizePolicy,
    QToolButton, QWidget)
import rc_pic

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(380, 680)
        self.gridLayout = QGridLayout(Widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Widget)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet(u"background-color: #EEF2F6;")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        font = QFont()
        font.setFamilies([u"PingFang SC"])
        self.widget_3.setFont(font)
        self.gridLayout_3 = QGridLayout(self.widget_3)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(10)
        sizePolicy1.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy1)
        self.gridLayout_4 = QGridLayout(self.widget_4)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 10, 0, 0)
        self.pushButton = QPushButton(self.widget_4)
        self.pushButton.setObjectName(u"pushButton")
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(14)
        font1.setBold(False)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
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
        icon = QIcon()
        icon.addFile(u":/new/prefix1/set.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)

        self.gridLayout_4.addWidget(self.pushButton, 2, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget_4, 1, 0, 1, 1)

        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy2)
        self.gridLayout_5 = QGridLayout(self.widget_5)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.chat = QToolButton(self.widget_5)
        self.chat.setObjectName(u"chat")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.chat.sizePolicy().hasHeightForWidth())
        self.chat.setSizePolicy(sizePolicy3)
        self.chat.setStyleSheet(u"QToolButton {\n"
"            border: none;\n"
"\n"
"            color: #666;\n"
"            border-top: 2px solid #E5E7EB;\n"
"            background-color: #DCE3EA;\n"
"        }\n"
"")

        self.gridLayout_5.addWidget(self.chat, 0, 0, 1, 1)

        self.phone = QToolButton(self.widget_5)
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
"\n"
"")

        self.gridLayout_5.addWidget(self.phone, 0, 1, 1, 1)

        self.my = QToolButton(self.widget_5)
        self.my.setObjectName(u"my")
        sizePolicy3.setHeightForWidth(self.my.sizePolicy().hasHeightForWidth())
        self.my.setSizePolicy(sizePolicy3)
        self.my.setStyleSheet(u"QToolButton {\n"
"            border: none;\n"
"            background: transparent;\n"
"            color: #666;\n"
"        }\n"
"")

        self.gridLayout_5.addWidget(self.my, 0, 2, 1, 1)


        self.gridLayout_3.addWidget(self.widget_5, 2, 0, 1, 1)

        self.widget_2 = QWidget(self.widget_3)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy2.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.widget_2, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_3, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"\u8bbe\u7f6e", None))
        self.chat.setText("")
        self.phone.setText("")
        self.my.setText("")
    # retranslateUi

