from PyQt5.QtWidgets import QMessageBox, QFrame, QListWidget, QMenu, QLabel, QAction, QSlider, QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QRect
import sys
from modes.singleplayer import Singleplayer
from modes.multiplayer import Multiplayer


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 600, 375)
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
        self.mp_btn.setText("Multiplayer")
        self.mp_btn.setGeometry(QRect(200, 175, 200, 50))
        self.mp_btn.clicked.connect(self.multiPlayer)

        self.exit_btn = QPushButton(self)
        self.exit_btn.setText("Exit")
        self.exit_btn.setGeometry(QRect(200, 250, 200, 50))
        self.exit_btn.clicked.connect(self.exit)

    def listWidgetClicked(self, item):
        if item.text() == "Single Player":
            self.singlePlayer()
        elif item.text() == "Multiplayer":
            self.multiPlayer()
        elif item.text() == "Exit":
            self.exit()

    def singlePlayer(self):
        self.hide()
        self.singlePlayer = Singleplayer()
        self.singlePlayer.show()

    def multiPlayer(self):
        self.hide()
        self.multiPlayer = Multiplayer()
        self.multiPlayer.show()

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
