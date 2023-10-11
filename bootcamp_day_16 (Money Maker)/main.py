from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# This is the same coffee machine as in day 15 considering OOP!
# Blue prints were given

# print report
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

# check resources sufficient.
should_continue = True
while should_continue:
    # print options and ask for choice.
    options = menu.get_items()
    choice = input(f"What would you like? ({options}):\n").lower()
    if choice == 'off':
        print('coffee machine turned off!')
        should_continue = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        # returns true if all necessary ingredients are available.
        approved = coffee_maker.is_resource_sufficient(menu.find_drink(choice))
        # searches menu for particular drink and returns it.
        drink = menu.find_drink(choice)
        print(menu.find_drink(choice))
        # make coffee if enough coins been inserted and resources efficient, else refund money and serve next costumer.
        if approved and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

# Eof (End of File)


