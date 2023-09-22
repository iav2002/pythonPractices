from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from draw import logo
coffee_maker = CoffeeMaker() #Creacion de Objetos (acceso a las clases)
money_machine = MoneyMachine() #para usar, metodos o atributos
menu = Menu() 

is_on = True #Boolean para que el loop no sea infinito
while is_on:
    print(logo)
    options = menu.get_items()
    choice = input(f"whats your drink of choice {options}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
               coffee_maker.make_coffee(drink)
            

