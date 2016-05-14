
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from pandas import read_csv


def load_events():
    self.list_events = read_csv('shop_inventory.csv', delimiter=';')
    print("Loaded shop")


def shop(self, main):
    main.clear_widgets()  # clears the main window

    #load items to shop
    shop.items = load_events()

    label = Label(text="What would you like to buy?")
    main.add_widget(label)

    box = BoxLayout()
    main.add_widget(box)
    for i in range(5):
        item = Button(text="Item " + str(i))
        box.add_widget(item)
    button = Button(text="You can click here, but it does nothing.")
    main.add_widget(button)

    #TEST