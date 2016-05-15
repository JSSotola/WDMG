pass

#Needs to be implemented. See TOR_temp.py

from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


#if main.parent.score.tor_enabled == False:
#
#    def addwidgetlabel1(self):
#        main.add_widget(label1)
#
#
#    # shouldbe just one function. This is a workaround. Figure out how to pass something to callback in Clock.schedule
#    def addwidgetlabel2(self):
#        main.add_widget(label2)
#
#
#    def addwidgetlabel3(self):
#        main.add_widget(label3)
#
#
#    main.clear_widgets()
#    label1 = Label(text="Connecting...")
#    Clock.schedule_once(addwidgetlabel1, 0.1)
#    label2 = Label(text="Error. Retrying...")
#    Clock.schedule_once(addwidgetlabel2, 0.7)
#
#    label3 = Label(text="Connection failed: You need to install TOR in order to connect to the dark markets.")
#    Clock.schedule_once(addwidgetlabel3, 1.5)
#else:
#    pass
#    # here market code will go