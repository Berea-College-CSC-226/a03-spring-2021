# Author: Anish Kharel
# Username: Kharela
# Assignment: A03: robotic turtle

import turtle

def make_base():
    """This functions main purpose is to draw the base layout in which the phone will build off of"""
    base = turtle.Turtle()
    base.hideturtle()
    base.penup()
    base.pensize(3)
    base.forward(-150)
    base.left(90)
    base.forward(200)
    base.right(180)
    base.pendown()
    for i in range(2):
        base.forward(450)
        base.left(90)
        base.forward(235)
        base.left(90)

def make_additions():
    """THis functions purpose is to implement the bezels and camera and homebutton"""
    homeb = turtle.Turtle() #make the bottom bezel of the phone
    homeb.hideturtle()
    homeb.penup()
    homeb.forward(-140)
    homeb.right(180)
    homeb.forward(10)
    homeb.left(90)
    homeb.forward(205)
    homeb.left(90)
    homeb.pendown()
    homeb.pensize(2)
    homeb.forward(235)
    homeb.penup()
                            #make the home button
    homeb.forward(-118)
    homeb.right(90)
    homeb.forward(25)
    homeb.pendown()
    homeb.circle(10)
    homeb.penup()
                            #making the top bezel
    homeb.left(180)
    homeb.forward(390)
    homeb.left(90)
    homeb.forward(118)
    homeb.left(180)
    homeb.pendown()
    homeb.forward(235)
    homeb.penup()
                            #making the camera and sesor
    homeb.forward(-140)
    homeb.left(90)
    homeb.forward(25)
    homeb.right(90)
    homeb.pensize(4)
    homeb.pendown()
    homeb.forward(25)
    homeb.penup()
    homeb.pensize(2)
    homeb.forward(15)
    homeb.pendown()
    homeb.circle(5)

def make_apps(amount):
    """ This functions purpose is to construct the apps that will fill the iphone screen"""
    app = turtle.Turtle()
    app.hideturtle()

    app.penup()
    app.forward(-135)
    app.left(90)
    app.forward(145)
    app.right(90)
    app.pendown()
    for i in range(amount):
        app.pendown()
        for i in range(4):
            app.forward(40)
            app.right(90)

        app.penup()
        app.forward(50)


def main():
    """Main function which will call everything else and put it together"""
    wn = turtle.Screen()
    wn.bgcolor("light blue")
    make_base()
    make_additions()

    make_apps(3)

    wn.mainloop()

main();