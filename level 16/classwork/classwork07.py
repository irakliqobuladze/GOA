# 7)

from turtle import*

speed(10)
width(4)

def draw_square():
    for i in range(4):
        forward(250)
        left(90)

def move_pen(x, y):
    penup()
    goto(x, y)
    pendown()

move_pen(0,0)    
draw_square()

move_pen(-280,0) 
draw_square()

move_pen(-280,-280) 
draw_square()

move_pen(0,-280) 
draw_square()

exitonclick