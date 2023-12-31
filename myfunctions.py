import turtle
from datetime import datetime
import re
from PIL import ImageGrab
from PIL import Image

def draw_background(a_turtle):
    """ Draw a background rectangle. This is necessary so that the background is 
    visible in the saved eps file. Simply setting t.screen.bgcolor() doesn't work."""
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

def get_datetime_str():
    date_time = datetime.now().isoformat() #now.strftime("%m/%d/%Y, %H:%M:%S")
    # drop miliseconds, i.e. everything after the dot
    date_time_str = re.sub(r'\..*', '', date_time) # replaces literal .  (\.) and everything that follows (.*) with empty string
    date_time_str = re.sub(r'(.*):(.*):(.*)', r'\1h\2m\3', date_time_str) # replace first ':' with h and second ':' with m, using 3 capture groups, denoted by '()' and called by \<integer>
    # print(date_time_str)
    # sys.exit(0)
    return date_time_str

def save_turtle_image(keyword_output_name):
    """
    keyword_output_name: str, determines the prefix of the output file
    Save the current turtle canvas as an EPS file, using the current date-time in the file name.
    """

    date_time_str = get_datetime_str()
    output_path = f"images/{keyword_output_name}_{date_time_str}.eps"
    turtle.getscreen().getcanvas().postscript(file=output_path)
    print(f"File saved under {output_path}")

###############
    
def dump_gui():
    """
    WARNING - this function has bugs
    takes a png screenshot of a tkinter window, and saves it on in cwd
    """
    print('...dumping gui window to png')

    x0 = root.winfo_rootx()
    y0 = root.winfo_rooty()
    x1 = x0 + root.winfo_width()
    y1 = y0 + root.winfo_height()
    
    date_time_str = get_datetime_str()
    ImageGrab.grab().crop((x0, y0, x1, y1)).save(f"images/gui_image_grabbed_{date_time_str}.png")

def save_layout(filename):
    """
    WARNING - this function has bugs
    """
    ps = turtle.getscreen().getcanvas().postscript(colormode="color")
    im = Image.open(io.BytesIO(ps.encode("utf-8")))
    im.save(filename, format="PNG")