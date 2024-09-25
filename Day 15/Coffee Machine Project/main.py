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
}


def print_report():
    pass




def process_coins():
    total = 0
    print("Please insert coins.")
    total += int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01

    return total


def check_cost():
    payment = process_coins()
    for drink, details in MENU.items():
        if payment >= details["cost"]:
            money = round(payment - details["cost"], 2)
            resources["money"] = money
            resources["water"] -= details["ingredients"]["water"]
            resources["coffee"] -= details["ingredients"]["coffee"]
            #resources["milk"] -= details["ingredients"]["milk"]
            print(f"Here is ${money}")
            print(f"Here is your {drink}. Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded.")

def check_against_resources():
    pass

#prompt should show every time action has completed
prompt = True

while prompt:
    choice = input("What would you like? (espresso/latte/cappuccino): ")


    #maintainers of the machine can shut down the machine by using 'off'
    if choice == 'off':
        sys.exit()


    if choice == 'report':
        print(resources)


    if choice == 'espresso':
        check_cost()

        #     #check ingredients against resources
        #     #if not enough resources, "Sorry there is not enough {resources}."



    # prompt the user to insert coins
    #quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    #calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
    #pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52


    #if enough money, resources gets updated with the profit and next time asking for a report the money will show up,
    # other resources get updated
    #if too much money inserted, the user gets refunded
    #if not enough money, "Sorry that's not enough money. Money refunded."

















