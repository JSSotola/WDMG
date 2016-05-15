
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from pandas import read_csv
import events
import numpy as np
import time
from random import randint




def load_events():
    list_events = np.genfromtxt('shop_inventory.csv', delimiter=',', dtype=np.str_)
    print("Loaded shop")
    return list_events

def choose_event(DF_events):
    # this function chooses a random event using pandas read_csv which reads a csv into a DataFrame
    # here are some examples of how to use Dataframes

    #print(DF_events.shape[1])  or print(len(DF_events.index)) # number of entries in DF
    #print(DF_events.info()) #prints info of DF

    # print(ev[[0]]) #gives titles of all events as DF
    # print(ev[:1]) #gives first event as DF
    # print(ev.get('event_title')) #prints titles of all events as DF
    # print(ev[:1].get('event_title')) #give title of first event as DF
    # print(ev.loc[0]) #prints first events as DF
    # print(ev.loc[0].get('event_title')) # prints first event title as a string
    # print(DF_events.loc[DF_events.tail(1).get('id')].get('event_title')) #gets the event title as DF from the last event if no index column is set

    DF_len = len(DF_events.index) -1 # takes header into account so number of events is index-1
    event_number = randint(0, DF_len-1) # inclusive random integer selector
    event = DF_events.loc[event_number]
    event_title = event.get('event_title')

    print("this is the chosen event: " + event_title)

    return

def shop(self, main):
    main.clear_widgets()  # clears the main window

    #load items to shop
    main.items = load_events()

    #Title
    label = Label(text="What would you like to buy?")
    main.add_widget(label)

    #add two rows of buttons
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

        #Confirm popup which executes trigger which then buys item iff YES was selected.
        events.popupconfirm("that you want to buy this", trigger)



    #create buttons from csv
    for i in range(1,main.items.shape[0]):
        item = Button(text=(main.items[i,0]+"\n"+main.items[i,1]+"$"), id=np.str_(i), text_size=(self.width/(main.items.shape[0]+2), None))
        item.bind(on_release=pressbutton)
        if i< 6:
            box.add_widget(item)
        else:
            box2.add_widget(item)
