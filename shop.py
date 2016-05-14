from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, BooleanProperty, DictProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import random
from pandas import read_csv
import time
import events
import shop

def shop(self, main):
    main.clear_widgets()  # clears the main window
    label = Label(text="What would you like to buy?")
    main.add_widget(label)

    box = BoxLayout()
    main.add_widget(box)
    for i in range(5):
        item = Button(text="Item " + str(i))
        box.add_widget(item)
    button = Button(text="You can click here, but it does nothing.")
    main.add_widget(button)