from turtle import *

#we want to paint a house

#step 1: draw a square
speed(30)
width(5)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
begin_fill()
color("yellow")
left(90)
forward(120)       #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing a window

left(30)
color("purple")
forward(60)
left(90)
color("brown")
begin_fill()
left(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()


penup()
goto(200,200)
pendown()


color("purple")
forward(20)
color("brown")
begin_fill()
right(90)
forward(50)
left(90)
forward(40)
left(90)
forward(50)
end_fill()

#draw a grass

penup()
goto(200,0)
pendown()

color("green")
begin_fill()
right(90)
forward(5)
left(90)
forward(170)
left(180)
forward(740)
left(90)
forward(300)
left(90)
forward(740)
left(90)
forward(300)
end_fill()

exitonclick()