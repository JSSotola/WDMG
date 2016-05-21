from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, BooleanProperty, DictProperty, ObjectProperty, BoundedNumericProperty
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty
import random
import actions, shop_function, marketplace, events, drug_lab, exchange, start_screen

#To do
#todo Finish marketplace. Implement actual items.
#todo Finish druglab.
#todo Finish shop items. Do not increase income ATM.
#todo Add ingredients to shop.
#todo Implement risk as a result of actions.
#todo Add textboxes that explain things to the player.
#todo Make reset work better and fix for new implementations such as equipment and risk.
#todo Add graphics
#todo Make presentation


#main variables settings
minutes = 15
timelimit = minutes*60*100
timefactor = 0.003
dollarfactor = 0.01
stealthfactor = 0.2
introduction_screen = True
random_events = False
checkTOR = False #todo put True here when finished testing




#Main game class that keeps track of game variables
class Scoreboard(Widget):

    #graphic properties


    #properties
    dollars = BoundedNumericProperty(400 + random.randint(-150,200), min = 0)
    bitcoins = BoundedNumericProperty(50, min = 0)
    debug = BooleanProperty(False)
    income = NumericProperty(0) #In BTC
    btc_rate = BoundedNumericProperty(300, min = 50) # exchange rate in dollars
    equipment = DictProperty()
    ingredients = DictProperty()
    equipment_list = StringProperty()
    ingredients_list = StringProperty()
    selected_ingredients = DictProperty()

    notcheckTOR = BooleanProperty(not checkTOR)
    time = NumericProperty(0)
    minutes = NumericProperty(0)
    seconds = NumericProperty(0)
    stealth = NumericProperty(0)
    delta_TOR = (2) # sets timing in TOR connection, gets decreased after first connect
    risk = NumericProperty(0)

    #Workaround. Didn't figure out any other way. Feel free to fix this.
    def restart(self, bool):
        if bool:
            self.dollars = 400 + random.randint(-150, 200)
            self.bitcoins = 0
            self.debug = False
            self.income = 0  # In BTC
            self.btc_rate = 300 # exchange rate in dollars
            #self.equipment = implement based on equipment implementation


class MainGame(Widget):
    score = ObjectProperty(None)
    actions = ObjectProperty(None)
    main = ObjectProperty(None)



    #updates the game, executes every 1/60 of a second. See MainApp at the end of this file
    def update(self, dt):
        self.t
        self.score.time=self.t
        self.score.minutes = int(self.t/6000)
        self.score.seconds = int((self.t/100)%60)


        #Risk inscrease
        self.score.risk = int((self.t * timefactor) + (self.score.dollars * dollarfactor) + (self.score.stealth * stealthfactor))



        if introduction_screen:
            try:
                self.start
                image = Button(text="AAA")
                self.score.add_widget(image)

            except AttributeError:
                start_screen.start(self)
                self.start = False

        if self.t <= timelimit:
            self.t += 1
        else:
            self.t = 0
            actions.killed()
            #endgame

        self.prob_events = 0.01

        #Random walk for bitcoin to dollar rate. Slight bias towards increasing.
        if self.t%200 == 0:
            self.score.btc_rate = round(self.score.btc_rate+random.randint(-100,110)/10, 1)
            if random.random() > self.prob_events and random_events:
                events.Events.event(self, self)
            self.score.bitcoins = round(self.score.income+self.score.bitcoins, 3)


#defines button press actions for the lower bar
#passes parent.main as the main game class to all functions so that functions can interface with the main game class
class Actions(BoxLayout):


    def exchange(self, parent):
        exchange.exchange(self, parent.main)

    def lab(self, parent):
        drug_lab.lab(self, parent.main)

    def shop(self, parent):
        shop_function.shop(self, parent.main)#Should be called directly not through MainWindow

    def market(self, parent):
        marketplace.marketplace(self,parent.main)#Should be called directly not through MainWindow

    #Debuging inteface. Right now this does not do much. Might be important for play testing
    #disabled in main.kv ATM
    def debug(self, parent):
        parent.score.debug = not parent.score.debug
        if parent.score.debug == True:
            parent.score.ids.debug.text = "Debugging ON \n More debugging \n information coming\n soon..."
        else:
            parent.score.ids.debug.text = "Debugging OFF"

    def event(self, parent):
        events.Events.event(self, parent)

    def restart(self, parent):
        actions.popupconfirm("you want to restart the game?", parent.score.restart)



#the central 2/3 interface. Most other events and functions interface with this.
class MainWindow(BoxLayout):
    orientation = 'vertical'


#Main game class and fucntion. Initialises the game.
class MainApp(App):
    def build(self):
        game = MainGame()
        game.t=0
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        print("Game started.")
        return game


if __name__ == '__main__':
    MainApp().run()

