from turtle import Turtle

class Paddle(Turtle): #Creacion de la clase junto con la herencia de la libreria Turtle

    def __init__ (self, position):
        super().__init__() #Inicializador de super metodos
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len= 1)
        self.goto(position)
    def go_up(self):

        
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)