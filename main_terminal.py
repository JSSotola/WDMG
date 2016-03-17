import random
import time
import shop
import market
from tabulate import tabulate
import numpy as np

start_time = time.time()

#Main game class that keeps track of game variables
class State():
    def __init__(self):

        self.dollars = 400 + random.randint(-150,200)
        self.bitcoins = 0
        self.debug = 0
        self.income = 0 #In BTC
        self.btc_rate = 300 # exchange rate in dollars
        self.equipment = np.zeros(shape = (1,9))
        self.shop = shop.Shop()
        self.time_last_tick = time.time()


############
#checks commands and executes the correct one
#Since Python does not have cases/switches this is done with elif's it could also be donne with dictionary but this seemed simpler.
def command(argument):
    cmds = ["quit" or "q", "restart" or "r", "help" or "h", "debug" or "d", "shop", "inventory", "status" or "s", "cmd7" , "exchange", "market", "equipment" or "e"] # list of commands
    help = ["Quits the game", "Restarts", "Displays this help file", "Debug on or off", "Opens the legal store", "Displays what you own", "Updates the game state", "Does nothing", "Currency exchange", "The illegal market", "displays equipment"]
    print("\n")
    if argument in (cmds[0]):
        quit()
    elif argument in cmds[1]:
        start()

    elif argument in cmds[2]:
        print("Availible commands are:")
        print(tabulate({"Command": cmds, "Description":help}, headers="keys" ))


    elif argument in cmds[3]:
        game.debug = (game.debug + 1)%2
        print("Debug set to:", game.debug)

    elif argument in cmds[4]:
        game.shop.display_inventory(game)


    elif argument in cmds[5]:
        print("You do not own anything. Try buying something in the shop or on the market.")

    elif argument in cmds[6]:
        pass #just updates the game

    elif argument in cmds[7]:
        pass # will do something

    elif argument in cmds[8]:
        exchange()

    elif argument in cmds[9]:
        market
    elif argument in cmds[10]:
        if len(game.equipment) > 0:
            print(tabulate(game.equipment))
        else:
            print("You have no equipment at the moment. Try shopping for something.")
    else:
        print("Sorry, command not found :(")


def exchange():
    print("How many BTC to buy?\n NB: Enter negative number to sell. 'r' to return to the main screen.\n The current rate is", game.btc_rate, "$ per BTC")
    buy = input("Buy BTC:")
    if buy in ["r", 0, "q"]:
        print("Returning to main menu")
    else:
        try:
            buy = float(buy)
            if buy >= 0:
                if game.dollars >= buy*game.btc_rate:
                    game.dollars -= buy*game.btc_rate
                    game.bitcoins += buy
                    print(buy, "BTC bought at", game.btc_rate, "$ per BTC")
                else:
                    print("Insufficient funds. Try again")
                    exchange()
            elif buy < 0:
                if game.bitcoins >= -buy:
                    game.dollars -= buy*game.btc_rate
                    game.bitcoins += buy
                    print(buy, "BTC sold at", game.btc_rate, "$ per BTC")
                else:
                    print("Insufficient funds. Try again")
                    exchange()

        except ValueError:
            print("Not really a number. Try again")
            exchange()


def start(): #starting    scrip, sets initial variables etc.
    # Display a title bar.
    print("\t**********************************************")
    print("\t***  Welcome!  ***")
    print("\t**********************************************")
    game.__init__()


#Updates the state of the game, might be better to do this in paralel. Resp. maybe not neccesary,
#as in the final version the game will not wait for user input.
def tick():
    #calculates time since last time game was updated
    since_last = time.time() - game.time_last_tick
    game.time_last_tick = time.time() #set up for next interation

    #sets income depending on the current equipement
    game.income = np.sum(game.equipment[:,4].astype(np.float))

    game.bitcoins += game.income*since_last
    game.btc_rate += random.randint(-300,300)/10


def status():
    print("\nState of the game:")
    print("   $:", game.dollars)
    print("   BTC:", game.bitcoins)
    print("   $ per BTC:", game.btc_rate)
    if game.debug == 1: #debuging info the players will normally not see
        print("Debuging info:")
        print("   Income:", game.income)
        print("   Seconds since start:", round(time.time() - start_time,1))


game = State()
start()
while True: # main game loop
    tick()
    status()
    cmd = input("Enter command:")
    command(cmd)