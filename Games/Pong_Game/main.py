from turtle import Turtle, Screen
from paddles import Paddle
from ball import Ball
import time
from score import Scoreboard
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
scroeboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    
    time.sleep(ball.move_speed) #realentizar actualizacion de frames
    screen.update()
    ball.move()

#Detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

#Detect collision with right paddle and left paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x()

#Detecth when R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scroeboard.l_point()
    
#Detecth when L paddle misses
    if ball.xcor() < - 380:
        ball.reset_position()
        scroeboard.r_point()

#Keep score


screen.exitonclick()