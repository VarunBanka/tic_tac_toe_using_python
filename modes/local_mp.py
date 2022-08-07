from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QWidget, QLabel, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QRect, Qt
from functools import partial


class Local_MP(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setGeometry(300, 300, 600, 450)
        self.setFixedSize(self.size())
        self.setWindowTitle("TicTacToe - Local Multiplayer")

        self.UIComponents()

        self.show()

    def UIComponents(self):
        # Make grid
        self.widget = QWidget(self)
        self.grid = QGridLayout(self.widget)
        self.grid.setAlignment(Qt.AlignCenter)
        self.grid.setSpacing(10)
        self.grid.setContentsMargins(25, 25, 0, 0)
        self.grid.setSizeConstraint(QGridLayout.SetFixedSize)

        self.turn_label = QLabel(self)
        self.turn_label.setText("Player 1's turn")
        self.turn_label.setFont(QFont("Arial", 12))
        self.turn_label.setAlignment(Qt.AlignCenter)
        self.turn_label.setGeometry(QRect(0, 50, 600, 50))

        # Make buttons
        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = QPushButton(self)
                button.clicked.connect(partial(self.buttonClicked, i * 3 + j))
                button.setFixedSize(100, 100)
                self.grid.addWidget(button, i+1, j)
                self.buttons.append(button)

        # Make exit button
        self.exit_btn = QPushButton(self)
        self.exit_btn.setText("Exit")
        self.exit_btn.setGeometry(QRect(135, 400, 100, 50))
        self.exit_btn.clicked.connect(self.exit)

        # Add everything to the grid
        self.grid.addWidget(self.turn_label, 0, 0, 1, 3)

    def listWidgetClicked(self, item):
        if item.text() == "Exit":
            self.exit()

    def buttonClicked(self, i):
        if self.turn == 0:
            self.buttons[i].setText("X")
        else:
            self.buttons[i].setText("O")
        self.checkWin()
        self.buttons[i].setEnabled(False)

        self.turn = 1 if self.turn == 0 else 0
        self.turn_label.setText(f"Player {self.turn + 1}'s turn")

    def checkWin(self):
        # Check rows
        for i in range(3):
            if self.buttons[i * 3].text() == self.buttons[i * 3 + 1].text() and self.buttons[i * 3 + 1].text() == self.buttons[i * 3 + 2].text() and self.buttons[i * 3].text() != "":
                self.buttons[i * 3].setStyleSheet("background-color: green")
                self.buttons[i * 3 +
                             1].setStyleSheet("background-color: green")
                self.buttons[i * 3 +
                             2].setStyleSheet("background-color: green")
                QMessageBox.information(
                    self, "Winner", f"Player {self.turn + 1} wins!")
                self.restart()

        # Check columns
        for i in range(3):
            if self.buttons[i].text() == self.buttons[i + 3].text() and self.buttons[i + 3].text() == self.buttons[i + 6].text() and self.buttons[i].text() != "":
                self.buttons[i].setStyleSheet("background-color: green")
                self.buttons[i + 3].setStyleSheet("background-color: green")
                self.buttons[i + 6].setStyleSheet("background-color: green")
                QMessageBox.information(
                    self, "Winner", f"Player {self.turn + 1} wins!")
                self.restart()

        # Check diagonals
        if self.buttons[0].text() == self.buttons[4].text() and self.buttons[4].text() == self.buttons[8].text() and self.buttons[0].text() != "":
            self.buttons[0].setStyleSheet("background-color: green")
            self.buttons[4].setStyleSheet("background-color: green")
            self.buttons[8].setStyleSheet("background-color: green")
            QMessageBox.information(
                self, "Winner", f"Player {self.turn + 1} wins!")
            self.restart()

        if self.buttons[2].text() == self.buttons[4].text() and self.buttons[4].text() == self.buttons[6].text() and self.buttons[2].text() != "":
            self.buttons[2].setStyleSheet("background-color: green")
            self.buttons[4].setStyleSheet("background-color: green")
            self.buttons[6].setStyleSheet("background-color: green")
            QMessageBox.information(
                self, "Winner", f"Player {self.turn + 1} wins!")
            self.restart()

        # Check for tie
        for i in range(9):
            if self.buttons[i].text() == "":
                break
        else:
            QMessageBox.information(
                self, "Tie", "It is a tie!")
            self.restart()

    def restart(self):
        for i in range(9):
            self.buttons[i].setText("")
            self.buttons[i].setEnabled(True)
            self.buttons[i].setStyleSheet("background-color: #455364")
        self.turn = 0
        self.turn_label.setText("Player 1's turn")

    def exit(self):
        self.close()
