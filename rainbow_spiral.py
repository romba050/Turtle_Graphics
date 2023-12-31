#!/usr/bin/env python3.12

import turtle
from myfunctions import *

t = turtle.Turtle()

colors = ["purple", "red", "light green", "pink", "orange", "blue", "aqua", "green", "cyan", "yellow"]

turtle.bgcolor("black")
draw_background(t)

for i in range(300):
    t.color(colors[i%10])
    t.pensize(2)
    t.forward(i)
    t.left(10)
    t.right(80)



save_turtle_image("rainbow_spiral")
turtle.getscreen().exitonclick()