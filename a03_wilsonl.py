######################################################################
# Author: Luke Wilson
# Username: wilsonl
#
# Assignment: A03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Continue practicing creating and using functions.
######################################################################
# Acknowledgements:
# https://stackoverflow.com/questions/29465666/how-do-you-draw-an-ellipse-oval-in-turtle-graphics-python
#################################################################################
import turtle                                       # import turtle library
bob = turtle.Turtle()                               # make turtle object


def banana():
    """draws a banana """
    turtle.colormode(255)
    bob.color(230, 230, 0)
    bob.begin_fill()
    bob.circle(90)
    bob.end_fill()
    bob.color("light green")
    bob.begin_fill()
    bob.left(45)
    bob.circle(135)
    bob.end_fill()                                              # banana is drawn
    bob.color("brown")
    bob.pensize(10)
    bob.forward(10)
    bob.penup()
    bob.goto(0, 170)
    bob.pendown()
    bob.forward(10)                                             # banana ends are drawn
    bob.penup()


def monkey_face():
    """draw monkey face"""
    bob.pensize(3)                                      # drawing head
    bob.goto(-100, 100)
    bob.pendown()
    bob.color("brown")
    bob.begin_fill()
    bob.circle(90, 405)
    bob.right(45)                                       # drawing ears
    bob.circle(45)
    bob.left(45)
    bob.circle(90, 135)
    bob.right(45)
    bob.circle(45)
    bob.end_fill()
    bob.left(45)
    bob.circle(90, 90)
    bob.left(45)                                        # drawing mouth
    bob.color("black")
    bob.penup()
    bob.forward(90)
    bob.pendown()
    bob.begin_fill()
    bob.circle(25)
    bob.penup()
    bob.goto(-200, 200)                                 # draw eyes
    bob.circle(5)
    bob.end_fill()
    bob.penup()
    bob.goto(-150, 210)
    bob.pendown()
    bob.begin_fill()
    bob.circle(5)
    bob.end_fill()
    bob.penup()                                          # draw nose
    bob.goto(-175, 175)
    bob.pendown()
    bob.begin_fill()
    bob.circle(1)
    bob.penup()
    bob.forward(15)
    bob.pendown()
    bob.circle(1)
    bob.end_fill()


def monkey_body():
    """draws monkey body"""
    bob.penup()
    bob.goto(0, 0)
    bob.color("brown")
    bob.pendown()
    bob.left(180)
    bob.pensize(5)
    bob.forward(300)                             # arms are drawn
    bob.penup()
    bob.goto(-50, -200)
    bob.right(45)
    bob.pendown()
    bob.forward(150)
    bob.left(90)
    bob.forward(150)                             # legs are drawn
    bob.penup()
    bob.goto(-200, 50)
    bob.pendown()
    bob.begin_fill()
    bob.circle(100)                             # this creates the torso
    bob.end_fill()


def main():
    """draw monkey with banana and display special message"""
    wn = turtle.Screen()                        # set up window for turtle screen
    wn.bgcolor("light green")
    bob.speed(100)                              # make turtle fast
    banana()
    monkey_face()                               # draw everything
    monkey_body()
    bob.penup()
    bob.goto(200, 200)
    color = ["black", "red", "blue", "yellow", "orange", "green", "pink", "purple"]  # make text in different colors
    for i in range(8):                          # make a staircase of text
        bob.color(color[i])
        bob.write("banana time!", move=False, align='center', font=("comic sans", 20))
        bob.penup()
        bob.forward(50)
        bob.pendown()
    wn.exitonclick()


main()
