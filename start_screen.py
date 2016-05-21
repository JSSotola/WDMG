
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
import random
import main as main_file
import actions

def start(main):
    def second_intro(instance):
        popup.dismiss
        #image = Image(source="media/Intro1.png")
        #content.add_widget(image)


    content = BoxLayout(orientation='vertical')
    label = Label(text="Welcome, blabla, enter your username")

    content.add_widget(label)

    textinput = TextInput(multiline=False)
    content.add_widget(textinput)



    button = Button(text = "OK")
    content.add_widget(button)

    button.bind(on_release = second_intro)

    popup = Popup(title="",
                  content=content,
                  size_hint=(0.9, 0.9))

    # bind the on_press event of the button to the dismiss function
    #button.bind(on_press=)

    popup.open()

