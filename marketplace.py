from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import events
import numpy as np
import webbrowser

import TOR

def load_events():
    list_events = np.genfromtxt('marketplace.csv', delimiter=',', dtype=np.str_)
    print("Loaded shop")
    return list_events


def trigger(main, TOR_working):
    main.clear_widgets()  # clears the main window
    label = Label(text="The net is dark and full of errors...")
    main.add_widget(label)

    if TOR_working:

        #load items to shop
        main.items = load_events()


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


        #create buttons from csv
        for i in range(1,main.items.shape[0]):
            item = Button(text=(main.items[i,0]+"\n"+main.items[i,1]+"BTC"), id=np.str_(i), text_size=(box.width, None))

            #check whether buy or sell type and assign to the appropriate row.
            if main.items[i,3] == "1":
                item.bind(on_release=pressbutton)
                box.add_widget(item)
            else:
                box2.add_widget(item)
                item.bind(on_release=pressbutton)
    else:
        label2 = Label(text="Please install TOR in order to connect to the dark net. See https://www.torproject.org/ .")
        main.add_widget(label2)

        box = BoxLayout()
        main.add_widget(box)
        button1 = Button(text="Take me to https://www.torproject.org/ to install TOR.", text_size=(box.width*2.7, None))
        button2 = Button(text="I don't want to install anything. Just let me play the game!", text_size=(box.width*2.7, None))

        box.add_widget(button1)
        box.add_widget(button2)

        def openTORweb(instance):
            webbrowser.open("https://www.torproject.org/")
            main.clear_widgets()  # clears the main window
        button1.bind(on_release = openTORweb)

        def trigger_button2(bool):
            trigger(main, bool)
        def pressbutton(instance):
            events.popupconfirm("? Your experience of the game will be greatly diminished by this choice.", trigger_button2)
        button2.bind(on_release = pressbutton)

def marketplace(self, main):
    if main.parent.score.notcheckTOR:
        trigger(main, True)
    else:
        TOR.TOR(main, trigger)