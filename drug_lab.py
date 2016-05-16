#drug lab
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown




def lab(self, main):
    main.clear_widgets()  # clears the main window

    def dropdown_list(mainbutton):

        def selection(instance):
            mainbutton.text = instance.text
            check_combinations()

        # create a dropdown with 10 buttons #todo Load actual ingredients probably the ones the player has already bought
        dropdown = DropDown()
        for n in range(10):
            # when adding widgets, we need to specify the height manually (disabling
            # the size_hint_y) so the dropdown can calculate the area it needs.
            btn = Button(text='Ingredient %d' % n, size_hint_y=None, height=30)
            # for each button, attach a callback that will call the selection() method
            btn.bind(on_release=selection)
            # then add the button inside the dropdown
            dropdown.add_widget(btn)

        # show the dropdown menu when the main button is released.
        mainbutton.bind(on_release=dropdown.open)

        return mainbutton


    def check_combinations():
        result.text="Resulting drug" #todo Implement a proper resulting function


    title_text = "This is your drag lab. Create drugs from ingredients. You might want to try looking for on TOR for recipes..." #Maybe add link to some sites?
    label = Label(text=title_text, text_size=(main.width, None), size_hint = (1,0.25))
    main.add_widget(label)

    bottom_area = BoxLayout(orientation = 'horizontal')
    main.add_widget(bottom_area)

    selectors = BoxLayout(orientation = 'vertical')
    result = Label(text="", text_size=(selectors.width, None), size_hint = (1.5,1))
    confirm = Button(text = "Create") #todo Implement
    bottom_area.add_widget(selectors)
    bottom_area.add_widget(result)
    bottom_area.add_widget(confirm)

    for i in range(1,6):
        dropdown = Button(text='Select ingredient '+str(i))
        selectors.add_widget(dropdown_list(dropdown))

