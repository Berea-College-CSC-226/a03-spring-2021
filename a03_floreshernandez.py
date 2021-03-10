###############################################################################
# Author: Michell Flores
# Username: floreshernandezm
#
# Assignment: Homework A03 - Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: to create a drawing using different functions
# Google Doc: https://docs.google.com/document/d/1_EjHXbyI7MC3JTAr1MCDiQdsSHdgdKsVGYk90uryreM/edit#
#
###############################################################################
import turtle
k = turtle.Turtle()
# import turtle and name it


def make_house(k):
    """Drawing a house"""
    turtle.colormode(255)
    k.color(100, 127, 115)
    k.shape("turtle")
    k.pensize(10)
    k.speed(2)
    k.penup()
    k.forward(10)
    k.right(90)
    k.pendown()
    k.begin_fill()
    for i in range(4):
        k.fd(250)
        k.left(90)
    k.left(135)
    k.fd(180)
    k.right(90)
    k.fd(180)
    k.end_fill()                # create the outline of the house and fill


y = turtle.Turtle()


def make_door(y):
    """Draw door on house"""
    y.shape("turtle")
    y.pensize(10)
    y.speed(5)
    y.color("red")
    y.penup()
    y.right(45)
    y.forward(250)
    y.right(90)
    y.fd(110)
    y.pendown()
    y.begin_fill()
    y.right(90)
    y.fd(50)
    y.left(90)
    y.fd(40)
    y.left(90)
    y.fd(50)
    y.left(90)
    y.fd(40)
    y.end_fill()


moe = turtle.Turtle()


def make_flower1(moe):
    """Draw flower 1 next to house"""
    moe = turtle.Turtle()
    moe.shape("turtle")
    moe.color("orange")
    moe.pensize(6)
    moe.speed(5)
    moe.penup()
    moe.goto(-140, -120)
    moe.pendown()
    for i in range(8):
        moe.right(45)
        moe.fd(30)
        moe.left(45)
        moe.fd(30)
        moe.left(135)
        moe.fd(30)
        moe.left(45)
        moe.fd(30)
        moe.left(135)
    moe.right(90)
    moe.fd(150)


p = turtle.Turtle()


def make_flower2(p):
    """Draw flower 3"""
    p.shape("turtle")
    p.color("pink")
    p.pensize(6)
    p.speed(5)
    p.penup()
    p.goto(-60, -180)
    p.pendown()
    for i in range(8):
        p.right(45)
        p.fd(30)
        p.left(45)
        p.fd(30)
        p.left(135)
        p.fd(30)
        p.left(45)
        p.fd(30)
        p.left(135)
    p.right(90)
    p.fd(150)


h = turtle.Turtle()


def make_flower3(h):
    """Draw last flower"""
    h = turtle.Turtle()
    h.shape("turtle")
    h.color("yellow")
    h.pensize(6)
    h.speed(5)
    h.penup()
    h.goto(-220, -180)
    h.pendown()
    for i in range(8):
        h.right(45)
        h.fd(30)
        h.left(45)
        h.fd(30)
        h.left(135)
        h.fd(30)
        h.left(45)
        h.fd(30)
        h.left(135)
    h.right(90)
    h.fd(150)


def main():
    """Draw house with flowers near it"""
    wn = turtle.Screen()
    wn.bgcolor("cyan")
    make_house(k)
    make_door(k)
    make_flower1(moe)
    make_flower2(p)
    make_flower3(h)

    wn.exitonclick()


main()
