from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QHBoxLayout,
    QPushButton, QScrollArea
)
from PySide6.QtCore import Qt, Signal, QPoint
from PySide6.QtGui import QPixmap, QPainter, QColor, QPolygon

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QHBoxLayout,
    QPushButton, QScrollArea
)
from PySide6.QtCore import Qt, Signal, QPoint
from PySide6.QtGui import QPixmap, QPainter, QColor, QPolygon


class Suggest(QWidget):
    selected = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        # ===== 核心：稳定弹窗 =====
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFocusPolicy(Qt.NoFocus)
        self.setAttribute(Qt.WA_ShowWithoutActivating)

        self.max_items = 5
        self.item_height = 50

        # ===== 主布局 =====
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 12, 0, 0)  # 给三角留空间

        # ===== 卡片 =====
        self.card = QWidget()
        self.card.setStyleSheet("""
            QWidget {
                background: white;
                border-radius: 10px;
            }
        """)
        self.main_layout.addWidget(self.card)

        # ===== scroll =====
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setFrameShape(QScrollArea.NoFrame)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.inner = QWidget()
        self.layout = QVBoxLayout(self.inner)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(2)

        self.scroll.setWidget(self.inner)

        card_layout = QVBoxLayout(self.card)
        card_layout.setContentsMargins(0, 0, 0, 0)
        card_layout.addWidget(self.scroll)

        self.items = []

    # ===== 数据 =====
    def set_data(self, data):
        # 清空
        for i in self.items:
            i.deleteLater()
        self.items.clear()

        # 添加
        for item in data:
            w = self.create_item(item)
            self.layout.addWidget(w)
            self.items.append(w)

        # ⭐ 核心：固定高度（别用adjustSize）
        count = min(len(data), self.max_items)
        total_height = count * self.item_height

        self.scroll.setFixedHeight(total_height)
        self.setFixedHeight(total_height + 12)  # +三角

    # ===== 单项 =====
    def create_item(self, item):
        w = QWidget()
        w.setFixedHeight(self.item_height)
        w.setStyleSheet("""
            QWidget:hover {
                background:#F5F7FA;
                border-radius:6px;
            }
        """)

        h = QHBoxLayout(w)
        h.setContentsMargins(10, 6, 10, 6)

        avatar = QLabel()
        avatar.setFixedSize(32, 32)

        pix = QPixmap(item["avatar"])
        if not pix.isNull():
            avatar.setPixmap(pix.scaled(32, 32, Qt.KeepAspectRatioByExpanding))

        h.addWidget(avatar)

        name = QLabel(item["name"])
        name.setStyleSheet("font-size:14px;")
        h.addWidget(name)

        h.addStretch()

        btn = QPushButton("添加")
        btn.setFixedSize(60, 26)

        if item.get("added"):
            btn.setText("已添加")
            btn.setEnabled(False)
            btn.setStyleSheet("""
                QPushButton {
                    background:#E4E7ED;
                    color:#909399;
                    border:none;
                    border-radius:13px;
                }
            """)
        else:
            btn.setStyleSheet("""
                QPushButton {
                    background:#409EFF;
                    color:white;
                    border:none;
                    border-radius:13px;
                }
                QPushButton:hover {
                    background:#66b1ff;
                }
            """)

        btn.clicked.connect(lambda _, fid=item["id"]: self.select(fid))
        h.addWidget(btn)

        w.mousePressEvent = lambda e, fid=item["id"]: self.select(fid)

        return w

    def select(self, fid):
        self.selected.emit(fid)
        self.hide()

    # ===== 三角 =====
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.setBrush(QColor(255, 255, 255))
        painter.setPen(Qt.NoPen)

        triangle = QPolygon([
            QPoint(30, 0),
            QPoint(40, 12),
            QPoint(20, 12),
        ])

        painter.drawPolygon(triangle)