from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__() #Para inicializar una clase de inheretance, usar metodos no nuestros
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len= 0.5, stretch_wid= 0.5)
        self.color("red")
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        self.refresh()

#refresh comidita de manera randomica
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

   
