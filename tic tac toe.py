import cv2
import numpy as np
from random import randint
import time

class Block():
    def __init__(self, i, j):
        self.value = None
        self.pos = (i, j)

    def setValue(self, value):
        self.value = value

class GUI():
    def __init__(self, windowName):
        self.windowName = windowName
        self.width, self.height = 500, 500
        self.menuHeight = 100
        self.image = np.zeros((self.height + self.menuHeight, self.width, 3), np.uint8)
        self.turn = 1
        self.vsCom = 0
        self.reset()

    def reset(self):
        self.blocks = []
        self.win = False
        self.change = True
        self.selected = False
        for i in range(3):
            row = []
            for j in range(3):
                row.append([Block(i, j), (j * (self.width // 3) + 3, i * (self.height // 3) + 3),
                            ((j + 1) * (self.width // 3) - 3, (i + 1) * (self.height // 3) - 3)])
            self.blocks.append(row)


    def draw(self):
        self.image = np.zeros((self.height + self.menuHeight, self.width, 3), np.uint8)
        for i in range(3):
            for j in range(3):
                start_point = self.blocks[i][j][1]
                end_point = self.blocks[i][j][2]
                cv2.rectangle(self.image, start_point, end_point, (255, 255, 255), -1)
                value = " " if self.blocks[i][j][0].value is None else self.blocks[i][j][0].value
                cv2.putText(self.image, value, (j * (self.width // 3) + 25, (i * self.height // 3) + 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 0, 0), 5)
        if self.checkWin():
            string = ("Player " + str(
                self.turn) + " Wins" if self.turn != self.vsCom else "Computer Wins") if self.turn == 1 else (
                "Player " + str(2) + " Win" if self.turn != self.vsCom else "Computer Win")
        else:
            if not self.checkDraw():
                string = ("Player " + str(
                    self.turn) + "'s Turn" if self.turn != self.vsCom else "Computer's Turn") if self.turn == 1 else (
                    "Player " + str(2) + "'s Turn" if self.turn != self.vsCom else "Computer's Turn")
            else:
                string = "Match Draw!!"
        cv2.putText(self.image, string, (self.width // 2 - 70, self.height + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (255, 255, 255), 1)
        cv2.putText(self.image, "R - Reset", (10, self.height + 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        cv2.putText(self.image, "Esc - Exit", (10, self.height + 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        string = "vs Computer" if self.vsCom == 0 else "vs Human"
        cv2.putText(self.image, "Space - " + string, (self.width // 2 + 10, self.height + 80), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (255, 255, 255), 1)

        if self.selected and not (self.checkWin() or self.checkDraw()):
            self.change = True
            self.selected = False
            self.turn *= -1


    def mainLoop(self):
        cv2.namedWindow(self.windowName)
        cv2.setMouseCallback(self.windowName, self.mouseCall)
        try:
            while True and cv2.getWindowProperty(self.windowName, 1) != -1:
                if self.change:
                    self.change = False
                    self.draw()

                    if self.vsCom == self.turn and not (self.checkWin() or self.checkDraw()):
                        block = self.nextMove()
                        block.setValue("x" if self.turn == 1 else "o")

                        self.selected = True
                        self.change = True

                    cv2.imshow(self.windowName, self.image)
                key = cv2.waitKey(1)
                if key == 27:
                    break
                elif key == ord("r") or key == ord("R"):
                    self.reset()
                if key == ord(" ") and not (self.checkWin() or self.checkDraw()):
                    if self.vsCom:
                        self.vsCom = 0
                    else:
                        self.vsCom = self.turn
                    self.change = True
            cv2.destroyAllWindows()
        except:
            print("Window is successfully closed")

    def checkWin(self):
        self.win = False
        if (self.blocks[0][0][0].value is not None and self.blocks[0][0][0].value == self.blocks[0][1][0].value ==
            self.blocks[0][2][0].value) or (
                self.blocks[1][0][0].value is not None and self.blocks[1][0][0].value == self.blocks[1][1][0].value ==
                self.blocks[1][2][0].value) or (
                self.blocks[2][0][0].value is not None and self.blocks[2][0][0].value == self.blocks[2][1][0].value ==
                self.blocks[2][2][0].value) or (
                self.blocks[0][0][0].value is not None and self.blocks[0][0][0].value == self.blocks[1][0][0].value ==
                self.blocks[2][0][0].value) or (
                self.blocks[0][1][0].value is not None and self.blocks[0][1][0].value == self.blocks[1][1][0].value ==
                self.blocks[2][1][0].value) or (
                self.blocks[0][2][0].value is not None and self.blocks[0][2][0].value == self.blocks[1][2][0].value ==
                self.blocks[2][2][0].value) or (
                self.blocks[0][0][0].value is not None and self.blocks[0][0][0].value == self.blocks[1][1][0].value ==
                self.blocks[2][2][0].value) or (
                self.blocks[2][0][0].value is not None and self.blocks[2][0][0].value == self.blocks[0][2][0].value ==
                self.blocks[1][1][0].value):
            self.win = True
        return self.win

    def checkDraw(self):
        flag = True
        for i in range(3):
            for j in range(3):
                if self.blocks[i][j][0].value == None:
                    flag = False
        return flag

    def nextMove(self):
        flag = 0
        blocks = []
        for i in range(3):
            for j in range(3):
                if self.blocks[i][j][0].value == None:
                    blocks.append(self.blocks[i][j][0])
        if not (len(blocks) == sum([len(row) for row in self.blocks]) or len(blocks) == sum(
                [len(row) for row in self.blocks]) - 1 or len(blocks) == 1):
            scoresList = {}
            for block in blocks:
                if block.value == None:
                    if self.computerWins(block):
                        scoresList[block] = 50
                    elif self.playerWins(block):
                        scoresList[block] = -50
                    elif not self.checkDraw():
                        block.value = ("x" if self.turn == 1 else "o")
                        scoresList[block] = self.min_max(1, self.vsCom)
                        block.value = None
                    else:
                        scoresList[block] = 0

            bestScore = (
                min(scoresList.values()) if abs(min(scoresList.values())) > abs(max(scoresList.values())) else max(
                    scoresList.values()))
            blocks = []
            for block in scoresList:
                if scoresList[block] == bestScore:
                    blocks.append(block)
        choice = blocks[randint(0, len(blocks) - 1)]

        return choice

    def min_max(self, depth, player):
        scoresList = []
        for row in self.blocks:
            for block in row:
                if block[0].value == None:
                    if self.computerWins(block[0]):
                        return (50 - depth)
                    elif self.playerWins(block[0]):
                        return (-50 + depth)
                    else:
                        block[0].value = ("x" if self.turn == 1 else "o")
                        scoresList.append(self.min_max(depth + 1, player * -1))
                        block[0].value = None
        if scoresList:
            return (min(scoresList) if abs(min(scoresList)) > abs(max(scoresList)) else max(scoresList))
        return 0

    def computerWins(self, block):
        flag = False
        block.value = ("x" if self.vsCom == 1 else "o")
        if self.checkWin(): flag = True
        self.win = False
        block.value = None
        return flag

    def playerWins(self, block):
        flag = False
        block.value = ("x" if self.vsCom != 1 else "o")
        if self.checkWin(): flag = True
        self.win = False
        block.value = None
        return flag

    def mouseCall(self, event, posx, posy, flag, param):
        if event == cv2.EVENT_LBUTTONDOWN and not self.win and self.turn != self.vsCom:
            self.setBlockInPos(posx, posy)

    def setBlockInPos(self, x, y):
        for i in range(3):
            for j in range(3):
                if self.blocks[i][j][0].value is None and self.blocks[i][j][1][0] <= x <= self.blocks[i][j][2][0] and \
                        self.blocks[i][j][1][1] <= y <= self.blocks[i][j][2][1]:
                    self.blocks[i][j][0].setValue("x" if self.turn == 1 else "o")
                    self.change = True
                    self.selected = True
                    break


game = GUI("TicTacToe by Varun, Kusti and  Soerensen")
game.mainLoop()
