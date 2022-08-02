import socket 
import threading
import random

HEADER = 64
PORT = 5050
# SERVER = socket.gethostbyname(socket.gethostname())
SERVER = "192.168.0.16"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
MAX_CONNECTIONS = 2
connections = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

class game():
    def __init__(self, player1, player2) -> None:
        self.player1 = player1
        self.player2 = player2
        players = (player1, player2)
        self.turn = 0
        self.first_move = random.randint(0, 1)
        self.xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pass

    def get_sum(a, b, c):
        return a + b + c


    def printBoard(self):
        zero = 'X' if self.xState[0] else ('O' if self.zState[0] else 0)
        one = 'X' if self.xState[1] else ('O' if self.zState[1] else 1)
        two = 'X' if self.xState[2] else ('O' if self.zState[2] else 2)
        three = 'X' if self.xState[3] else ('O' if self.zState[3] else 3)
        four = 'X' if self.xState[4] else ('O' if self.zState[4] else 4)
        five = 'X' if self.xState[5] else ('O' if self.zState[5] else 5)
        six = 'X' if self.xState[6] else ('O' if self.zState[6] else 6)
        seven = 'X' if self.xState[7] else ('O' if self.zState[7] else 7)
        eight = 'X' if self.xState[8] else ('O' if self.zState[8] else 8)
        return f"""{zero} | {one} | {two}
--|---|---
{three} | {four} | {five}
--|---|---
{six} | {seven} | {eight}"""


    def checkWin(self):
        wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for win in wins:
            if (sum(self.xState[win[0]], self.xState[win[1]], self.xState[win[2]]) == 3):
                print("X Won the match")
                return 1
            if (sum(self.zState[win[0]], self.zState[win[1]], self.zState[win[2]]) == 3):
                print("O Won the match")
                return 0
        return -1


    """if __name__ == "__main__":
        self.xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        turn = 1  # 1 for X and 0 for O
        print("Welcome to Tic Tac Toe")
        while (True):
            printBoard(self.xState, self.zState)
            if (turn == 1):
                print("X's Chance")
                value = int(input("Please enter a value: "))
                self.xState[value] = 1
            else:
                print("O's Chance")
                value = int(input("Please enter a value: "))
                self.zState[value] = 1
            cwin = checkWin(self.xState, self.zState)
            if (cwin != -1):
                print("Match over")
                break

            turn = 1 - turn"""

# start()
"""def restart_and_exit():
    print("do you want to restart ? \n")
    restart = input("y/n \n")
    if restart == "y":
        game_start()
    if restart == "n":
        print("okay, exiting.....")
        print("end of program")
        exit()"""

# restart_and_exit()

# xyz_pro_plus = 1

"""while (xyz_pro_plus < 2):
    restart_and_exit()"""


def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        if len(connections) >= MAX_CONNECTIONS:
            conn.send("Sorry, too many connections!".encode(FORMAT))
            conn.close()
            continue
        connections.append(conn)

        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        
        if len(connections) == 2:
            print("Two players connected!")
            print("Starting game...")
            tictactoe = game(connections[0], connections[1])
            connections[0].send("You are player 1\n".encode(FORMAT))
            connections[1].send("You are player 2\n".encode(FORMAT))
            [connection.send(f"player{tictactoe.first_move + 1} goes first\n".encode(FORMAT)) for connection in connections]
            connections[0].send("""You are "X's" \n""".encode(FORMAT))
            connections[1].send("""You are "O's" \n""".encode(FORMAT))
            connections[tictactoe.first_move + tictactoe.turn].send(f"{tictactoe.printBoard()}\n".encode(FORMAT))
            connections[tictactoe.first_move + tictactoe.turn].send("Your turn".encode(FORMAT))
            # print(connections[tictactoe.first_move + tictactoe.turn].recv(2048).decode(FORMAT))
        # print(connections[0].recv(2048).decode(FORMAT))

start()
