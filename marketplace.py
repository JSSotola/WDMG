#This is where the marketplace gets defined.

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import actions
import numpy as np
import webbrowser

import TOR

def load_events():
    list_events = np.genfromtxt('marketplace.csv', delimiter=',', dtype=np.str_)
    print("Loaded shop")
    return list_events


def trigger(main, TOR_working):
    main.clear_widgets()  # clears the main window
    label = Label(text="The net is dark and full of errors...", bold=True, font_size=20)
    main.add_widget(label)

    if TOR_working:

        #load items to shop
        main.items = load_events()


        box = BoxLayout()
        box2 = BoxLayout()
        box_drugs = BoxLayout()
        main.add_widget(box)
        main.add_widget(box2)
        main.add_widget(box_drugs)
        sell_label = Label(text="Drugs in demand:", bold=True)
        buy_label = Label(text="Ingredients\nfor\nsale:", bold=True, halign = 'center')

        box.add_widget(buy_label)
        box_drugs.add_widget(sell_label)

        #define button press
        def buy_ingredient(instance):
            bought = actions.change_bitcoin(main.parent, -float(main.items[float(instance.id), 1]))
            if bought:
                if main.items[instance.id,0] in main.parent.score.ingredients:
                    main.parent.score.ingredients[main.items[instance.id, 0]] += 1
                    actions.generate_ingredients_list(main.parent)

                else:
                    main.parent.score.ingredients[main.items[instance.id, 0]] = 1
                    actions.generate_ingredients_list(main.parent)

        def sell_drug(instance):
            #check if item in inventory
            if main.items[instance.id, 0] in main.parent.score.equipment:
                if main.parent.score.equipment[main.items[instance.id, 0]]>0:
                    main.parent.score.equipment[main.items[instance.id, 0]] -= 1
                    actions.change_bitcoin(main.parent, float(main.items[float(instance.id), 1]))
                    actions.generate_equipment_list(main.parent)
                else:
                    actions.popupmessage("You do not have this drug, hence you cannot sell it.")
            else:
                actions.popupmessage("You do not have this drug, hence you cannot sell it.")





        #create buttons from csv
        n=0 #dummy
        for i in range(1,main.items.shape[0]):
            main.items[i, 1] = str(round(float(main.items[i, 1]) / main.parent.score.btc_rate, 2)) # convert to BTC at the current rate
            item = Button(text=(main.items[i,0]+"\n"+main.items[i, 1]+"BTC"), id=np.str_(i), text_size=box.size, bold=True, halign='center', valign='middle')

            #check whether buy or sell type and assign to the appropriate row.
            if main.items[i,3] == "1" and n < 5:
                item.bind(on_release=buy_ingredient)
                box.add_widget(item)
                n+=1
            elif main.items[i,3] == "1" and n >= 5:
                item.bind(on_release=buy_ingredient)
                box2.add_widget(item)
                n+=1
            else:
                box_drugs.add_widget(item)
                item.bind(on_release=sell_drug)
    else:
        label2 = Label(text="Please install TOR in order to connect to the dark net. See https://www.torproject.org/ .", bold=True)
        main.add_widget(label2)

        box = BoxLayout()
        main.add_widget(box)
        button1 = Button(text="Take me to https://www.torproject.org/ to install TOR.", text_size=(box.width*2.7, None), bold=True)
        button2 = Button(text="I don't want to install anything. Just let me play the game!", text_size=(box.width*2.7, None), bold=True)

        box.add_widget(button1)
        box.add_widget(button2)

        def openTORweb(instance):
            webbrowser.open("https://www.torproject.org/")
            main.clear_widgets()  # clears the main window
        button1.bind(on_release = openTORweb)

        def trigger_button2(bool):
            trigger(main, bool)
        def pressbutton2(instance):
            actions.popupconfirm("? Your experience of the game will be greatly diminished by this choice.", trigger_button2)
        button2.bind(on_release = pressbutton2)

def marketplace(self, main):
    if main.parent.score.notcheckTOR:
        trigger(main, True)
    else:
        TOR.TOR(main, trigger)