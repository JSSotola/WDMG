#drug lab
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.spinner import Spinner
from kivy.properties import ListProperty
import actions


def lab(self, main):
    main.clear_widgets()  # clears the main window

    def check_combinations(list_ingredients):

        if ("Muriatic accid" in list_ingredients) and ("Sodium Hydroxide (NaOH)" in list_ingredients) and ("Diethyl Ether" in list_ingredients) and ("Ephedrine" in list_ingredients):
            result.text = "Methamphetamine"
        elif ("MORNING GLORY SEEDS" in list_ingredients) and ("Petroleum ether" in list_ingredients) and ("Alcohol" in list_ingredients):
            result.text = "LSD"
        elif ("sulfuric acid" in list_ingredients) and ("potassium permanganate" in list_ingredients) and ("coca paste" in list_ingredients):
            result.text = "Cocaine"
        else:
            result.text = "Incorrect combination"

    def create_drug(instance):
        if result.text == "Incorrect combination" or result.text == "":
            actions.popupmessage("The combination of ingredients is \n not correct, try looking online...")
        else:
            create = True
            for item in main.list_ingredients:
                if not main.parent.score.ingredients[item]>0:
                    create = False
                    actions.popupmessage("You do not have enough "+ str(item))

            if create:
                for item in main.list_ingredients:
                    main.parent.score.ingredients[item] -= 1
                if result.text in main.parent.score.equipment:
                    main.parent.score.equipment[result.text] += 1
                else:
                    main.parent.score.equipment[result.text] = 1
            actions.generate_equipment_list(main.parent)
            actions.generate_ingredients_list(main.parent)


    title_text = "This is your drug lab. Create drugs from ingredients. You might want to try looking on TOR for recipes..." #Maybe add link to some sites?
    label = Label(text=title_text, text_size=(main.width/1.1, None), size_hint = (1,0.25), bold=True, font_size=22)
    main.add_widget(label)

    bottom_area = BoxLayout(orientation = 'horizontal')
    main.add_widget(bottom_area)

    selectors = BoxLayout(orientation = 'vertical', padding = [10,10,10,10], spacing = 10)
    result = Label(text="", text_size=(selectors.width, None), size_hint = (1.5,1), bold=True)
    confirm = Button(text = "Create", bold=True, font_size=30, text_size=self.size, valign='middle', halign='center')
    bottom_area.add_widget(selectors)
    bottom_area.add_widget(result)
    bottom_area.add_widget(confirm)

    confirm.bind(on_release = create_drug)


    def exec_on_selection(spinner, text):
        main.parent.score.selected_ingredients[spinner.id] = text

        main.list_ingredients = []
        for item in main.parent.score.selected_ingredients:
            main.list_ingredients += [main.parent.score.selected_ingredients[item]]

        check_combinations(main.list_ingredients)#todo fix bug the argument is not the list of selected but the list of available




    if main.parent.score.ingredients == {}:
        ingredient_list = ("You need to buy", "ingredients in the", "dark market first.")
    else:
        ingredient_list =  main.parent.score.ingredients


    for i in ["first", "second", "third", "fourth", "fifth"]:
        dropdown = Spinner(
            # default value shown
            text="Select " + i +" ingredient",
            # available values
            values=ingredient_list,
            id = i, valign='middle', halign='center', bold=True, text_size=self.size)
        selectors.add_widget(dropdown)
        dropdown.bind(text = exec_on_selection)

