from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, BooleanProperty, DictProperty, ReferenceListProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
import random



#Main game class that keeps track of game variables
class Scoreboard(Widget):

    dollars = NumericProperty(400 + random.randint(-150,200))
    bitcoins = NumericProperty(0)
    debug = BooleanProperty(0)
    income = NumericProperty(0) #In BTC
    btc_rate = NumericProperty(300) # exchange rate in dollars
    equipment = DictProperty()

class MainGame(Widget):

    def update(self, dt):
        pass

class Actions(BoxLayout):

    def press(self):
        self.ids.button1.text = "Pressed"
        self.ids.label1.text = "test2"

class MainApp(App):
    def build(self):
        game = MainGame()

        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return MainGame()


if __name__ == '__main__':
    MainApp().run()