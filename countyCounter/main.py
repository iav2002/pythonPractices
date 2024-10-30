import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("Ireland Counties")
image = "countyCounter/ireland-blank-map.gif"
screen.addshape(image)
turtle.shape(image)

data =  pd.read_csv("countyCounter/32_counties.csv")

county_list = data["county"].to_list()
#print(state_list)
guessed_county = []
missed_county = []

while len(guessed_county) < 34:
    answer_county = screen.textinput(title = f"{len(guessed_county)} out of 32",
                                     prompt="Guess the County").title()
    print(answer_county)

    if answer_county == "Exit":

        for county in county_list:
            if county not in guessed_county:
                missed_county.append(county)
            
        print(missed_county)
        new_data = pd.DataFrame(missed_county)
        counter = len(missed_county)
        new_data.to_csv(f"/Users/ignacioalarconvarela/Developer/VsCode_Python/countyCounter/{counter}_counties_to_learn.csv")
        break

    if answer_county in county_list:

        guessed_county.append(answer_county)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        county_data = data[data.county == answer_county]
        t.goto(float(county_data.x.item()),float(county_data.y.item()))
        t.write(answer_county)

