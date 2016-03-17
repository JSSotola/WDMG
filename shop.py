#This is the legal store where you can buy computers, chemistry sets and what not. Pay with dollars.
import numpy as np
from tabulate import tabulate


class Shop():
    def __init__(self):
        raw_data = np.genfromtxt('shop_inventory.csv', delimiter=',', dtype=np.str_)
        self.inventory = raw_data

    def display_inventory(self,game):
        print("Items availible:")
        #implement a loop that checks conditions and does not display locked items
        print(tabulate(self.inventory[:,:4]))
        if game.debug == 1:
            print("Debuging info:")
            print(tabulate(self.inventory[:,4:]))
        self.buy(game)
    def buy(self, game):
        print("What would you like?")
        print("Enter 'r' to return to the main screen.")
        print("You have", game.dollars, "$.")

        buy = input("Enter item number")
        if buy in ["r", 0, "q"]:
            print("Returning to main menu")
        else:
            try:
                buy = int(buy)
                if buy >= 0:
                    cost = float(self.inventory[buy,2])
                    if game.dollars >= cost:
                        game.dollars -= cost

                        game.equipment = np.append(game.equipment, np.reshape(self.inventory[buy,:], (1,9)), axis = 0)
                        print(self.inventory[buy,1], "bought.")
                        return
                    else:
                        print("Insufficient funds. Try again")
                        self.buy(game)
                else:
                    print("Insufficient funds. Try again")
                    self.buy(game)
            except ImportError:#ValueError:
                pass
            #    print("Not really a number. Try again")
            #    self.buy(game)
