######################################################################
# Author: Sabdi Lopez                                       ****** TODO: CHANGE THIS!! ******
# username: lopezjimenezs                                   ****** TODO: CHANGE THIS!! *****
#
# Purpose: draw something complex, like a house, animal, or person
# I am going to be drawing my dog (there is a picture reference in my google docs)
#https://docs.google.com/document/d/1Dfdfu9-5X_AGFb_uNJKpNpcRDDoIxyrazyOssvjOjsk/edit#
######################################################################
# Acknowledgements:
#
# Modified from original code written by Dr. Jan Pearce
#
# Licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
######################################################################
import turtle


def circle_1(moon):        #in order to make a moon i have to have two circles overlapping, this is the first one
    """
    Makes the first circle to make the moon
    """
    moon.penup()
    moon.goto(100, -100)
    moon.pendown()
    moon.color("white")
    moon.begin_fill()
    moon.circle(80)
    moon.end_fill()
    moon.penup()


def circle_2(moon):                    #this is the second moon that overlaps
    """
    Makes the second circle in order to complete the moon
    """

    moon.goto(150, -100)
    moon.pendown()
    moon.color('black')
    moon.begin_fill()
    moon.circle(80)
    moon.end_fill()

def star_1(moon):                 #star number 1
    """
    Makes the first star
    """
    moon.penup()
    moon.goto(-50, 30)
    moon.pendown()
    moon.color('hot pink')
    moon.begin_fill()
    for i in range(5):
        moon.forward(50)
        moon.right(144)
    moon.end_fill()

def star_2(moon):                   #star number
    """
    Make the 2nd star
    """
    # star num 2
    moon.penup()
    moon.goto(-100, 150)
    moon.pendown()
    moon.color('purple')
    moon.begin_fill()
    for i in range(5):
        moon.forward(70)
        moon.right(144)
    moon.end_fill()

def star_3(moon):            #star number 3
    """
    make the 3rd star
    """
    # star num 3
    moon.penup()
    moon.goto(-200, -40)
    moon.pendown()
    moon.color("light sky blue")
    moon.begin_fill()
    for i in range(5):
        moon.forward(40)
        moon.right(144)
    moon.end_fill()

def star_4(moon):                     #star number 4
    """
    makes 4th star
    """
    # star num 4
    moon.penup()
    moon.goto(-250, -100)
    moon.pendown()
    moon.color('lime')
    moon.begin_fill()
    for i in range(5):
        moon.forward(55)
        moon.right(144)
    moon.end_fill()
def star_5(moon):                  #star number 5
    """
    makes 5th star
    """
    moon.penup()
    moon.goto(-250, 100)
    moon.pendown()
    moon.color('light coral')
    moon.begin_fill()
    for i in range(5):
        moon.forward(80)
        moon.right(144)
    moon.end_fill()

def make_text(moon, txt):               #writes my  text
    """
    Writes text to the screen.

    :param shape: a Turtle object
    :return: None
    """
    moon.penup()
    moon.color("#775a85")
    moon.setpos(-70,-130)
    moon.pendown()
    moon.write(txt, move=False, align='center', font=("Arial", 40, ("bold", "normal")))



def main():
    """
    Draws a moon and four stars on the screen

    :return: None
    """

    wn = turtle.Screen()
    wn.bgpic("space_bg.gif")

    moon = turtle.Turtle()
    moon.hideturtle()
    # Function calls for each part of the house
    circle_1(moon)
    circle_2(moon)
    star_1(moon)
    star_2(moon)
    star_3(moon)
    star_4(moon)
    star_5(moon)
    make_text(moon,"Dream Big!")

    wn.exitonclick()
main()