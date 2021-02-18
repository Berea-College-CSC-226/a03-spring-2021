#################################################################################
# Author: Beau Schneider
# Username:schneiderb
#
# Assignment:a03_schneiderb
# Purpose: a03 assignment
# Google Doc Link:https://docs.google.com/document/d/1dzsqV2KnOE22uxNHBlgi8hzqCdq1IqWeQvJhdgPX_Ks/edit?usp=sharing
#
#################################################################################
import turtle
wn = turtle.Screen()
wn.bgcolor('light blue')

t1 = turtle.Turtle()
t1.pensize(10)
t1.speed(9)


# House body
def function_1(t1):
    """ the use of this function is to draw the body of the house"""
    t1.pencolor("#A52A2A")
    t1.fillcolor("#A52A2A")
    t1.begin_fill()
    for i in range(1):
        t1.forward(140)
        t1.left(90)
        t1.forward(150)
        t1.left(90)
        t1.forward(140)
        t1.left(90)
        t1.forward(150)
    t1.end_fill()



function_1(t1)

t2 = turtle.Turtle()
t2.pensize(10)
t2.speed(9)


# Roof of House
def function_2(t2):
    """the use of this function of to draw the roof onto the top of the house"""
    t2.pencolor("#CD0000")  # sets pen color
    t2.fillcolor("#CD0000")   # sets fill color
    t2.penup()
    t2.left(90)
    t2.fd(150)
    t2.pendown()   # gets pen into position
    t2.begin_fill()
    t2.right(45)    #draws roof
    t2.forward(85)
    t2.right(80)
    t2.forward(100)   #finishes roof
    t2.right(145)
    t2.fd(140)
    t2.end_fill()


function_2(t2)

t3 = turtle.Turtle()
t3.pensize(5)
t3.speed(9)


# chimney
def function_3(t3):
    """ the use of this function is to draw the chimney on the house """
    t3.penup()
    t3.pencolor("#CD0000")
    t3.fillcolor("#CD0000")
    t3.forward(140)    # getting int position
    t3.left(90)
    t3.fd(150)
    t3.pendown()
    t3.begin_fill()   # sets marker to begin fill
    t3.fd(60)    # begins the drawing of chimney
    t3.left(90)
    t3.fd(30)
    t3.left(90)
    t3.fd(60)
    t3.left(90)
    t3.fd(30)
    t3.end_fill()   # ends marker to fill and fills red
    t3.penup()


function_3(t3)

t4 = turtle.Turtle()
t4.pensize(30)
t4.speed(9)


# chimney smoke
def function_4(t4):
    """ the use of this function is to draw the chimney smoke """
    t4.pencolor("#808080")   # setting draw color
    t4.fillcolor("#808080")  # setting fill color
    t4.penup()
    t4.fd(140)
    t4.left(90)
    t4.fd(160)
    t4.left(10)
    t4.fd(60)   # in position
    t4.pendown()
    t4.right(10)
    t4.forward(20)
    t4.left(40)
    t4.forward(20)


function_4(t4)

t5 = turtle.Turtle()
t5.pensize(5)
t5.speed(9)


# window for the house
def function_5(t5):
    """the use of this function is to draw the window of the house """
    t5.pencolor("#000000") # sets pen color to black
    t5.fillcolor("#00FFFF")   # sets fill color to aqua
    t5.penup()
    t5.forward(120)
    t5.left(90)
    t5.forward(50)
    t5.pendown()   # in position
    t5.begin_fill()
    t5.left(90)    # begins drawing window
    t5.forward(30)
    t5.right(90)
    t5.forward(50)
    t5.right(90)
    t5.forward(30)
    t5.right(90)
    t5.forward(50)   # finishes window
    t5.end_fill()


function_5(t5)

t6 = turtle.Turtle()
t6.pensize(5)
t6.speed(9)
t6.pencolor("#000000") # sets the sraw color to black
t6.fillcolor("#53868B") # sets the fill color to cadet blue


# door of the house
def function_6(t6):
    """The use of this function is to draw the door on the house"""
    t6.penup()
    t6.forward(50)
    t6.pendown()
    t6.begin_fill()
    t6.left(90)
    t6.fd(70)
    t6.left(90)
    t6.fd(30)
    t6.left(90)
    t6.fd(70)
    t6.left(90)
    t6.fd(30)
    t6.end_fill()


function_6(t6)










wn.exitonclick()











