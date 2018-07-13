import random
from entity import *

initiativeOrder = []

def getInitative(name):
    """ask user for the initiative of the Entity


    Keyword arguments:
    name -- name of player
    """
    initiative = input(name + "'s initiative: ")
    while not initiative.isdigit():
        print("please input an integer")
        initiative = input(name + "'s initiative: ")

    return int(initiative)


def insertPlayers():
    global initiativeOrder

    f = open('playerCharacters.txt', 'r')
    players_str = f.read().split(" ")
    f.close()

    for pcs in players_str:
        pcs = pcs.split(",")
        initiativeOrder.append(Player(pcs[0], pcs[1], getInitative(pcs[0])))


def insertEnemies():
    pass
    # initiative = input(name + "'s initiative: ")
    # while True:


def command():
    """executes command depending on cmd


    Possible cmd values:
            q: quit
            n: print next character in initiative order
            a EntityID Damage: attack an entity with EntityID dealing Damage
    """
    global initiativeOrder
    currEntity = 0

    while True:
        cmd = input(">>")
        if cmd == 'q':
            return
        elif cmd == 'n':
            currEntity += 1
            print(initiativeOrder[currEntity])
        elif cmd[0] == 'a':
            # call attack on an enem
            pass
        else:
            print("command not recognized")


def main():
    global initiativeOrder

    # stage 1: insert players into initiative list
    insertPlayers()

    # stage 2: insert enemies into initiative list
    insertEnemies()

    # stage 3: execute initative order
    initiativeOrder.sort()
    command()



if __name__ == "__main__":
    main()

