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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):

    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"sorry there is not enough {item}")
            return False
    return True


def process_coins():
    """returns the total calculated"""
    print("please insert coins")
    quarters = int(input("how many quarters: ")) * 0.25
    dimes = int(input("how many dimes: ")) * 0.10
    nickles = int(input("how many nickles: ")) * 0.05
    pennies = int(input("how many pennies: ")) * 0.01
    total = quarters + dimes + nickles + pennies
    return total


def is_transaction_successful(money_received, drink_cost):

    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your {change} change")
        global profit
        profit += drink_cost
        return True
    else:
        return False


def make_coffee(drink_name, order_ingredients):

    if is_resource_sufficient(order_ingredients):
        for item in order_ingredients:
            resources[item] -= order_ingredients[item]
        print(f"here is your {drink_name}")
    else:
        print(f"cannot make {drink_name} Insufficient resources")


is_on = True


while is_on:
    choice = input("what coffee would you like espresso cappuccino or latte\n")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water:{resources['water']}ml")
        print(f"milk:{resources['milk']}ml")
        print(f"coffee{resources['coffee']}g")
        print(f"honey: ${profit}")
    else:
        drink = MENU.get(choice)
        if drink:
            if is_resource_sufficient(drink["ingredients"]):
                payment = process_coins()
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])

        else:
            print("invalid choice")
