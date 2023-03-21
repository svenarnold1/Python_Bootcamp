# This is a coffee machine that contains tree hot flavours.
# Only $ in cash are accepted.

from coffee_recipe import MENU, resources

money = 0
flavour = input("What would you like? (espresso/latte/cappuccino): ").lower()


def report():
    """returns the resources left inside of coffee machine"""
    return f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml" \
           f" \nCoffee: {resources['coffee']}g \nMoney: ${cash}"


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
    resources['water'] -= MENU[flavour]['ingredients']['water']
    resources['milk'] -= MENU[coffee]['ingredients']['milk']
    resources['coffee'] -= MENU[coffee]['ingredients']['coffee']


# TODO 2. Turn off the Coffee Machine by entering “off” to the prompt.


if flavour == 'report':
    print(report())


# TODO 4. Check resources sufficient?
# need to consider that 'report' creates a bug here!
if check_resources(flavour) == 0:
    # TODO 5. Process coins.
    cash = insert_coins()
    price = MENU[flavour]['cost']

    print(f"cash: {cash} price: {price}")
    if cash == price:
        print("Here is your {coffee}. Enjoy!")
        reduce_resources(flavour)
    elif cash > price:
        refund = cash - price
        print(f"Here is ${refund} in change.")
        reduce_resources(flavour)
    else:
        print("Sorry that's not enough money. Money refunded.")
else:
    print(check_resources(flavour))

