from turtle import Screen  
from score import Score
import time
from food import Food
from snake import Snake

# Create a snake body
# Move the Snake
# Control the Sake
# Detect collision with food
# Create a scoreboard
# Detect collision with wall
# Detect collision with tail

screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

#Creando nuestros objetos
snake = Snake()
food = Food()
scoreboard = Score()

screen.listen()
# Cuando el methodo no es tu yo, es mejor utilizar keywords arguments, y no posicionales
screen.onkey(key = "Up", fun = snake.up) #al pasar la funcion non se utiliza ()
screen.onkey(key = "Down", fun = snake.down)
screen.onkey(key = "Left", fun = snake.turn_left)
screen.onkey(key = "Right", fun = snake.turn_right)

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
   
    snake.move()
    #detection of colicison #calling method to random position
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    
    #detect collition with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280: 
        is_game_on = False
        scoreboard.game_over()

    #detect collition with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()

    #if head collie

screen.exitonclick()

