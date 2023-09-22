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
public_menu = {
    "espresso" : "1.5$",
    "latte" : "2.5$",
    "capuccino" : "3.0$"

}


profit = 0
resources = {
    "water": 200,
    "milk": 200,
    "coffee": 100,
}
# 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
def order():
    order = input("What would you like? (espresso/latte/cappuccino): ")
    return order

def check_resources(order_tbchecked):
   for item in order_tbchecked:
        if order_tbchecked[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
   return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input( "how many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change, {change}$")
        global profit
        profit = profit + drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    """Make the coffee when ingredients and payments was successfull"""
    for item in order_ingredients: 
        resources[item] -= order_ingredients[item]
    print(f"Here is your coffee!")


is_on = True
while is_on:
    print("//////")
    for _ in public_menu:
        print(f"{_}: {public_menu[_]}")
    print("//////")
    prompt = order()
    if prompt == "off":
        is_on = False
    elif prompt == "report":        
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[prompt] #en nuestro main hashmap utiiliza nuestro prompt como llave. 
        #drink tiene la bebida para manejarla  
        if check_resources(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(prompt, drink["ingredients"]) #drink es la bebida, ingredients para iterar en ese hashmap
