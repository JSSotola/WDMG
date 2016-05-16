from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import actions


def exchange(self, main):
    main.clear_widgets()  # clears the main window
    main.buy = 0

    def on_text(instance, value):
        try:
            main.buy = float(value)
            if main.buy > 0:
                button.text = "Buy " + str(main.buy) + " BTC for " + str(main.buy * self.parent.score.btc_rate) + "$"

            elif main.buy < 0:
                button.text = "Sell " + str(-main.buy) + " BTC for " + str(-main.buy * self.parent.score.btc_rate) + "$"

        except ValueError:
            main.buy = 0
            button.text = "You need to enter a number"

    def buysell(instance):
        try:
            if main.buy > 0:
                if self.parent.score.dollars >= main.buy * self.parent.score.btc_rate:
                    buy_BTC(main.buy)
                else:
                    button.text = "Not enough money"
            elif main.buy < 0:
                if self.parent.score.bitcoins >= -main.buy:
                    sell_BTC(-main.buy)
                else:
                    button.text = "Not enough BTC"
        except ValueError:
            button.text = "You need to enter a number"

    def sell_BTC(sell):
        actions.change_dollars(main.parent, sell * self.parent.score.btc_rate)
        actions.change_bitcoin(main.parent, -sell)

    def buy_BTC(buy):
        actions.change_dollars(main.parent, -buy * self.parent.score.btc_rate)
        actions.change_bitcoin(main.parent, buy)

    label = Label(text="How much BTC do you want to buy?")
    main.add_widget(label)
    textinput = TextInput(multiline=False)
    textinput.bind(text=on_text)
    main.add_widget(textinput)
    button = Button(text="0")
    button.bind(on_release=buysell)
    main.add_widget(button)