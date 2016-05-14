from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import events
import numpy as np

import TOR

def load_events():
    list_events = np.genfromtxt('marketplace.csv', delimiter=',', dtype=np.str_)
    print("Loaded shop")
    return list_events

def marketplace(self, main):
    TOR
    main.clear_widgets()  # clears the main window

    #load items to shop
    main.items = load_events()


    label = Label(text = "The net is dark and full of errors...")
    main.add_widget(label)

    box = BoxLayout()
    box2 = BoxLayout()
    main.add_widget(box)
    main.add_widget(box2)

    #define button press
    def pressbutton(instance):


        bought = events.change_bitcoin(main.parent, -float(main.items[float(instance.id), 1]))
        if bought:
            if main.items[instance.id,0] in main.parent.score.equipment:
                main.parent.score.equipment[main.items[instance.id, 0]] += 1
                events.generate_equipment_list(main.parent)
            else:
                main.parent.score.equipment[main.items[instance.id, 0]] = 1
                events.generate_equipment_list(main.parent)


    #create buttons
    for i in range(1,main.items.shape[0]):
        item = Button(text=(main.items[i,0]+"\n"+main.items[i,1]+"BTC"), id=np.str_(i), text_size=(self.width/(main.items.shape[0]+2), None))
        item.bind(on_release=pressbutton)

        if main.items[i,3] == "1":
            box.add_widget(item)
        else:
            box2.add_widget(item)
