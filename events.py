
#This file contains all functionality connected to events. Importing, randomisation etc.

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.video import Video
from kivy.uix.image import Image
import random
import actions #do not remove! Is used even though not higleghted, because the use is in an exec() function as a string.
import numpy as np


#used for scrollabel text
Builder.load_string('''
<ScrollableLabel>:
    Label:
        size_hint_y: None
        height: self.texture_size[1]
        text_size: self.width, None
        text: root.text
''')
class ScrollableLabel(ScrollView):
    text = StringProperty('')


def choose_event(event_list):
    events_len = event_list.shape[0]-1 #zero indexed
    event_number = random.randint(0, events_len) # inclusive random integer selector
    event = event_list[event_number, :]
    return event

#event class. Should be moved to a separete file to decluter this one.
class Events(FloatLayout):
    events_list = np.genfromtxt('events.csv', delimiter=';', dtype=np.str_, skip_header=1)[:,1:]
    column_names = events_list[0,:]
    for i in range(column_names.shape[0]):
        exec(column_names[i]+ "=" +str(i))
    events_list = events_list[1:,:]
    def event(self, main):
        event = choose_event(Events.events_list)

        box=BoxLayout()
        layout = GridLayout(cols=1)
        box.add_widget(layout)

        text= ScrollableLabel(text=event[Events.event_text]+"\n"+event[Events.event_effect])
        layout.add_widget(text)

        if event[Events.media_type] == "image":
            image = Image(source="media/"+event[Events.media])
            layout.add_widget(image)
        elif event[Events.media_type] == "video":
            pass
        popup = Popup(title=event[Events.event_title], content=box, size_hint=(0.7, 0.7), auto_dismiss = False)
        popup.open()

        def option_click(main, option, arg):
            if not option == "" and not arg == "":
                print(option, arg)
                exec("actions"+"."+option+"(main, "+arg+")")
            popup.dismiss()

        option1 = Button(text=event[Events.option_1_text], size_hint=(0.2, 0.1))
        layout.add_widget(option1)
        option1.bind(on_release = lambda dt: option_click(main, event[Events.option_1_do], event[Events.option_1_arg]))

        if not event[Events.option_2_text] == "":
            option2 = Button(text=event[Events.option_2_text], size_hint=(0.2, 0.1))
            layout.add_widget(option2)
            option2.bind(on_release=lambda dt: option_click(main, event[Events.option_2_do], event[Events.option_2_arg]))






