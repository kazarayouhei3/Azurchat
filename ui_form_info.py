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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QSpacerItem, QToolButton, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(480, 680)
        self.gridLayout = QGridLayout(Widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, -1)
        self.widget = QWidget(Widget)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(self.widget)
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
        self.AzurChat.setStyleSheet(u"background-color:  #ededed;")
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

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.toolButton = QToolButton(self.AzurChat)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setStyleSheet(u"QToolButton {\n"
"    border: none;\n"
"    background: transparent;\n"
"}")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.FormatJustifyFill))
        self.toolButton.setIcon(icon)

        self.gridLayout_3.addWidget(self.toolButton, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.AzurChat, 1, 0, 1, 1)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        font2 = QFont()
        font2.setFamilies([u"PingFang SC"])
        self.widget_3.setFont(font2)

        self.gridLayout_2.addWidget(self.widget_3, 3, 0, 1, 1)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 10))
        self.widget_2.setMaximumSize(QSize(16777215, 80))

        self.gridLayout_2.addWidget(self.widget_2, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Info", None))
        self.toolButton.setText("")
    # retranslateUi

