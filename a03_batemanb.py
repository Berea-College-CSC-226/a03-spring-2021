#################################################################################
# Author: Brady Bateman
# Username: batemanb
#
# Assignment: A03: Fully Functional Gitty Psychedelic Robotic Turtles
#
# Purpose: Continue practicing creating and using functions.
# Google Doc Link: https://docs.google.com/document/d/1_m_paILsEOJis4kQXogZXEzn9-v-kvkR7mi4Bu0dsP4/edit#
#
#################################################################################
# Acknowledgements: A big thank you to my brother, Dylan Bateman. He helped me figure out an algorithm
# for drawing the koch snowflake in code
#
#################################################################################

import turtle
from random import randrange


def thue_morse(n):
    """Returns the Thue-Morse sequence as an array. Each element is a bool(True or False)"""
    n = 2 * n + 1
    out = [True]
    for i in range(n):
        step = []
        for j in out:
            step.append(not j)
        for j in step:
            out.append(j)
    return out


def teleport(tt, pos):
    """teleports turtles across the canvas without drawing the taken path"""
    tt.up()
    tt.goto(pos[0], pos[1])
    tt.down()
    return True


def koch(tt, order, pos, ort, step):
    """draws a koch snowflake"""
    fractal = thue_morse(order)   # Create an array using our thue_morse function
    teleport(tt, pos)   # Teleports the turtle to a given random position
    tt.seth(ort)   # Sets the turtle's heading to a random direction in a 360 degree scope
    tt.begin_fill()
    for i in range(3):
        for j in fractal:
            if j:
                tt.forward(step)
                tt.right(60)
            else:
                tt.right(180)
    tt.end_fill()
    return True


def create_turtle():
    """creates a turtle object with a random color"""
    name = turtle.Turtle()
    name.speed(0)
    name.ht()
    turtle.colormode(255)
    color = (randrange(0, 255), randrange(0, 255), randrange(0, 255))
    name.color(color)
    name.fillcolor(color)
    return name


def koch_and_stroke():
    """creates random parameters for our koch snowflake on each run, and loops the drawing until we close"""
    turtle_list = ["turtle1"]
    width = int(turtle.window_width() / 2)
    height = int(turtle.window_height() / 2)

    while True:
        for i in turtle_list:
            tt = create_turtle()
            pos = [randrange(-width, width), randrange(-height, height)]
            ort = randrange(360)
            order = randrange(4)
            step = randrange(10, 100)
            if order != 0:
                step /= 2 ** order
            koch(tt, order, pos, ort, step)


def main():
    window = turtle.Screen()
    window.bgcolor("black")
    koch_and_stroke()


main()
