from turtle import Turtle
import random

#Varibales fijas, que al momemnto de querer ser cambiadas es mas sencillo
ALIGMENT = "center"
FONT = ("Arial", 24, "normal")




class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("Snake_game/data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score {self.score}, High Score : {self.high_score}",align= ALIGMENT, font= FONT )


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Snake_game/data.txt", mode = "w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto( 0 ,0)
    #     self.write(f"GAME OVER",align= ALIGMENT, font= FONT  )


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


