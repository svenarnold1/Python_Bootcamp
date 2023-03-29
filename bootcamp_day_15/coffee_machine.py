# This is a coffee machine that contains tree hot flavours.
# Only $ in cash are accepted.

from coffee_recipe import MENU, resources


def report():
    """returns the resources left inside of coffee machine"""
    return f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml" \
           f" \nCoffee: {resources['coffee']}g \nMoney: ${money_inside}"


def check_resources(coffee):
    """checks if all the resources needed are available inside of coffee machine"""
    if MENU[coffee]['ingredients']['water'] > resources['water']:
        return "Sorry there is not enough water"
    else:
        if MENU[coffee]['ingredients']['coffee'] > resources['coffee']:
            return "Sorry there is not enough coffee"
        else:
            if coffee != 'espresso' and MENU[coffee]['ingredients']['milk'] > resources['milk']:
                return "Sorry there is not enough milk"
            else:
                return 0


def insert_coins():
    """returns amount of cash user put in"""
    print("Please insert coins")
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickles = int(input("How many nickles: "))
    pennies = int(input("How many pennies: "))
    return 0.25*quarters + 0.1*dimes + 0.05*nickles + 0.01*pennies


def reduce_resources(coffee):
    resources['water'] -= MENU[coffee]['ingredients']['water']
    resources['coffee'] -= MENU[coffee]['ingredients']['coffee']
    if coffee != 'espresso':
        resources['milk'] -= MENU[coffee]['ingredients']['milk']


money_inside = 0
cash = 0
should_continue = True
while should_continue:
    # ask what coffee user wants.
    flavour = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # enable turn off and report
    if flavour == 'report':
        print(report())
    elif flavour == 'off':
        should_continue = False
    else:
        # if enough resources, continue
        if check_resources(flavour) == 0:
            # process coins.
            cash = insert_coins()
            price = MENU[flavour]['cost']

            print(f"cash: {cash} price: {price}")
            if cash == price:
                money_inside += price
                print(f"Here is your {flavour} ☕. Enjoy!")
                reduce_resources(flavour)
            elif cash > price:
                refund = round(cash - price, 2)
                money_inside += price
                print(f"Here is ${refund} in change.\nHere is your {flavour} ☕. Enjoy!")
                reduce_resources(flavour)
            else:
                cash = 0
                print("Sorry that's not enough money. Money refunded.")
        else:
            print(check_resources(flavour))

# EoF (End of File)
