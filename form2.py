from PySide6.QtWidgets import QWidget
from ui_form_info import Ui_Widget   # ← 根据你真实类名改

class InfoWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()   # ← 类名必须一致
        self.ui.setupUi(self)
