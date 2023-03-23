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





# # Another solution.
# turtle_module.colormode(255)
# tim = turtle_module.Turtle()
# tim.speed("fastest")
# tim.penup()
# tim.hideturtle()
# color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
# number_of_dots = 100

# for dot_count in range(1, number_of_dots + 1):
#     tim.dot(20, random.choice(color_list))
#     tim.forward(50)

#     if dot_count % 10 == 0:
#         tim.setheading(90)
#         tim.forward(50)
#         tim.setheading(180)
#         tim.forward(500)
#         tim.setheading(0)





# #Drawing a Spirograph
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         t.color(random_color())
#         t.circle(100)
#         t.setheading(t.heading() + size_of_gap)
# draw_spirograph(5)


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