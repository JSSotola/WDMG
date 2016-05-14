
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from pandas import read_csv
import events
import numpy as np



def load_events():
    list_events = np.genfromtxt('shop_inventory.csv', delimiter=',', dtype=np.str_)
    print("Loaded shop")
    return list_events

def shop(self, main):
    main.clear_widgets()  # clears the main window

    #load items to shop
    main.items = load_events()


    label = Label(text="What would you like to buy?")
    main.add_widget(label)

    box = BoxLayout()
    main.add_widget(box)

    #define button press
    def pressbutton(instance):
        if events.popupconfirm("that you want to buy this") == True:
            events.change_dollars(main.parent, -np.int(main.items[np.int(instance.id),1]))

    #create buttons
    for i in range(1,main.items.shape[0]):
        item = Button(text=(main.items[i,0]+"\n"+main.items[i,1]+"$"), id=np.str_(i), text_size=(self.width/(main.items.shape[0]+2), None))
        print(main.items[i, 1].astype(int))
        item.bind(on_press=pressbutton)

        events.change_dollars(main.parent, -100)
        box.add_widget(item)
    button = Button(text="You can click here, but it does nothing.")
    main.add_widget(button)

    #TEST