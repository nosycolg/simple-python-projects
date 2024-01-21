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
        il = ic = 0
        while il < 3:
            soma = 0
            ic = 0
            while ic < 3:
                if hash[il][ic] == True:
                    soma += 1
                ic += 1
            if soma == 3:
                win = True
                break
            il += 1
        if win != False:
            break
        # verify columns
        il = ic = 0
        while ic < 3:
            soma = 0
            il = 0
            while il < 3:
                if hash[il][ic] == True:
                    soma += 1
                il += 1
            if soma == 3:
                win = True
                break
            ic += 1
        if win != False:
            break
        # verify diagonal
        soma = 0
        idiag = 0
        while idiag < 3:
            if hash[idiag][idiag] == True:
                soma += 1
            idiag += 1
        if soma == 3:
            win = True
            break
        # verify diagonal
        soma = 0
        idiagl = 0
        idiagc = 2
        while idiagc >= 0:
            if hash[idiagl][idiagc] == True:
                soma += 1
            idiagl += 1
            idiagc -= 1
        if soma == 3:
            win = True
            break
    return win


while True:
    Screen()
    WhoPlay()
    CPUPlay()
    Screen()
    whoWin = VerifyWin()
    print(whoWin)
    if whoWin != False or plays >= maxPlays:
        break
    
    print(Fore.RED + "FIM DE JOGO" + Fore.YELLOW)
    if (whoWin=="X" or whoWin=="O"):
        print('Resultado: Jogador ' + whoWin + " venceu")
    else:
        print('Resultado: Empate')
