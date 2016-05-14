
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


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