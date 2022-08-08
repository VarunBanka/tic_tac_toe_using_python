from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QWidget, QLabel, QMessageBox


class OnlineMP(QWidget):
    def __init__(self, session_id) -> None:
        super().__init__()
        self.session_id = session_id
        self.setGeometry(300, 300, 600, 450)
        self.setFixedSize(self.size())
        self.setWindowTitle("TicTacToe - Online Multiplayer")

        self.UIComponents()
        self.show()

    def UIComponents(self):
        pass
