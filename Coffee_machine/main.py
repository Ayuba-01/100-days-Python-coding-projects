from menu import *


profit = 0


def get_report(resources, profit):
    """Take the machine resources and the profit to return the machine report."""
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    return f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: {profit}"


def check_drink_resources(order_ingredient):
    """Takes the ordered drink ingredient to return False if the machine has less resources and True if there are enough
    recourses."""
    for item in order_ingredient:
        if resources[item] < order_ingredient[item]:
            print(f"Sorry there is not enough {item} to make your drink.")
            return False
    return True


def process_coin(quarters, dimes, nickles, pennies):
    """Process the user coin input and return the total amount of money in"""
    processed_quarter = quarters * 0.25
    processed_dimes = dimes * 0.10
    processed_nickles = nickles * 0.05
    processed_pennies = pennies * 0.01
    money_in = processed_quarter + processed_dimes + processed_nickles + processed_pennies
    return float(f"{money_in:.2f}")


def check_transaction(money_in, money_needed):
    """Take user money_in and the money_needed for the drink to return True if the user has enough money and False if
    user has less money """
    if money_in < money_needed:
        print(f"Sorry you don't have enough money. ${money_in} refunded")
        return False
    elif money_in >= money_needed:
        return True


def deduct_resources(order_ingredient):
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    return resources


is_on = True
while is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "report":
        print(get_report(resources, profit))
    elif user_choice == "off":
        is_on = False
    else:
        drink = MENU[user_choice]
        if check_drink_resources(drink["ingredients"]):
            print("Please insert coins.")
            quarters = int(input("How many quarters: "))
            dimes = int(input("How many dimes: "))
            nickles = int(input("How many nickles: "))
            pennies = int(input("How many pennies: "))
            money_in = process_coin(quarters, dimes, nickles, pennies)
            money_needed = drink["cost"]
            if check_transaction(money_in, money_needed):
                change = money_in - money_needed
                profit += money_needed
                print(f"Here is ${change:.2f} dollars in change")
                resources = deduct_resources(drink["ingredients"])
                print(f"Here is your {user_choice} ☕️. Enjoy!")




