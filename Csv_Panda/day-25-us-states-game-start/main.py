import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "/Users/ignacioalarconvarela/Developer/VsCode_Python/day-25-us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("day-25-us-states-game-start/50_states.csv")
state_list = data["state"].to_list()

guessed_states = []


while len(guessed_states) < 50:

    answer_state = screen.textinput(title = f"{len(guessed_states)} States out of 50",
                                     prompt= "What's another state's name:").title()
    print(answer_state)
    
    if answer_state == "Exit":
        #Same as a 4 lines but in a comprenhension list
        missing_states = [state for state in list  if state not in guessed_states]
        # missing_states = []
        # for state in state_list:
        #     if state not in guessed_states:
        #         missing_states.append(state)                  
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("day-25-us-states-game-start/states_to_learn.csv")
        break  

    if answer_state in state_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_state)


        
    #states_to_learn.csv 