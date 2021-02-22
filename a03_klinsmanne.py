#################################################################################
# Author: Emmanuel Klinsmann
# Username: klinsmanne
#
# Assignment: A03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose:
# Google Doc Link: https://docs.google.com/document/d/1t6m_Ml__f6pDf03wgLTeq3lsXDSaRN7Y8db6U-ATdRU/edit?usp=sharing
#
#################################################################################


import turtle

car = turtle.Turtle()


def draw_upperbody(car):
    """
    Draw and fill upperbody
    :param car:
    :return:
    """
    car.color('#008000')  # set pen color to green
    car.fillcolor('#008000')  # set fill color to green
    car.speed(3)
    car.penup()  # pick pen to begin to draw upper body rectangle
    car.goto(0, 0)
    car.pendown()
    car.begin_fill()
    car.forward(370)
    car.left(90)
    car.forward(50)
    car.left(90)
    car.forward(370)
    car.left(90)
    car.forward(50)
    car.end_fill()  # finish drawing anf filling upperbody rectangle

    # ....


def draw_window_and_roof(car):
    """
    Draw window and roof
    :param car:
    :return:
    """

    car.speed(3)
    car.penup()  # pick pen to begin to draw trapezoidal top
    car.goto(100, 50)
    car.pendown()
    car.setheading(45)
    car.forward(70)
    car.setheading(0)
    car.forward(100)
    car.setheading(-45)
    car.forward(70)
    car.setheading(90)
    car.penup()
    car.goto(200, 50)
    car.pendown()
    car.forward(49.50)  # finish drawing  trapezoidal top
    # ...


def draw_two_tyres(car):
    """
    Draw two tyres
    :param car:
    :return:
    """

    car.penup()  # pick pen to begin to draw circular tyres
    car.goto(100, -10)
    car.pendown()
    car.color('#FFFFFF')
    car.fillcolor('#FFFFFF')
    car.begin_fill()
    car.circle(30)
    car.end_fill()
    car.penup()
    car.goto(300, -10)
    car.pendown()
    car.color('#FFFFFF')
    car.fillcolor('#FFFFFF')
    car.begin_fill()
    car.circle(30)
    car.end_fill()
    car.pendown()

    car.hideturtle()  # finish drawing circular tyres and hide pen


def write_text(car, txt):
    """
    Writes text to the screen
    :param car:
    :param txt:
    :return: None
    """
    car.penup()  # pick pen to put in position to write the title text
    car.color("#FFFFFF")
    car.setpos(70, 120)
    car.write(txt, move=False, align='center', font=("Times New Roman", 30, ("bold", "normal")))  # set properties
    # for title text


def main():
    """
    Draw a car on the screen
    :return:
    """

    wn = turtle.Screen()  # makes a new turtle screen
    wn.bgcolor('#000000')
    wn.title("klinsmann's car")

    # ...
    draw_upperbody(car)  # Function call to draw upperbody
    draw_window_and_roof(car)  # Function call to draw window and roof
    draw_two_tyres(car)  # Function call to draw the two tyres
    write_text(car, "Klinsmann's Car")  # Function call to write the title text

    wn.exitonclick()  # wait for a user click to exit


main()
