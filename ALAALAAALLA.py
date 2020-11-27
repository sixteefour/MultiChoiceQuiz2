#Space Invaders
#Set up the Screen
#Python 2.7 on Windows
import turtle
import os

#Set up the Screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

#Draw a border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()








delay = raw_input("Press Enter to finish.")