class Board:
    def __init__(self):
        self.boardState = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def play(self):
        turn = 1  # 1 for X and 0 for O
        print("Welcome to Tic Tac Toe")
        while True:
            self.printBoard()
            if turn == 1:
                print("X's Chance")
                value = self.checkInput()
                self.boardState[value] = "X"
            else:
                print("O's Chance")
                value = self.checkInput()
                self.boardState[value] = "O"

            cwin = self.checkWin()
            if cwin:
                print("Match over")
                break

            turn = 0 if turn else 1

    def checkInput(self):
        while True:
            try:
                value = int(input("Please enter a value: "))
            except ValueError:
                print("Please enter a valid value")
                continue
            if value > 9 or value < 0:
                print("Please enter a valid value")
                continue
            break
        return value

    def printBoard(self):
        print("---------")
        for i in range(0, 9):
            if i % 3 != 0:
                print("|", end=" ")
            if self.boardState[i] == "X":
                print("X", end=" ")
            elif self.boardState[i] == "O":
                print("O", end=" ")
            else:
                print(i, end=" ")
            if (i + 1) % 3 == 0:
                print("\n---------")

    def checkWin(self):
        wins = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6],
        ]

        for win in wins:
            if (
                self.boardState[win[0]] == "X"
                and self.boardState[win[1]] == "X"
                and self.boardState[win[2]] == "X"
            ):
                print("X wins")
                return True
            elif (
                self.boardState[win[0]] == "O"
                and self.boardState[win[1]] == "O"
                and self.boardState[win[2]] == "O"
            ):
                print("O wins")
                return True

        if 0 not in self.boardState:
            print("Draw")
            return True

        return False


if __name__ == "__main__":
    Board().play()
    while True:
        print("Do you want to restart ? \n")
        restart = input("y/n\n").lower()
        if restart == "y" or restart == "n":
            break

    if restart == "y":
        Board().play()

    if restart == "n":
        print("okay, exiting.....")
        print("end of program")
        exit()
