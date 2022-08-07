from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QWidget, QLabel, QMessageBox


class Online_MP(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setGeometry(300, 300, 600, 450)
        self.setFixedSize(self.size())
        self.setWindowTitle("TicTacToe - Online Multiplayer")

        self.UIComponents()

        self.show()

    def UIComponents(self):
        pass
