from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup


#Function randomly determines whether you are arrested, or get to walk free.
def cointoss(probability):
    pass


#Can be used to either increase or decrease player's amount of bitcoin
def change_bitcoin(self, amount, notcheckzero=False):
    if self.score.bitcoins < -amount and notcheckzero==False:
     print("EROROR less than zero") # should be a popup
    else:
        self.score.bitcoins += amount

    
#Can be used to either increase or decrease player's amount of dollars.
def change_dollars(self, amount, notcheckzero=False):
    if self.score.dollars < -amount and notcheckzero == False:
        print("EROROR less than zero")  # should be a popup
    else:
        self.score.dollars += amount


#Used to change gamestate to arrested state
def arrested():
    pass

#Used to change gamestate to dead state (endgame)
def killed():
    pass

def popupconfirm(text):
    def returntrue(instace):
        return True
    def returnfalse(instance):
        return False
    content = BoxLayout(orientation = 'vertical')
    popup = Popup(title='Confirmation',
                  content=content,
                  size_hint=(0.5, 0.3))

    label_top = Label(text='Are you sure '+ text)
    buttons = BoxLayout(orientation = 'horizontal')
    yes_button = Button(text = "Yes")
    yes_button.bind(on_press=returntrue)
    yes_button.bind(on_release=popup.dismiss)
    no_button = Button(text = "No")
    no_button.bind(on_release=returnfalse)

    buttons.add_widget(yes_button)
    buttons.add_widget(no_button)
    content.add_widget(label_top)
    content.add_widget(buttons)
    # bind the on_press event of the button to the dismiss function

    #buttons.yes_button.bind(on_press=popup.dismiss)
    popup.open()

