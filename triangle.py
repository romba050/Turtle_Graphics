#!/usr/bin/env python3.12

from datetime import datetime
import tkinter as tk
from PIL import ImageGrab
from PIL import Image
import turtle
import sys
import re
import io

def dump_gui():
    """
    takes a png screenshot of a tkinter window, and saves it on in cwd
    """
    print('...dumping gui window to png')

    x0 = root.winfo_rootx()
    y0 = root.winfo_rooty()
    x1 = x0 + root.winfo_width()
    y1 = y0 + root.winfo_height()
    ImageGrab.grab().crop((x0, y0, x1, y1)).save(f"gui_image_grabbed_{date_time_str}.png")

def save_layout(filename):
    ps = turtle.getscreen().getcanvas().postscript(colormode="color")
    im = Image.open(io.BytesIO(ps.encode("utf-8")))
    im.save(filename, format="PNG")
    

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

# # setting up the tk canvas
# root = tk.Tk()
# canvas = tk.Canvas(root, width=500, height=500)
# canvas.pack()
# t = turtle.RawTurtle(canvas)

# Draw triangle
t = turtle.Turtle()
# s = turtle.Screen()
# s.bgcolor("black")

t.screen.bgcolor("black")
draw_background(t)
t.width(2)
t.speed(15)

#col = ('yellow', 'red', 'cyan')
col = ('white', 'pink', 'cyan')

for i in range(300):
    t.pencolor(col[i%3])
    t.forward(i*4)
    t.right(121)

s = turtle.Screen()
s.bgcolor("black")


# ts = t.getscreen()
# canvas = ts.getcanvas()
# canvas.postscript(file=f"graphic_{date_time_str}.eps")



date_time = datetime.now().isoformat() #now.strftime("%m/%d/%Y, %H:%M:%S")
# drop miliseconds, i.e. everything after the dot
date_time_str = re.sub(r'\..*', '', date_time) # replaces literal .  (\.) and everything that follows (.*) with empty string
date_time_str = re.sub(r'(.*):(.*):(.*)', r'\1h\2m\3', date_time_str) # replace first ':' with h and second ':' with m, using 3 capture groups, denoted by '()' and called by \<integer>
# print(date_time_str)
# sys.exit(0)
turtle.getscreen().getcanvas().postscript(file=f"graphic_{date_time_str}.eps")

turtle.getscreen().exitonclick()  # optional

# save_layout(f"graphic_{date_time_str}.png")

# save canvas as png
# dump_gui()   