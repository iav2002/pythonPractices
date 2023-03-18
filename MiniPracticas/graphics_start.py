# # import turtle
# # jonny = turtle.Turtle()
# from turtle import Turtle, Screen
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("red")
# timmy.circle(100)
# my_screen = Screen()

# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["POKEMON", "TYPE"]
table.add_row(["Adelaide", 600.5])
table.add_row(["Brisbane", 1146.4])
print(table)