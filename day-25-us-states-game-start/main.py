import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "/Users/ignacioalarconvarela/Developer/VsCode_Python/day-25-us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data =pd.read_csv("day-25-us-states-game-start/50_states.csv")
state_list = data["state"].to_list()

guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title = f"{len(guessed_states)} States out of 50",
                                     prompt= "What's another state's name:").title()
    print(answer_state)

    if answer_state in state_list:

        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)


screen.exitonclick()