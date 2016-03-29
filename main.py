from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, BooleanProperty, DictProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import random



#Main game class that keeps track of game variable+s
class Scoreboard(Widget):

    dollars = NumericProperty(400 + random.randint(-150,200))
    bitcoins = NumericProperty(0)
    debug = BooleanProperty(False)
    income = NumericProperty(0) #In BTC
    btc_rate = NumericProperty(300) # exchange rate in dollars
    equipment = DictProperty()

    #Workaround. Didn't figure out any other way. Feel free to fix this.
    def restart(self):
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

    def update(self, dt):
        self.t
        if self.t < 60:
            self.t += 1
        else:
            self.t = 0

        if self.t%60 == 0:
            self.score.btc_rate = round(self.score.btc_rate+random.randint(-100,110)/10, 1)



class Actions(BoxLayout):
    def exchange(self, parent):
        MainWindow.exchange(self, parent.main)

    def shop(self, parent):
        MainWindow.shop(self, parent.main)

    def debug(self, parent):
        parent.score.debug = not parent.score.debug
        if parent.score.debug == True:
            parent.score.ids.debug.text = "Debugging ON"
            #ATM this does not do anything.
        else:
            parent.score.ids.debug.text = "Debugging OFF"

    def restart(self, parent):
        parent.score.restart()

class MainWindow(BoxLayout):
    orientation = 'vertical'
    def exchange(self, main):
        main.clear_widgets()

        def on_text(instance, value):
            try:
                buy = float(value)
                if buy>0:
                    button.text = "Buy "+str(buy)+" BTC for "+str(buy*self.parent.score.btc_rate)+"$"
                    if self.parent.score.dollars >= buy * self.parent.score.btc_rate:
                        button.bind(on_release= buy_BTC(buy)) # for some reason this does not wait for button press but executes imideatly
                    else:
                        print("Nout enought money")
                elif buy<0:
                    button.text = "Sell " + str(-buy) + " BTC for " + str(-buy*self.parent.score.btc_rate)+"$"
                    if self.parent.score.bitcoins >= -buy:
                        button.bind(on_release=sell_BTC(-buy)) # for some reason this does not wait for button press but executes imideatly
                    else:
                        print("Not enough BTC")
            except ValueError:
                button.text = "You need to enter a number"

        def sell_BTC(sell):
                self.parent.score.bitcoins -= sell
                self.parent.score.dollars += sell * self.parent.score.btc_rate
        def buy_BTC(buy):
            self.parent.score.bitcoins += buy
            self.parent.score.dollars -= buy * self.parent.score.btc_rate

        label = Label(text="How much BTC do you want to buy?")
        main.add_widget(label)
        textinput = TextInput(multiline=False)
        textinput.bind(text=on_text)
        main.add_widget(textinput)
        button = Button(text="0")
        main.add_widget(button)

    def shop(self, main):
        label = Label(text="What would you like to buy?")
        main.add_widget(label)

        box = BoxLayout()
        main.add_widget(box)
        for i in range(5):
            item = Button(text="Item "+str(i))
            box.add_widget(item)
        button = Button(text="0")
        main.add_widget(button)




class MainApp(App):
    def build(self):
        game = MainGame()
        game.t=0
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        print("Game started.")
        return game


if __name__ == '__main__':
    MainApp().run()