import sys

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money" : 0
}


def retrieve_drink_cost(drink):
    cost = MENU[drink]["cost"]
    return cost


def process_coins():
    """Returns the total calculated from coins inserted."""
    total = 0
    print("Please insert coins.")
    total += int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01

    return total


def check_cost_and_update_resources(drink):
    """Checks if inserted money is sufficient and deducts the required ingredients from the resources."""
    payment = process_coins()
    drink_cost = retrieve_drink_cost(drink)

    if payment >= drink_cost:
        money = round(drink_cost, 2)
        refund = round(payment - MENU[drink]["cost"], 2)
        resources["money"] += money
        resources["water"] -= MENU[drink]["ingredients"]["water"]
        resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]

        if "milk" in MENU[drink]["ingredients"]:
            resources["milk"] -= MENU[drink]["ingredients"]["milk"]

        print(f"Here is ${refund}")
        print(f"Here is your {drink}. Enjoy!")

    else:
        print("Sorry that's not enough money. Money refunded.")


def check_against_resources(drink):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in MENU[drink]["ingredients"]:
        if resources[item] < MENU[drink]["ingredients"][item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    #maintainers of the machine can shut down the machine by using 'off'
    if choice == 'off':
        sys.exit()

    if choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
        continue

    if choice == 'espresso':
        if check_against_resources(choice):
            check_cost_and_update_resources(choice)

    elif choice == 'latte':
        if check_against_resources(choice):
            check_cost_and_update_resources(choice)

    elif choice == 'cappuccino':
        if check_against_resources(choice):
            check_cost_and_update_resources(choice)

    else:
        print("Choose a valid drink.")
