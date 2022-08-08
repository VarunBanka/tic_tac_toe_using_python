from PyQt5.QtWidgets import QWidget, QPushButton, QWidget, QLineEdit, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QRect, Qt
import random
import requests
from modes.online_mp import OnlineMP


class OnlineMenu(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setGeometry(300, 300, 300, 450)
        self.setFixedSize(self.size())
        self.setWindowTitle("TicTacToe - Local Multiplayer")

        self.UIComponents()

        self.show()

    def UIComponents(self):
        self.join_input = QLineEdit(self)
        self.join_input.setGeometry(QRect(135, 50, 150, 50))
        self.join_input.setPlaceholderText("Enter host ID")
        self.join_input.setAlignment(Qt.AlignCenter)
        self.join_input.setFont(QFont("Arial", 12))

        self.join_btn = QPushButton(self)
        self.join_btn.setText("Join")
        self.join_btn.setGeometry(QRect(135, 125, 150, 50))
        self.join_btn.clicked.connect(self.join)

        self.create_btn = QPushButton(self)
        self.create_btn.setText("Create")
        self.create_btn.setGeometry(QRect(135, 175, 150, 50))
        self.create_btn.clicked.connect(self.create)

        self.status = QLabel(self)
        self.status.setText("")
        self.status.setFont(QFont("Arial", 12))
        self.status.setAlignment(Qt.AlignCenter)
        self.status.setGeometry(QRect(0, 225, 300, 50))

    def join(self):
        # Get the session ID from the input field
        try:
            self.session_id = int(self.join_input.text())
        except ValueError:
            self.status.text(response["message"])
            return

        # Send a request to the server to join the session
        url = f"https://Tic-Tac-Toe.varunbanka18.repl.co/join"
        response = requests.post(
            url, json={"session_id": self.session_id}).json()

        if response["status"] == "error":
            self.status.text(response["message"])
            return

        self.hide()
        self.win = OnlineMP(self.session_id)
        self.win.show()

    def create(self):
        self.session_id = random.randint(1, 100000)

        # Create a new session
        url = f"https://Tic-Tac-Toe.varunbanka18.repl.co/create"
        response = requests.post(
            url, json={"session_id": self.session_id}).json()
        if response["status"] == "error":
            self.status.text(response["message"])
            return
        self.hide()
        self.win = OnlineMP(self.session_id)
        self.win.show()
