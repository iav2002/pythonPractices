# import colorgram

# # Extract 6 colors from an image.
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
# Copiar los colores de una imagen.


import turtle 
import random
t = turtle.Turtle()
t.speed("fastest")
t.hideturtle()
turtle.colormode(255)
color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]

t.penup()
t.goto(-200, -250)

#que haya un espacio blanco, y que lo haga 10 veces
for _ in range(10):
    for _ in range(10):
       #Que pinte un dot y avance
        t.dot(20, random.choice(color_list))
        t.penup()
        t.fd(50)
    t.setheading(90)
    t.fd(50)
    t.setheading(180)
    t.fd(500)
    t.setheading(0)


#girar hacia la izquierda y repetir


screen = turtle.Screen()
screen.exitonclick() 