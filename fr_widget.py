from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Signal, Qt, QPropertyAnimation, QEasingCurve, Property, QRectF
from PySide6.QtGui import QPixmap, QPainter, QTransform, QPainterPath
from PySide6.QtSvg import QSvgRenderer

from qap import get_round_pixmap


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
        self.current_selected = None   # ⭐记录当前选中

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
        header_layout.setContentsMargins(10, 0, 10, 0)

        self.arrow = ArrowLabel()
        self.arrow.setFixedSize(16, 16)

        self.title = QLabel(title)
        self.title.setStyleSheet("font-weight:500; font-size:14px;")

        self.count_label = QLabel("0")
        self.count_label.setStyleSheet("color:#999; font-size:12px;")

        header_layout.addWidget(self.arrow)
        header_layout.addWidget(self.title)
        header_layout.addStretch()
        header_layout.addWidget(self.count_label)

        self.main_layout.addWidget(self.header)

        self.header.mousePressEvent = lambda e: self.toggle()

        # ===== 内容 =====
        self.content = QWidget()
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(30, 0, 0, 0)
        self.content_layout.setSpacing(0)

        self.content.setMaximumHeight(0)
        self.main_layout.addWidget(self.content)

        # 动画
        self.anim = QPropertyAnimation(self.content, b"maximumHeight")
        self.anim.setDuration(200)
        self.anim.setEasingCurve(QEasingCurve.OutCubic)

        self.arrow_anim = QPropertyAnimation(self.arrow, b"angle")
        self.arrow_anim.setDuration(200)
        self.arrow_anim.setEasingCurve(QEasingCurve.OutCubic)

        self.update_title()

    # ================= 添加好友 =================
    def add_item(self, friend_id, name, avatar_path="", desc="", show_add=True):
        item = QWidget()
        item.setObjectName("friendItem")
        item.setProperty("selected", False)

        item.setAttribute(Qt.WA_StyledBackground, True)

        layout = QHBoxLayout(item)
        layout.setContentsMargins(10, 6, 10, 6)
        layout.setSpacing(10)

        # ===== 头像 =====
        avatar = QLabel()
        avatar.setFixedSize(40, 40)

        pix = get_round_pixmap(avatar_path, 40)
        if not pix.isNull():
            avatar.setPixmap(pix)

        avatar.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        layout.addWidget(avatar)

        # ===== 文本 =====
        text_layout = QVBoxLayout()
        text_layout.setSpacing(2)

        # ✅ 名字（不写颜色！！）
        name_label = QLabel(name)
        name_label.setObjectName("nameLabel")
        name_label.setStyleSheet("""
            font-size:14px;
            font-weight:600;
            background: transparent;
        """)
        name_label.setAttribute(Qt.WA_TransparentForMouseEvents, True)

        # ✅ 描述（不写颜色！！）
        desc_label = QLabel(desc)
        desc_label.setObjectName("descLabel")
        desc_label.setStyleSheet("""
            font-size:12px;
            background: transparent;
        """)
        desc_label.setAttribute(Qt.WA_TransparentForMouseEvents, True)

        text_layout.addWidget(name_label)
        text_layout.addWidget(desc_label)

        layout.addLayout(text_layout, 1)

        # ===== 按钮 =====
        btn = QPushButton("添加")
        btn.setFixedHeight(28)
        btn.setMinimumWidth(60)

        btn.setStyleSheet("""
            QPushButton {
                background:#409EFF;
                color:white;
                border:none;
                border-radius:14px;
                padding:0 12px;
            }
            QPushButton:hover {
                background:#66b1ff;
            }
        """)

        btn.clicked.connect(lambda: self.item_signal.emit(friend_id))

        if show_add:
            layout.addWidget(btn)

        # ===== ⭐核心QSS（完全正确版）=====
        item.setStyleSheet("""
        #friendItem {
            background: transparent;
            border-radius:6px;
        }

        #friendItem * {
            background: transparent;
        }

        #friendItem:hover {
            background:#F5F7FA;
        }

        #friendItem[selected="true"] {
            background:#409EFF;
        }

        /* ⭐名字 */
        #nameLabel {
            color: #333;
        }

        /* ⭐描述 */
        #descLabel {
            color: #888;
        }

        /* ⭐选中全部变白 */
        #friendItem[selected="true"] QLabel {
            color: white;
        }

        #friendItem[selected="true"]:hover {
            background:#409EFF;
        }
        """)

        # ===== 点击选中 =====
        def on_click(e, w=item, fid=friend_id):
            if self.current_selected and self.current_selected != w:
                self.current_selected.setProperty("selected", False)
                self.current_selected.style().unpolish(self.current_selected)
                self.current_selected.style().polish(self.current_selected)

            w.setProperty("selected", True)
            w.style().unpolish(w)
            w.style().polish(w)

            self.current_selected = w
            self.item_signal.emit(fid)

        item.mousePressEvent = on_click

        # ===== 存数据 =====
        item.setProperty("friend_id", friend_id)
        item.setProperty("name", name)
        item.setProperty("avatar", avatar_path)

        self.content_layout.addWidget(item)

        self.count += 1
        self.update_title()
    # ================= 标题 =================
    def update_title(self):
        self.count_label.setText(str(self.count))

    # ================= 已添加 =================
    def set_added(self, friend_id):
        for i in range(self.content_layout.count()):
            item = self.content_layout.itemAt(i).widget()
            if not item:
                continue

            if item.property("friend_id") == friend_id:
                btn = item.findChild(QPushButton)
                if btn:
                    btn.setText("已添加")
                    btn.setEnabled(False)

    # ================= 展开 =================
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