import random
from entity import *

initiativeOrder = []


def user_int_input(name, request_phrase):
    """ask user for the integer


    Keyword arguments:
    name -- name of entity
    request_phrase -- prompt to ask user
    """
    initiative = input(">> " + name + "'s " + request_phrase + ": ")
    while not initiative.isdigit():
        print(">> please input an integer")
        initiative = input(">> " + name + "'s " + request_phrase + ": ")

    return int(initiative)


def insertPlayers():
    global initiativeOrder

    f = open('playerCharacters.txt', 'r')
    players_str = f.read().split(" ")
    f.close()

    for pcs in players_str:
        pcs = pcs.split(",")
        initiativeOrder.append(Player(pcs[0], pcs[1], user_int_input(pcs[0], "initiative")))
        # initiativeOrder.append(Player(pcs[0], pcs[1], pcs[2]))


def insertEnemies():
    name = input(">> Enemy's name: ")
    initative = user_int_input(name, "initiative")
    hitpoints = user_int_input(name, "hit points")
    Enemy(name, hitpoints, initative)
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
        cmd = input(">> ")
        if cmd == 'q':
            return
        elif cmd == 'n':
            currEntity += 1
            if currEntity >= len(initiativeOrder):
                currEntity = 0
            print(initiativeOrder[currEntity])
        elif cmd != "" and cmd[0] == 'a':
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
    initiativeOrder.sort(reverse=True)
    print(initiativeOrder)
    command()



if __name__ == "__main__":
    # run with python 3!!
    main()

