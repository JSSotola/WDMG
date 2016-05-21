
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

def zero_intro(main):
    content = BoxLayout(orientation='vertical')
    image = Image(source="media/TOKopening.jpg")
    content.add_widget(image)

    popup = Popup(title="",
                  content=content,
                  size_hint=(1, 1))

    button = Button(text="START", size_hint = (1,0.1), bold=True, font_size=40)
    content.add_widget(button)
    button.bind(on_press=popup.dismiss)



    # bind the on_press event of the button to the dismiss function
    #button.bind(on_press=)

    popup.open()

def first_intro(main):
    content = BoxLayout(orientation='vertical')
    label = Label(text=
                       " You are to fulfill our quest, \n To see which Knight will be our best."
                       "\n What quest, you ask? Well, click around! \n There are many treasures to be found. "
                        "\n Wisdom, pleasure, or perhaps some gold "
                        "\n and many souls that may be sold."
                        "\n The largest pile of gold will win"
                        "\n While losers rot away in sin."
                        "\n \n Be careful! Heed her many terrors!"
                        "\n The Net is dark and full of errors..."
                       "\n \n Created by: \n S. Bisseling \n A. Dispenza \n D. Langerveld \n J. S. Sotola"
                        "\n \n You have 15 minutes. Anywhere you click can and will be used against you. ",
                        size_hint = (1,0.9), font_size=20, bold=True)
    content.add_widget(label)

    popup = Popup(title="Welcome to our game, sweet Onion Knight!",
                  content=content,
                  size_hint=(1, 1))

    button = Button(text="START", size_hint = (1,0.1), bold=True, font_size=40)
    content.add_widget(button)
    button.bind(on_press=popup.dismiss)



    # bind the on_press event of the button to the dismiss function
    #button.bind(on_press=)

    popup.open()


def second_intro(username):
    content = BoxLayout(orientation='vertical')
    label = Label(text="Greetings "+username+"!", size_hint = (1,0.1), font_size=20, bold=True)
    content.add_widget(label)
    image = Image(source="media/Intro.png")
    content.add_widget(image)

    popup = Popup(title="",
                  content=content,
                  size_hint=(0.9, 0.9))

    button = Button(text = "OK", size_hint = (1,0.1))
    content.add_widget(button)
    button.bind(on_press = popup.dismiss)



    # bind the on_press event of the button to the dismiss function
    #button.bind(on_press=)

    popup.open()


def start(main):
    content = BoxLayout(orientation='vertical')
    label = Label(text="Howdy partner!\n"
                       "the pied piper dark net market has just opened its doors and is looking for vendors!\n"
                       "Would you like to embark on a journey filled with encryption,\n"
                       "drugs, and most importantly, some sweet, sweet, bitcoins? then join pied piper!\n"
                       "if you join us now, you will not have to pay a vendor-subscription fee.\n"
                       "This is a limited time offer, so open up your tor browser, \n"
                       "and go to http://piedpipermkzskura.onion/home.php !\n"
                       "If you need help with anything at all please do not hesitate to ask. yours faithfully\n"
                       "pied piper team.")
    content.add_widget(label)
    box = BoxLayout(orientation = 'horizontal', size_hint = (1, 0.1))

    box.add_widget(Label(text="Enter your username:"))

    textinput = TextInput(multiline=False)
    box.add_widget(textinput)
    content.add_widget(box)

    content.add_widget(Label(text="", size_hint = (1, 0.1)))

    popup = Popup(title="You've got mail!",
                  content=content,
                  size_hint=(0.9, 0.9))

    button = Button(text = "OK", size_hint = (1, 0.1))
    content.add_widget(button)
    button.bind(on_release = lambda dt: second_intro(textinput.text))
    button.bind(on_press = popup.dismiss)



    # bind the on_press event of the button to the dismiss function
    #button.bind(on_press=)

    popup.open()
    first_intro(main)
    zero_intro(main)
