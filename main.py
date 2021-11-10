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


def sufficient_resources(order_ingredients):
    """Returns a boolean representing sufficent resources to make the ordered drink."""
    sufficient = True  # we could just return 'False' or 'True' on 40 + 41 w/o naming 'sufficient'
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return sufficient


def count_money():
    """Returns the total amount of money given to the machine."""
    print("Please insert money.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(user_input_money, drink_cost):
    """Returns a bool representing if money for transaction is sufficient"""
    if user_input_money >= drink_cost:
        change = round(user_input_money - drink_cost, 2)
        print(f"Here is ${change} in change.")
        # this "brings in" the money_collected variable and allows for manipulation.
        global money_collected
        money_collected += drink_cost
        return True
    else:
        print("Sorry that is not enough money. Your money has been refunded.")
        return False


def make_drink(drink_name, drink_resource_cost):
    """Deduct resources from the machine to make specified drink."""
    for item in drink_resource_cost:
        resources[item] -= drink_resource_cost[item]
    print(f"Here is your {drink_name}")


money_collected = 0
power_state = True

while power_state:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "off":
        power_state = False
    elif order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money_collected}")
    else:
        drink = MENU[order]
        if sufficient_resources(drink["ingredients"]):
            payment = count_money()
            is_transaction_successful(payment, drink["cost"])
            make_drink(order, drink["ingredients"])
