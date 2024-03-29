from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width = 500, height= 400)
user_bet = screen.textinput(title = "Make your bet", prompt="Which turtle will win the Race, type a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-120, -80, -40, 0, 40, 80]
all_turtles = []


for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230, y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
   
    for turtle in all_turtles:
        if turtle.xcor() > 230:
           is_race_on = False
           winning_color = turtle.pencolor()
           if winning_color == user_bet:
                print(f"You've won, The {winning_color} is the champ!")
           else:
                print(f"You've lost, The {winning_color} is the champ!")

        rand_distance =  random.randint(0, 10)
        turtle.fd(rand_distance)
screen.exitonclick()