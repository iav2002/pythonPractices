from turtle import Turtle, Screen
from paddles import Paddle

#Create Screeen
screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800, height = 600)
screen.title("Pong")
screen.tracer(0)


#Create and move a paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((350, 0))


screen.listen()
screen.onclick(r_paddle.go_up, "Up")
screen.onclick(r_paddle.go_up, "Down")
screen.onclick(l_paddle.go_up, "w")
screen.onclick(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    screen.update()
    
#Create the ball and make it move
#Detect collision with wall and bounce
#Detect collision with paddle
#Detecth when paddle misses
#Keep score


screen.exitonclick()