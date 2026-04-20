import sys
from PySide6.QtWidgets import QApplication, QSplashScreen
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import Qt, QTimer

from login import Login
from widget import Widget
from db import init_db, load_all_friends_from_json

def start_login():
    login = Login()

    def on_login_success(username):
        login.main = Widget()   # ⭐挂在 login 上

        login.main.setGeometry(login.geometry())
        login.main.after_login(username)
        login.main.show()

        login.close()

    login.signal.connect(on_login_success)
    login.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon(":/new/prefix1/azur.ico"))

    # ===== 初始化 =====
    init_db()
    load_all_friends_from_json()

    # ===== 启动图 =====
    splash_pix = QPixmap("logo.png")
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.show()
    app.processEvents()

    QTimer.singleShot(1500, splash.close)
    QTimer.singleShot(1500, start_login)

    sys.exit(app.exec())