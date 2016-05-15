from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, BooleanProperty, DictProperty, ReferenceListProperty, ObjectProperty
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.video import Video
from kivy.uix.image import Image
import random
from pandas import read_csv
import events, shop_function, marketplace
import numpy as np

#To do
#todo Finish marketplace. Implement better items.
#todo Create a drug creation interface so players can sell something. Perhaps call it a druglab?
#todo Finish TOR.
#todo Finish item interface. Does not execute button actions ATM.
#todo Finish shop items. Do not increase income ATM.
#todo Play test?
#todo Move class events to a separete file to keep the main.py short.
#todo Make reset work better and fix for new implementations such as equipment and risk.
#todo Several functions are called from Actions through MainWindow. Should be called straight forward.


#main variables settings
minutes = 15
timelimit = minutes*60*100
timefactor = 0.003
dollarfactor = 0.01
stealthfactor = 0.2
checkTOR = False


class ScrollableLabel(ScrollView):
    text = StringProperty('')

#Main game class that keeps track of game variables
class Scoreboard(Widget):

    dollars = NumericProperty(400 + random.randint(-150,200))
    bitcoins = NumericProperty(50)
    debug = BooleanProperty(False)
    income = NumericProperty(0) #In BTC
    btc_rate = NumericProperty(300) # exchange rate in dollars
    equipment = DictProperty()
    equipment_list = StringProperty()
    notcheckTOR = BooleanProperty(not checkTOR)
    time = NumericProperty(0)
    minutes = NumericProperty(0)
    seconds = NumericProperty(0)
    stealth = NumericProperty(0)
    risk = NumericProperty(0)

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

    #loads list of events from csv, move to events class which should be moved to a separete file
    def load_events(self):
        self.list_events = read_csv('events.csv', delimiter=';')
        print("Loaded events")

    #updates the game, executes every 1/60 of a second. See MainApp at the end of this file
    def update(self, dt):
        self.t
        self.score.time=self.t
        self.score.minutes = int(self.t/6000)
        self.score.seconds = int((self.t/100)%60)

        #Risk inscrease
        self.score.risk = int((self.t * timefactor) + (self.score.dollars * dollarfactor) + (self.score.stealth * stealthfactor))


        if self.t <= timelimit:
            self.t += 1
        else:
            self.t = 0
            #endgame
            #todo implement endgame

        #Random walk for bitcoin to dollar rate. Slight bias towards increasing.
        if self.t%200 == 0:
            self.score.btc_rate = round(self.score.btc_rate+random.randint(-100,110)/10, 1)


#defines button press actions for the lower bar
#passes parent.main as the main game class to all functions so that functions can interface with the main game class
class Actions(BoxLayout):
    def exchange(self, parent):
        MainWindow.exchange(self, parent.main)

    def shop(self, parent):
        MainWindow.shop(self, parent.main)#Should be called directly not through MainWindow

    def market(self, parent):
        MainWindow.market(self,parent.main)#Should be called directly not through MainWindow

    #Debuging inteface. Right now this does not do much. Might be important for play testing
    def debug(self, parent):
        parent.score.debug = not parent.score.debug
        if parent.score.debug == True:
            parent.score.ids.debug.text = "Debugging ON \n More debugging \n information coming\n soon...\n \ntor_enabled:"+str(parent.score.tor_enabled)
        else:
            parent.score.ids.debug.text = "Debugging OFF"

    def event(self, parent):
        Events.event(self, parent)

    def restart(self, parent):
        parent.score.restart()

#event class. Should be moved to a separete file to decluter this one.
class Events(FloatLayout):
    def event(self, parent):

        events = np.genfromtxt('events.csv', delimiter=';', dtype=np.str_)
        event=events[1] #this is where the event should be chosed, default is event 1

        box=BoxLayout()
        #text = ScrollableLabel(text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus odio nisi, pellentesque molestie adipiscing vitae, aliquam at tellus. Fusce quis est ornare erat pulvinar elementum ut sed felis. Donec vel neque mauris. In sit amet nunc sit amet diam dapibus lacinia. In sodales placerat mauris, ut euismod augue laoreet at. Integer in neque non odio fermentum volutpat nec nec nulla. Donec et risus non mi viverra posuere. Phasellus cursus augue purus, eget volutpat leo. Phasellus sed dui vitae ipsum mattis facilisis vehicula eu justo.\n\n Quisque neque dolor, egestas sed venenatis eget, porta id ipsum. Ut faucibus, massa vitae imperdiet rutrum, sem dolor rhoncus magna, non lacinia nulla risus non dui. Nulla sit amet risus orci. Nunc libero justo, interdum eu pulvinar vel, pulvinar et lectus. Phasellus sed luctus diam. Pellentesque non feugiat dolor. Cras at dolor velit, gravida congue velit. Aliquam erat volutpat. Nullam eu nunc dui, quis sagittis dolor. Ut nec dui eget odio pulvinar placerat. Pellentesque mi metus, tristique et placerat ac, pulvinar vel quam. Nam blandit magna a urna imperdiet molestie. Nullam ut nisi eget enim laoreet sodales sit amet a felis.\n")
        text= ScrollableLabel(text=event[2])
        #text.bind(size=lambda s, w: s.setter('text_size')(s, w))

        layout = GridLayout(cols=1)



        option1 = Button(text=event[6], size_hint=(0.2,0.1))
        option2 = Button(text=event[8], size_hint=(0.2,0.1))
        close = Button(text='Close me!', size_hint=(0.2,0.1))
        video = Video(source='drugvideo.mp4')
        image = Image(source='currencydepreciation.jpg')


        layout.add_widget(text)
        #layout.add_widget(image)
        #layout.add_widget(video)
        layout.add_widget(option1)
        layout.add_widget(option2)
        layout.add_widget(close)
        box.add_widget(layout)


        popup = Popup(title=event[1],
                      content=box,
                      size_hint=(0.7, 0.7))


        #popup2
        box2=BoxLayout()
        layout2 = GridLayout(cols=1)
        clickme= Button(text='Click Here', size_hint=(0.1,0.1))
        layout2.add_widget(image)
        layout2.add_widget(clickme)
        box2.add_widget(layout2)
        popup2 = Popup(title=event[1],
                      content=box2,
                      size_hint=(0.7, 0.7))

        # bind the on_press event of the button to the dismiss function
        close.bind(on_press=popup.dismiss)
        clickme.bind(on_press=popup2.dismiss)

        popup.open()
        #popup2.open()


#the central 2/3 interface. Most other events and functions interface with this.
class MainWindow(BoxLayout):
    orientation = 'vertical'

    def market(self, main):
        marketplace.marketplace(self, main)#Should be called directly not through MainWindow

    #todo Perhaps also move this to a separate file?
    def exchange(self, main):
        main.clear_widgets() #clears the main window
        main.buy=0
        def on_text(instance, value):
            try:
                main.buy = float(value)
                if main.buy>0:
                    button.text = "Buy "+str(main.buy)+" BTC for "+str(main.buy*self.parent.score.btc_rate)+"$"

                elif main.buy<0:
                    button.text = "Sell " + str(-main.buy) + " BTC for " + str(-main.buy*self.parent.score.btc_rate)+"$"

            except ValueError:
                button.text = "You need to enter a number"
        def buysell(instance):
            try:
                if main.buy > 0:
                    if self.parent.score.dollars >= main.buy * self.parent.score.btc_rate:
                        buy_BTC(main.buy)
                    else:
                        button.text = "Not enough money"
                elif main.buy < 0:
                    if self.parent.score.bitcoins >= -main.buy:
                        sell_BTC(-main.buy)
                    else:
                        button.text = "Not enough BTC"
            except ValueError:
                button.text = "You need to enter a number"
        def sell_BTC(sell):
            events.change_dollars(main.parent, sell* self.parent.score.btc_rate)
            events.change_bitcoin(main.parent, -sell)
        def buy_BTC(buy):
            events.change_dollars(main.parent, -buy* self.parent.score.btc_rate)
            events.change_bitcoin(main.parent, buy)

        label = Label(text="How much BTC do you want to buy?")
        main.add_widget(label)
        textinput = TextInput(multiline=False)
        textinput.bind(text=on_text)
        main.add_widget(textinput)
        button = Button(text="0")
        button.bind(on_release=buysell)
        main.add_widget(button)

    def shop(self, main):
        shop_function.shop(self, main)#Should be called directly not through MainWindow


#Main game class and fucntion. Initialises the game.
class MainApp(App):
    def build(self):
        game = MainGame()
        game.t=0
        game.load_events()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        print("Game started.")
        return game


if __name__ == '__main__':
    MainApp().run()

