from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFrame


class CustomMenu(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # ⭐ 关键：用 Popup，保证行为正常
        self.setWindowFlags(Qt.Popup | Qt.FramelessWindowHint)

        # ===== 布局 =====
        layout = QVBoxLayout(self)
        layout.setContentsMargins(6, 6, 6, 6)
        layout.setSpacing(2)

        self.about_btn = QPushButton("关于")
        self.exit_btn = QPushButton("退出")

        # 分割线
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFixedHeight(1)

        layout.addWidget(self.about_btn)
        layout.addWidget(line)
        layout.addWidget(self.exit_btn)

        # ===== 样式（核心）=====
        self.setStyleSheet("""
        QWidget {
            background-color: #FFFFFF;
            border-radius: 12px;
        }

        QPushButton {
            border: none;
            padding: 8px 16px;
            text-align: center;
            background: transparent;
        }

        QPushButton:hover {
            background-color: #F3F4F6;
        }

        QPushButton:last-child {
            color: #DC2626;
        }

        QFrame {
            background-color: #E5E7EB;
            margin: 2px 8px;
        }
        """)