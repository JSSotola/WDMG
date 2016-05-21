#drug lab
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.spinner import Spinner
from kivy.properties import ListProperty



def lab(self, main):
    main.clear_widgets()  # clears the main window

    def check_combinations(dict_ingredients):
        result.text="Resulting drug" #todo Implement a proper resulting function


    title_text = "This is your drug lab. Create drugs from ingredients. You might want to try looking on TOR for recipes..." #Maybe add link to some sites?
    label = Label(text=title_text, text_size=(main.width/1.1, None), size_hint = (1,0.25), bold=True, font_size=22)
    main.add_widget(label)

    bottom_area = BoxLayout(orientation = 'horizontal')
    main.add_widget(bottom_area)

    selectors = BoxLayout(orientation = 'vertical', padding = [10,10,10,10], spacing = 10)
    result = Label(text="", text_size=(selectors.width, None), size_hint = (1.5,1))
    confirm = Button(text = "Create") #todo Implement
    bottom_area.add_widget(selectors)
    bottom_area.add_widget(result)
    bottom_area.add_widget(confirm)



    def exec_on_selection(spinner, text):
        print('The spinner', spinner, 'have text', text)
        main.parent.score.selected_ingredients[spinner.id] = text
        check_combinations(main.parent.score.selected_ingredients)




    if main.parent.score.ingredients == {}:
        ingredient_list = ("You need to buy", "ingredients in the", "dark market first.")
    else:
        ingredient_list =  main.parent.score.ingredients


    for i in ["first", "second", "third", "fourth", "fifth"]:
        dropdown = Spinner(
            # default value shown
            text="Select " + i +" ingredient",
            # available values
            values=ingredient_list,#todo add actual drugs, load it from what the player bought
            id = i, )
        selectors.add_widget(dropdown)
        dropdown.bind(text = exec_on_selection)

