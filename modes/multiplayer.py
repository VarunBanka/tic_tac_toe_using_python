from PyQt5.QtWidgets import QMainWindow


class Multiplayer(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setGeometry(300, 300, 600, 450)
        self.setFixedSize(self.size())
        self.setWindowTitle("TicTacToe - Single Player")

        self.UIComponents()

        self.show()

    def UIComponents(self):
        pass
