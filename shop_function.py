
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from pandas import read_csv
import events
import numpy as np
import time



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
    box2 = BoxLayout()
    main.add_widget(box)
    main.add_widget(box2)

    #define button press
    def pressbutton(instance):

        def trigger(confirm):
            if confirm:
                bought = events.change_dollars(main.parent, -np.int(main.items[np.int(instance.id), 1]))
                if bought:
                    if main.items[instance.id,0] in main.parent.score.equipment:
                        main.parent.score.equipment[main.items[instance.id, 0]] += 1
                        events.generate_equipment_list(main.parent)
                    else:
                        main.parent.score.equipment[main.items[instance.id, 0]] = 1
                        events.generate_equipment_list(main.parent)
            else:
                print("No selected")

        events.popupconfirm("that you want to buy this", trigger)



    #create buttons
    for i in range(1,main.items.shape[0]):
        item = Button(text=(main.items[i,0]+"\n"+main.items[i,1]+"$"), id=np.str_(i), text_size=(self.width/(main.items.shape[0]+2), None))
        item.bind(on_release=pressbutton)
        if i< 6:
            box.add_widget(item)
        else:
            box2.add_widget(item)
