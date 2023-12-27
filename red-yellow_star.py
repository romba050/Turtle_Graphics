#!/usr/bin/env python3.12

"""
Star from tutorial:
https://docs.python.org/3/library/turtle.html#turtle.circle
"""

from datetime import datetime
import tkinter as tk
from PIL import ImageGrab
from PIL import Image
import turtle
import sys
import re
import io


def draw_background(a_turtle):
    """ Draw a background rectangle. This is necessaru so that the background is 
    visible in the saved eps file. Just setting t.screen.bgcolor() doesn't work."""
    ts = a_turtle.getscreen()
    canvas = ts.getcanvas()
    height = ts.getcanvas()._canvas.winfo_height()
    width = ts.getcanvas()._canvas.winfo_width()

    turtleheading = a_turtle.heading()
    turtlespeed = a_turtle.speed()
    penposn = a_turtle.position()
    penstate = a_turtle.pen()

    a_turtle.penup()
    a_turtle.speed(0)  # fastest
    a_turtle.goto(-width/2-2, -height/2+3)
    a_turtle.fillcolor(turtle.Screen().bgcolor())
    a_turtle.begin_fill()
    a_turtle.setheading(0)
    a_turtle.forward(width)
    a_turtle.setheading(90)
    a_turtle.forward(height)
    a_turtle.setheading(180)
    a_turtle.forward(width)
    a_turtle.setheading(270)
    a_turtle.forward(height)
    a_turtle.end_fill()

    a_turtle.penup()
    a_turtle.setposition(*penposn)
    a_turtle.pen(penstate)
    a_turtle.setheading(turtleheading)
    a_turtle.speed(turtlespeed)


# Start turtle
t = turtle.Turtle(visible=False) # Turtle(shape="turtle", visible=False)

# t.screen.bgcolor("white")
# draw_background(t)

t.color('red')
t.fillcolor('yellow')
t.speed(0)
TURTLE_SIZE = 20
line_length = 600

t.begin_fill()
screen = t.getscreen()

# initialise the turtle to a position without drawing
t.penup()
# pos (0, 0) is the middle
start_pos = turtle.Vec2D(-line_length/2, -TURTLE_SIZE/2)
t.goto(start_pos)
t.pendown()

# t.goto(TURTLE_SIZE/2 - screen.window_width()/2, screen.window_height()/2 - TURTLE_SIZE/2) # top left

while True:
    print(t.pos())
    t.forward(line_length)
    t.left(170)
    # if t.pos() == start_pos: # doesn't work because floating point numbers are not exactly the same
    if abs(t.xcor() - start_pos[0]) < 0.5 and \
        abs(t.ycor() - start_pos[1]) < 0.5:
    # if abs(t.pos()) < 1: # abs(pos()) < 1 is a good way to know when the turtle is back at its home position.
        break

t.end_fill() # applies the filling color defined at the beginning


# ts = t.getscreen()
# canvas = ts.getcanvas()
# canvas.postscript(file=f"graphic_{date_time_str}.eps")



date_time = datetime.now().isoformat() #now.strftime("%m/%d/%Y, %H:%M:%S")
# drop miliseconds, i.e. everything after the dot
date_time_str = re.sub(r'\..*', '', date_time) # replaces literal .  (\.) and everything that follows (.*) with empty string
date_time_str = re.sub(r'(.*):(.*):(.*)', r'\1h\2m\3', date_time_str) # replace first ':' with h and second ':' with m, using 3 capture groups, denoted by '()' and called by \<integer>
# print(date_time_str)
# sys.exit(0)
turtle.getscreen().getcanvas().postscript(file=f"images/red-yellow_star_{date_time_str}.eps")

turtle.getscreen().exitonclick()  # optional