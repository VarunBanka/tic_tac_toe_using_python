from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QWidget, QLabel, QMessageBox


class Singleplayer(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setGeometry(300, 300, 380, 500)
        self.setFixedSize(self.size())
        self.setWindowTitle("TicTacToe - Singleplayer")
        self.turn = 0

        self.UIComponents()

        self.show()

    def UIComponents(self):
        pass
