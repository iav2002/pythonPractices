import turtle

tim = turtle.Turtle()
screen = turtle.Screen()

def move_forwards():
    tim.fd(20)
        
def move_backwards():
    tim.fd(-20)

def turn_left():
    tim.left(10)

def turn_right():
    tim.setheading(tim.heading() - 10)

def clear_():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown

screen.listen()
# Cuando el methodo no es tu yo, es mejor utilizar keywords arguments, y no posicionales
screen.onkey(key = "w", fun = move_forwards) #al pasar la funcion non se utiliza ()
screen.onkey(key = "s", fun = move_backwards)
screen.onkey(key = "a", fun = turn_left)
screen.onkey(key = "d", fun = turn_right)
screen.onkey(key = "c", fun = clear_)

screen.exitonclick()

