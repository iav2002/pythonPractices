from turtle import Turtle, Screen
from paddles import Paddle
from ball import Ball
import time

#Create Screeen
screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800, height = 600)
screen.title("Pong")
screen.tracer(0)


#Create and move a paddle, OOP
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    
    time.sleep(0.1) #realentizar actualizacion de frames
    screen.update()
    ball.move()




#Detect collision with wall and bounce
#Detect collision with paddle
#Detecth when paddle misses
#Keep score


screen.exitonclick()