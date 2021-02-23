#################################################################################
# Author: Malena Leon Hidalgo
# Username: leonhidalgom
#
# Assignment: A03: Robotic Turtles (Spring 2021)
#
# Google Docs Document: https://docs.google.com/document/d/1AUoVQFGwSgxNgRgfb_sRYt14vh0nEoEfPSMUJsufEFs/edit?usp=sharing
# Acknowledgements: https://www.youtube.com/watch?v=k5IWXZ28BTU, https://www.101computing.net/rgb-converter/, https://www.geeksforgeeks.org/turtle-write-function-in-python/
#################################################################################

import turtle  # import turtle from library
from random import randint

wn = turtle.Screen()  # set up the turtle screen
wn.bgcolor("#000000")


def draw_figure(turtle, color, x, y, radius):            # create a figure that will later turn into a moon
    """
    this function draws the moon using the turtle
    :param turtle: it is used to draw the moon
    :param color: determines the color of the turtle
    :param x: coordinates of the turtle
    :param y: coordinates of the turtle
    :param radius: the radius of the circle of the moon
    :return:
    """
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


def draw_starts(turtle,color,x,y,size):                   # create the form of the stars
    """
    this function draws the stars
    :param turtle: it is used to draw the stars
    :param color: determines the color of the turtle
    :param x: coordinates of the turtle
    :param y: coordinates of the turtle
    :param size: the radius of the circle of the moon
    :return:
    """
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.right(150)
    for i in range(5):
        turtle.forward(size)
        turtle.right(155)
        turtle.forward(size)
    turtle.end_fill()
    turtle.setheading(0)



def main():  # draw the moon and the stars with using a def main():
    """
    call the other functions
    :return:
    """
    for i in range(25):
        starts = randint(25, 35)
        for z in range(0, starts):
            x = randint(-190, 190)
            y = randint(-150, 140)
            size = randint(8, 25)

        draw_starts(turtle, "#add700", x, y, size)

    draw_figure(turtle, "white", 120, 80, 50)  # drawing a white circle
    draw_figure(turtle, "#000000", 90, 80, 50)  # drawing over the white circle to create the form of a moon

    # drawing the stars

    turtle.color("#ff0073")  # message the will be display in the turtle screen
    style = ('verdana', 15, 'italic', 'bold')
    turtle.write('Good night my friends! - Malena', font=style, align='center')
    turtle.hideturtle()


main()  # calling the main function

wn.exitonclick()
