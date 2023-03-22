import turtle 
import random

t = turtle.Turtle()
turtle.colormode(255)
t.shape("arrow")
t.pensize(2)
t.speed("fastest")

def random_color():
    r = random.randint(0 , 255)
    g = random.randint(0 , 255)
    b = random.randint(0 , 255)
    color = [r , g, b]
    return color

#Drawing a Spirograph
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading() + size_of_gap)
    
draw_spirograph(5)








# #Random Walk
# directions = [ 0, 90, 180, 270]
# turtle.pensize(15)
# turtle.speed("fastest")

# for i in range (250):
#     turtle.color(random_color())
#     turtle.fd(30)
#     turtle.setheading(random.choice(directions))

# #Multiples Formas Dibujo
# def draw_shape(num_side):
#     angulo = 360 / num_side
#     for i in range (num_side):

#         turtle.forward(100)
#         turtle.left(angulo)

# # Dibujar Multiples formas geomertricas
# for shape_side_n in range (3, 11):
#     turtle.color(random.choice(colours))
#     draw_shape(shape_side_n)



# Dibujar un cuadrado
# for i in range (4):
#     cody.forward(100)
#     cody.left(90)

# # Dashed line
# for _ in range(15):
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)
#     turtle.pendown()


screen = turtle.Screen()
screen.exitonclick() 