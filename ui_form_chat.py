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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QListWidget,
    QListWidgetItem, QSizePolicy, QSpacerItem, QToolButton,
    QWidget)

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
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)

        self.label = QLabel(self.AzurChat)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"PingFang SC"])
        font1.setPointSize(20)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.label.setFont(font1)

        self.gridLayout_3.addWidget(self.label, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.mainButton = QToolButton(self.AzurChat)
        self.mainButton.setObjectName(u"mainButton")
        self.mainButton.setStyleSheet(u"QToolButton {\n"
"    border: none;\n"
"    background: transparent;\n"
"}")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoPrevious))
        self.mainButton.setIcon(icon)

        self.gridLayout_3.addWidget(self.mainButton, 0, 0, 1, 1)


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
        self.list = QListWidget(self.widget_3)
        self.list.setObjectName(u"list")
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

        self.gridLayout_4.addWidget(self.list, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.widget_3, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText(QCoreApplication.translate("Widget", u"\u5e0c\u4f69\u5c14", None))
        self.mainButton.setText("")
    # retranslateUi

