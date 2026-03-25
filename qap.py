from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QTimer, Qt
from PySide6.QtGui import QPixmap, QPainter, QPainterPath
from PySide6.QtWidgets import QGraphicsOpacityEffect, QLabel


class Toast(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)

        self.setStyleSheet("""
            QLabel {
                background-color: rgba(0, 0, 0, 180);
                color: white;
                padding: 10px 20px;
                border-radius: 8px;
                font-size: 14px;
            }
        """)

        self.adjustSize()
        self.move(
            (parent.width() - self.width()) // 2,
            parent.height() // 3
        )

        self.setGraphicsEffect(QGraphicsOpacityEffect(self))
        self.opacity_effect = self.graphicsEffect()

        self.animation = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.animation.setDuration(300)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.setEasingCurve(QEasingCurve.OutCubic)

        self.show()
        self.animation.start()

        # 1.5 秒后开始淡出
        QTimer.singleShot(1500, self.fade_out)

    def fade_out(self):
        self.animation = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.animation.setDuration(500)
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.setEasingCurve(QEasingCurve.OutCubic)
        self.animation.finished.connect(self.close)
        self.animation.start()

def get_round_pixmap(src, size=36):
    if isinstance(src, str):
        src = QPixmap(src)

    if src.isNull():
        return QPixmap()

    src = src.scaled(
        size, size,
        Qt.KeepAspectRatioByExpanding,
        Qt.SmoothTransformation
    )

    result = QPixmap(size, size)
    result.fill(Qt.transparent)

    painter = QPainter(result)
    painter.setRenderHint(QPainter.Antialiasing)

    path_circle = QPainterPath()
    path_circle.addEllipse(0, 0, size, size)

    painter.setClipPath(path_circle)
    painter.drawPixmap(0, 0, src)
    painter.end()

    return result