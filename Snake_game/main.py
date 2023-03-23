from turtle import Screen, Turtle
import time
from snake import Snake

screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
   
    snake.move()
    screen.listen()
    # Cuando el methodo no es tu yo, es mejor utilizar keywords arguments, y no posicionales
    screen.onkey(key = "Up", fun = snake.up) #al pasar la funcion non se utiliza ()
    screen.onkey(key = "Down", fun = snake.down)
    screen.onkey(key = "Left", fun = snake.turn_left)
    screen.onkey(key = "Right", fun = snake.turn_right)



screen.exitonclick()

