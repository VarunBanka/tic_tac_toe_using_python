from PyQt5.QtWidgets import QMessageBox, QLabel, QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QRect
import sys
from modes.online_mp import Online_MP
from modes.singleplayer import Singleplayer
from modes.local_mp import Local_MP


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 600, 400)
        self.setFixedSize(self.size())
        self.setWindowTitle("TicTacToe - Menu")
        self.UIComponents()

        self.show()

    def UIComponents(self):
        self.title = QLabel(self)
        self.title.setText("TicTacToe")
        self.title.setFont(QFont("Arial", 18))
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setGeometry(QRect(0, 0, 600, 50))

        self.undertitle = QLabel(self)
        self.undertitle.setText("Select a mode")
        self.undertitle.setFont(QFont("Arial", 12))
        self.undertitle.setAlignment(Qt.AlignCenter)
        self.undertitle.setGeometry(QRect(0, 50, 600, 50))

        self.sp_btn = QPushButton(self)
        self.sp_btn.setText("Single Player")
        self.sp_btn.setGeometry(QRect(200, 100, 200, 50))
        self.sp_btn.clicked.connect(self.singlePlayer)

        self.mp_btn = QPushButton(self)
        self.mp_btn.setText("Local Multiplayer")
        self.mp_btn.setGeometry(QRect(200, 175, 200, 50))
        self.mp_btn.clicked.connect(self.local_mp)

        self.mp2_btn = QPushButton(self)
        self.mp2_btn.setText("Online Multiplayer")
        self.mp2_btn.setGeometry(QRect(200, 250, 200, 50))
        self.mp2_btn.clicked.connect(self.online_mp)

        self.exit_btn = QPushButton(self)
        self.exit_btn.setText("Exit")
        self.exit_btn.setGeometry(QRect(200, 325, 200, 50))
        self.exit_btn.clicked.connect(self.exit)

    def singlePlayer(self):
        self.hide()
        self.win = Singleplayer()
        self.win.show()

    def local_mp(self):
        self.hide()
        self.win = Local_MP()
        self.win.show()

    def online_mp(self):
        self.hide()
        self.win = Online_MP()
        self.win.show()

    def exit(self):
        self.close()


if "__main__" == __name__:
    app = QApplication(sys.argv)

    try:
        with open(f"./assets/stylesheet", "r") as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        QMessageBox.warning(None, "Error", "Could not load stylesheet")
        app.exit()

    menu = Menu()
    sys.exit(app.exec_())
