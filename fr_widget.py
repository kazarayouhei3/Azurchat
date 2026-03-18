from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PySide6.QtCore import Signal, QPropertyAnimation, QEasingCurve, Property
from PySide6.QtGui import QPixmap, QPainter, QTransform
from PySide6.QtSvg import QSvgRenderer

class ArrowLabel(QLabel):
    def __init__(self):
        super().__init__()
        self._angle = 0
        self.renderer = QSvgRenderer("icon/click.svg")  # 👉 SVG路径
        self.setFixedSize(16, 16)

    def set_angle(self, angle):
        self._angle = angle
        self.update()

    def get_angle(self):
        return self._angle

    angle = Property(float, get_angle, set_angle)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        transform = QTransform()
        transform.translate(self.width()/2, self.height()/2)
        transform.rotate(self._angle)
        transform.translate(-self.width()/2, -self.height()/2)

        painter.setTransform(transform)

        self.renderer.render(painter)

class GroupWidget(QWidget):
    item_signal = Signal(str)

    def __init__(self, title="分组"):
        super().__init__()

        self.is_expanded = False

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        self.base_title = title
        self.count = 0

        # ===== 头部 =====
        self.header = QWidget()
        self.header.setFixedHeight(40)
        self.header.setStyleSheet("""
            QWidget:hover {
                background:#F5F5F5;
            }
        """)

        header_layout = QHBoxLayout(self.header)
        header_layout.setContentsMargins(10, 0, 10, 0)  # 👉 右边留点空间

        # ===== 箭头 =====
        self.arrow = ArrowLabel()
        self.arrow.setFixedSize(16, 16)

        # ===== 标题（左）=====
        self.title = QLabel(title)
        self.title.setStyleSheet("""
            font-weight: 500;
            font-size: 14px;
        """)

        # ===== 🔥 数量（右）=====
        self.count_label = QLabel("0")
        self.count_label.setStyleSheet("""
            color: #999;
            font-size: 12px;
        """)

        # ===== 布局 =====
        header_layout.addWidget(self.arrow)
        header_layout.addWidget(self.title)
        header_layout.addStretch()
        header_layout.addWidget(self.count_label)  # 👈 放最右

        self.main_layout.addWidget(self.header)

        # 点击
        self.header.mousePressEvent = lambda e: self.toggle()

        # ===== 内容区域 =====
        self.content = QWidget()
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(30, 0, 0, 0)
        self.content_layout.setSpacing(0)

        self.content.setMaximumHeight(0)
        self.main_layout.addWidget(self.content)

        # ===== 展开动画 =====
        self.anim = QPropertyAnimation(self.content, b"maximumHeight")
        self.anim.setDuration(200)
        self.anim.setEasingCurve(QEasingCurve.OutCubic)

        # ===== 箭头动画 =====
        self.arrow_anim = QPropertyAnimation(self.arrow, b"angle")
        self.arrow_anim.setDuration(200)
        self.arrow_anim.setEasingCurve(QEasingCurve.OutCubic)

        self.update_title()

    # ===== 添加好友 =====
    def add_item(self, name):
        label = QLabel(name)
        label.setFixedHeight(36)
        label.setStyleSheet("""
            QLabel {
                padding-left:10px;
            }
            QLabel:hover {
                background:#EAEAEA;
                border-radius:6px;
            }
        """)

        label.mousePressEvent = lambda e, n=name: self.item_signal.emit(n)

        self.content_layout.addWidget(label)

        # 更新数量
        self.count += 1
        self.update_title()

    # ===== 🔥 更新标题（只更新右边）=====
    def update_title(self):
        self.count_label.setText(str(self.count))

    # ===== 展开/收起 =====
    def toggle(self):
        self.is_expanded = not self.is_expanded

        h = self.content.sizeHint().height()

        if self.is_expanded:
            self.anim.setStartValue(0)
            self.anim.setEndValue(h)

            self.arrow_anim.setStartValue(0)
            self.arrow_anim.setEndValue(90)
        else:
            self.anim.setStartValue(h)
            self.anim.setEndValue(0)

            self.arrow_anim.setStartValue(90)
            self.arrow_anim.setEndValue(0)

        self.anim.start()
        self.arrow_anim.start()