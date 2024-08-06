from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()


is_on = True
while is_on:
    user_choice = input(f"What would you like? {menu.get_items()}:  ")
    if user_choice == "report":
        coffeMaker.report()
        moneyMachine.report()
    elif user_choice == "off":
        is_on = False
    else:
        drink = menu.find_drink(user_choice)
        if coffeMaker.is_resource_sufficient(drink):
            money_needed = drink.cost
            if moneyMachine.make_payment(money_needed):
                coffeMaker.make_coffee(drink)
#

