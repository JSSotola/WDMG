#todo Move all events functionality here

#This file contains all functionality connected to events. Importing, randomisation etc.
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, BooleanProperty, DictProperty, ReferenceListProperty, ObjectProperty
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.video import Video
from kivy.uix.image import Image
import random
from pandas import read_csv
import actions
import numpy as np
import events

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
    print(event_list)
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
    event_number = random.randint(0, DF_len-1) # inclusive random integer selector
    event = DF_events.loc[event_number]

    return event

#event class. Should be moved to a separete file to decluter this one.
class Events(FloatLayout):
    events_list = ObjectProperty(np.genfromtxt('events.csv', delimiter=';', dtype=np.str_, skip_header=1))
    def event(self, parent):
        event = choose_event(Events.events_list)


        box=BoxLayout()
        #text = ScrollableLabel(text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus odio nisi, pellentesque molestie adipiscing vitae, aliquam at tellus. Fusce quis est ornare erat pulvinar elementum ut sed felis. Donec vel neque mauris. In sit amet nunc sit amet diam dapibus lacinia. In sodales placerat mauris, ut euismod augue laoreet at. Integer in neque non odio fermentum volutpat nec nec nulla. Donec et risus non mi viverra posuere. Phasellus cursus augue purus, eget volutpat leo. Phasellus sed dui vitae ipsum mattis facilisis vehicula eu justo.\n\n Quisque neque dolor, egestas sed venenatis eget, porta id ipsum. Ut faucibus, massa vitae imperdiet rutrum, sem dolor rhoncus magna, non lacinia nulla risus non dui. Nulla sit amet risus orci. Nunc libero justo, interdum eu pulvinar vel, pulvinar et lectus. Phasellus sed luctus diam. Pellentesque non feugiat dolor. Cras at dolor velit, gravida congue velit. Aliquam erat volutpat. Nullam eu nunc dui, quis sagittis dolor. Ut nec dui eget odio pulvinar placerat. Pellentesque mi metus, tristique et placerat ac, pulvinar vel quam. Nam blandit magna a urna imperdiet molestie. Nullam ut nisi eget enim laoreet sodales sit amet a felis.\n")
        text= ScrollableLabel(text=event.get('event_text'))
        #text.bind(size=lambda s, w: s.setter('text_size')(s, w))

        layout = GridLayout(cols=1)
        layout.add_widget(text)

        if isinstance(event.get('option_1_text'), str):
            option1 = Button(text=event.get('option_1_text'), size_hint=(0.2,0.1))
            layout.add_widget(option1)
        else: pass

        if isinstance(event.get('option_2_text'), str):
            option2 = Button(text=event.get('option_2_text'), size_hint=(0.2,0.1))
            layout.add_widget(option2)
        else:
            pass
        close = Button(text='There is nothing you can do. Close me!', size_hint=(0.2,0.1))
        layout.add_widget(close)


        #video = Video(source='drugvideo.mp4')
        #image = Image(source='currencydepreciation.jpg')
        # layout.add_widget(image)
        # layout.add_widget(video)


        box.add_widget(layout)


        popup = Popup(title=event.get('event_title'),
                      content=box,
                      size_hint=(0.7, 0.7))


        # popup2
        # box2=BoxLayout()
        # layout2 = GridLayout(cols=1)
        # clickme= Button(text='Click Here', size_hint=(0.1,0.1))
        # layout2.add_widget(image)
        # layout2.add_widget(clickme)
        # box2.add_widget(layout2)
        # popup2 = Popup(title=event[1],
        #               content=box2,
        #               size_hint=(0.7, 0.7))

        # bind the on_press event of the button to the dismiss function
        close.bind(on_press=popup.dismiss)
        # clickme.bind(on_press=popup2.dismiss)

        popup.open()
        # popup2.open()