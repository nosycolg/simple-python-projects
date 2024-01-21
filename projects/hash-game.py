import os
import random
from colorama import Fore, Back, Style

playAgain = True
plays = 0
whoPlay = 2
maxPlays = 9
win = False
hash = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]


def Screen():
    global hash
    global plays
    os.system("clear")
    print("    0   1   2")
    print("0:  " + hash[0][0] + " | " + hash[0][1] + " | " + hash[0][2])
    print("  -------------")
    print("1:  " + hash[1][0] + " | " + hash[1][1] + " | " + hash[1][2])
    print("  -------------")
    print("2:  " + hash[2][0] + " | " + hash[2][1] + " | " + hash[2][2])
    print("Plays: " + Fore.GREEN + str(plays) + Fore.RESET)


def WhoPlay():
    global plays
    global whoPlay
    global win
    global maxPlays
    if whoPlay == 2 and plays < maxPlays:
        l = int(input("Line: "))
        c = int(input("Column: "))
        while hash[l][c] != " ":
            l = int(input("Line: "))
            c = int(input("Column: "))
        try:
            hash[l][c] = "X"
            whoPlay = 1
            plays += 1
        except:
            print("Invalid line or column")


def CPUPlay():
    global plays
    global whoPlay
    global win
    global maxPlays
    if whoPlay == 1 and plays < maxPlays:
        l = random.randrange(0, 3)
        c = random.randrange(0, 3)
        while hash[l][c] != " ":
            l = random.randrange(0, 3)
            c = random.randrange(0, 3)
        hash[l][c] = "O"
        whoPlay = 2
        plays += 1


def VerifyWin():
    global hash
    win = False
    symbles = ["X", "O"]
    for s in symbles:
        win = False
        # verify lines
        lines = 0
        columns = 0
        while lines < 3:
            sum = 0
            columns = 0
            while columns < 3:
                if hash[lines][columns] == s:
                    sum += 1
                columns += 1
                print(hash[0][0])
            if sum == 3:
                win = s
                break
            lines += 1
            if win != False:
                break
        # verify columns
        lines = 0
        columns = 0
        while columns < 3:
            sum = 0
            lines = 0
            while lines < 3:
                if hash[lines][columns] == s:
                    sum += 1
                lines += 1
            if sum == 3:
                win = s
                break
            columns += 1
        if win != False:
            break
        # verify diagonal
        sum = 0
        idiag = 0
        while idiag < 3:
            if hash[idiag][idiag] == s:
                sum += 1
            idiag += 1
        if sum == 3:
            win = s
            break
        # verify diagonal
        sum = 0
        idiagl = 0
        idiagc = 2
        while idiagc >= 0:
            if hash[idiagl][idiagc] == s:
                sum += 1
            idiagl += 1
            idiagc -= 1
        if sum == 3:
            win = s
            break
    return win


while True:
    Screen()
    WhoPlay()
    CPUPlay()
    Screen()
    whoWin = VerifyWin()
    if whoWin != False or plays >= maxPlays:
        print(Fore.RED + "FIM DE JOGO" + Fore.YELLOW)
        if whoWin == "X" or whoWin == "O":
            print("Resultado: Jogador " + whoWin + " venceu")
        else:
            print("Resultado: Empate")
        break
