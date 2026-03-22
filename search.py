from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QHBoxLayout,
    QPushButton
)
from PySide6.QtCore import Qt, QPoint, Signal
from PySide6.QtGui import QPainter, QPolygon, QColor, QPixmap


class Suggest(QWidget):
    selected = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        # ⭐ 不抢焦点
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setAttribute(Qt.WA_ShowWithoutActivating)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # ===== 外层布局（给三角留空间）=====
        outer = QVBoxLayout(self)
        outer.setContentsMargins(0, 10, 0, 0)

        # ===== 白卡片 =====
        self.content = QWidget()
        self.content.setObjectName("content")
        self.content.setStyleSheet("""
        #content {
            background: white;
            border-radius: 8px;
        }
        """)

        outer.addWidget(self.content)

        # ===== 内容布局 =====
        self.layout = QVBoxLayout(self.content)
        self.layout.setContentsMargins(10, 20, 10, 10)
        self.layout.setSpacing(4)

        self.items = []

    # ===== 数据 =====
    def set_data(self, data):
        # 清空旧
        for i in self.items:
            i.deleteLater()
        self.items.clear()

        for item in data:
            w = QWidget()
            w.setObjectName("item")

            h = QHBoxLayout(w)
            h.setContentsMargins(10, 6, 10, 6)

            # ===== 头像 =====
            avatar = QLabel()
            avatar.setFixedSize(32, 32)

            pix = QPixmap(item["avatar"])
            if not pix.isNull():
                pix = pix.scaled(
                    32, 32,
                    Qt.KeepAspectRatioByExpanding,
                    Qt.SmoothTransformation
                )
                avatar.setPixmap(pix)

            h.addWidget(avatar)

            # ===== 名字 =====
            name = QLabel(item["name"])
            name.setStyleSheet("font-size:14px; font-weight:600;")
            h.addWidget(name)

            h.addStretch()

            # ===== 按钮 =====
            btn = QPushButton()
            btn.setFixedHeight(26)

            # ⭐ 判断是否已添加
            if item.get("added"):
                self.set_added_style(btn)
            else:
                self.set_add_style(btn)

            # ⭐ 点击
            btn.clicked.connect(
                lambda _, b=btn, n=item["name"]: self.on_add(b, n)
            )
            btn.setAttribute(Qt.WA_NoMousePropagation)

            h.addWidget(btn)

            # ===== hover =====
            w.setStyleSheet("""
                #item:hover {
                    background:#F5F7FA;
                    border-radius:6px;
                }
            """)

            # 点击整行
            def make_click(name):
                return lambda e: self.selected.emit(name)

            w.mousePressEvent = make_click(item["name"])

            self.layout.addWidget(w)
            self.items.append(w)

    # ===== 按钮：未添加 =====
    def set_add_style(self, btn):
        btn.setText("添加")
        btn.setEnabled(True)
        btn.setStyleSheet("""
            QPushButton {
                background:#409EFF;
                color:white;
                border:none;
                border-radius:13px;
                padding:0 10px;
            }
            QPushButton:hover {
                background:#66b1ff;
            }
        """)

    # ===== 按钮：已添加 =====
    def set_added_style(self, btn):
        btn.setText("已添加")
        btn.setEnabled(False)
        btn.setStyleSheet("""
            QPushButton {
                background:#E4E7ED;
                color:#909399;
                border:none;
                border-radius:13px;
                padding:0 10px;
            }
        """)

    # ===== 点击添加 =====
    def on_add(self, btn, name):
        # ⭐ UI立即变化
        self.set_added_style(btn)

        # ⭐ 发信号（外部写数据库）
        self.selected.emit(name)

    # ===== 三角 =====
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.setBrush(QColor(255, 255, 255))
        painter.setPen(Qt.NoPen)

        # ⭐ 只画三角（不要再画矩形，避免叠加）
        triangle = QPolygon([
            QPoint(30, 0),
            QPoint(40, 10),
            QPoint(20, 10),
        ])

        painter.drawPolygon(triangle)