from turtle import Screen, Turtle
import time

STARTING_POSITIONS = [(0, 0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    #este es el inicilizador  necesario para poder crear el objeto.
    #en el que tambien creamos los metodos necesarios para despues.
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0] #agarramos el primer segmento y lo nombramos "cabeza"

    #creamos la serpiente, y pasamos como parametro el metodo pre_creado anterior mente
    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
    #metodo para moverse, donde cada cuadro anterior tracea el posterior
    def move(self): 
        for seg_num in range(len(self.segments) - 1, 0, -1):
                new_x = self.segments[seg_num -1].xcor()       
                new_y = self.segments[seg_num -1].ycor()       
                self.segments[seg_num].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE) #La cabeza la mandamos que siempre este en movimiento.

    #Fuciones para poder controlar la cabeza
    
    def up (self):
        #Condicional para ver, si la cabeza esta mirando abajo, NO SE PUEDE SUBIR
        #No seria un movimiento natural del "juego"
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)




