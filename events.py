from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
import time


def popupconfirm(text, trigger):
    def returntrue(instance):
        trigger(True)


    def returnfalse(instance):
        trigger(False)


    content = BoxLayout(orientation='vertical')
    popup = Popup(title='Confirmation',
                  content=content,
                  size_hint=(0.5, 0.3))

    label_top = Label(text='Are you sure ' + text)
    buttons = BoxLayout(orientation='horizontal')

    yes_button = Button(text="Yes")
    yes_button.bind(on_press=returntrue)
    yes_button.bind(on_release=popup.dismiss)
    no_button = Button(text="No")
    no_button.bind(on_release=returnfalse)
    no_button.bind(on_release=popup.dismiss)

    buttons.add_widget(yes_button)
    buttons.add_widget(no_button)

    content.add_widget(label_top)
    content.add_widget(buttons)

    popup.open()


def popupmessage(text):
    content = BoxLayout(orientation='vertical')
    label = Label(text=text)
    button = Button(text = "OK")
    content.add_widget(label)
    content.add_widget(button)
    popup = Popup(title="",
                  content=content,
                  size_hint=(0.3, 0.5))

    # bind the on_press event of the button to the dismiss function

    button.bind(on_press=popup.dismiss)

    popup.open()


#Function randomly determines whether you are arrested, or get to walk free.
def cointoss(probability):
    pass


#Can be used to either increase or decrease player's amount of bitcoin
def change_bitcoin(self, amount, notcheckzero=False):
    if self.score.bitcoins < -amount and notcheckzero==False:
        popupmessage("Not enough Bitcoin!")
        return False
    else:
        self.score.bitcoins += amount
        return True
    
#Can be used to either increase or decrease player's amount of dollars.
def change_dollars(self, amount, notcheckzero=False):
    if self.score.dollars < -amount and notcheckzero == False:
        popupmessage("Not enough money!")
        return False
    else:
        self.score.dollars += amount
        return True
def generate_equipment_list(self):
    self.score.equipment_list = "Items: \n"
    for i in self.score.equipment.keys():
        self.score.equipment_list += str(i)+ ': ' +str(self.score.equipment[i])+ "\n"
#Used to change gamestate to arrested state
def arrested():
    pass

#Used to change gamestate to dead state (endgame)
def killed():
    pass

