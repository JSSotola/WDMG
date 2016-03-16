import os
import sys
import numpy as np
import random
import time

start_time = time.time()#probably not a good implementation



class State():
    def __init__(self):

        self.dollars = 100 + random.randint(-25,50)
        self.debug = 0
        self.income =1

cmds = ["restart", "help", "debug", "shop", "inventory", "cmd5"] # list of commands
def command(argument):
    print("\n")
    if argument == cmds[0]:
        start()

    elif argument == cmds[1]:
        print("Availible commands are:", cmds)

    elif argument == cmds[2]:
        game.debug = (game.debug + 1)%2
        print("Debug set to:", game.debug)

    elif argument == cmds[3]:
        pass # will open a shop

    elif argument == cmds[4]:
        pass # will display inventory

    elif argument == cmds[5]:
        pass # will ...
    else:
        print("Command not found :(")

    return

def start(): #starting    scrip, sets initial variables etc.
    # Display a title bar.
    print("\t**********************************************")
    print("\t***  Welcome!  ***")
    print("\t**********************************************")
    game.__init__()


before = 0 # dummy just to initialise
def tick():

    since_last = time.time() - start_time - before
    last = time.time() - start_time
    game.dollars += game.income*since_last


def status():
    print("\nState of the game")
    print("Seconds since start:", round(time.time() - start_time,1))
    print("$:", game.dollars)
    if game.debug == 1: #an example of debuging info the players will normally not see
        print("Income:", game.income)
    return

game = State()

start()

while True: # main game loop
    tick()
    status()
    cmd = input("Enter command:")
    command(cmd)
