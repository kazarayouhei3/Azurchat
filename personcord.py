import os

from PySide6.QtCore import Signal, QFile, Qt, QSize, QEvent
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QWidget, QToolButton, QLabel, QMessageBox, QInputDialog, QLineEdit, QPushButton, \
    QGraphicsBlurEffect

from setting_dialog import Setting


class Personcord(QWidget):
    signal = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        # ===== UI加载 =====
        loader = QUiLoader()
        base_dir = os.path.dirname(__file__)
        ui_path = os.path.join(base_dir, "personRecord.ui")

        file = QFile(ui_path)
        file.open(QFile.ReadOnly)
        self.root = loader.load(file)
        file.close()

        self.root.setParent(self)
        self.root.setFocusPolicy(Qt.StrongFocus)

        # ===== 返回按钮 =====
        self.quit_button = self.root.findChild(QToolButton, "quit_button")
        self.quit_button.clicked.connect(self.signal.emit)

        # ===== 数据显示控件 =====
        self.name = self.root.findChild(QLabel, "name")
        self.avatar = self.root.findChild(QToolButton, "avatar")
        self.line = self.root.findChild(QLabel, "line")
        self.region = self.root.findChild(QLabel, "region")
        self.level = self.root.findChild(QLabel, "level")
        self.birth = self.root.findChild(QLabel, "birthday")

        # ===== 按钮绑定（统一走一个函数）=====
        self.bind_edit("name_widget", "nameLabel")
        self.bind_edit("line_widget", "lineLabel")
        self.bind_edit("region_widget", "regionLabel")
        self.bind_edit("level_widget", "levelLabel")
        self.bind_edit("birthday_widget", "birthLabel")

        # 密码可以单独处理（后面你要做页面）
        self.pwButton = self.root.findChild(QToolButton, "pwButton")
        if self.pwButton:
            self.pwButton.clicked.connect(self.on_edit_password)

    # ========================
    # ⭐ 通用绑定函数
    # ========================
    def bind_edit(self, widget_name, label_name):
        row = self.root.findChild(QWidget, widget_name)
        if not row:
            return

        row.setCursor(Qt.PointingHandCursor)

        # ⭐ 给整行装
        row.installEventFilter(self)
        row._label_name = label_name

        # ⭐ 给子控件也装（关键）
        for child in row.findChildren(QWidget):
            child.installEventFilter(self)
            child._label_name = label_name

    # ========================
    # ⭐ 通用点击逻辑
    # ========================
    def on_edit(self, widget_name, label_name):
        row = self.root.findChild(QWidget, widget_name)
        if not row:
            return

        # ⭐ 标题
        title_label = row.findChild(QLabel, label_name)

        # ⭐ 值（核心：去掉 "Label"）
        value_name = label_name.replace("Label", "")
        value_label = row.findChild(QLabel, value_name)

        if not title_label or not value_label:
            return

        title = title_label.text()  # 昵称
        value = value_label.text()  # 张三

        # ===== 模糊 =====
        self.blur = QGraphicsBlurEffect()
        self.blur.setBlurRadius(15)
        self.root.setGraphicsEffect(self.blur)

        # ===== 遮罩 =====
        self.mask = QWidget(self.root)
        self.mask.setStyleSheet("background: transparent;")
        self.mask.setGeometry(self.root.rect())
        self.mask.show()
        self.mask.raise_()

        # ===== 弹窗 =====
        self.open_setting_page(title, value)
    # ========================
    # ⭐ 密码单独处理（推荐）
    # ========================
    def on_edit_password(self):
        print("进入修改密码页面")


    # ========================
    # ⭐ 数据填充
    # ========================
    def get_user(self, record):
        self.name.setText(record["nickname"])

        pix = QPixmap(record["avatar"])

        pix = pix.scaled(
            20, 20,
            Qt.KeepAspectRatioByExpanding,
            Qt.SmoothTransformation
        )

        self.avatar.setIcon(QIcon(pix))
        self.avatar.setIconSize(QSize(20, 20))

        self.line.setText(record["signature"])
        self.region.setText(record["region"])
        self.level.setText(str(record["level"]))
        self.birth.setText(record["birthday"])

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonPress:
            if hasattr(obj, "_label_name"):

                # ⭐ 找到真正的 row（父控件）
                row = obj
                while row and not hasattr(row, "_label_name"):
                    row = row.parent()

                if row:
                    self.on_edit(row.objectName(), row._label_name)

                return True

        return super().eventFilter(obj, event)

    def open_setting_page(self, title, value):
        self.setting = Setting(parent=self)

        self.setting.setGeometry(0, 0, self.width(), self.height())
        self.setting.raise_()

        self.setting.set_data(title, value)

        # ⭐ 必须接信号！！！
        self.setting.signal.connect(self.close_setting_page)

        self.setting.show()

    def close_setting_page(self):
        self.root.setGraphicsEffect(None)

        if hasattr(self, "mask"):
            self.mask.deleteLater()

        if hasattr(self, "setting"):
            self.setting.close()