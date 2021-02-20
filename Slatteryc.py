######################################################################
# Author: Cienna-Paige Slattery
# Username: slatteryc
#
# Assignment: A03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: create complex shapes using the turtle library
#
# google dox link: https://docs.google.com/document/d/1SWDcNhWhDWb3_HaFkmlPAocDKr0XGRKjXCv6GPtAj5M/edit?usp=sharing
#
######################################################################

import turtle


def spider():
    ts=turtle.Screen()    # name turtle screen
    ts.bgcolor("#861F9B")          # set background color to purple

    t1= turtle.Turtle()   # setting up turtle
    t1.speed(0)
    t1.up()
    t1.color("black")
    t1.goto(20, 100)
    t1.setheading(310)
    t1.down()

    t1.begin_fill()

    for i in range(40):  # draw first side of body
        t1.fd(1)
        t1.rt(2)
        t1.fd(3)

    for i in range(50):  # draw bottom of body
        t1.fd(3)
        t1.rt(2)

    for i in range(40):  # draw second side of body
        t1.fd(1)
        t1.rt(2)
        t1.fd(3)

    for i in range(50):  # draw top of body
        t1.fd(3)
        t1.rt(2)

    t1.end_fill()

# drawing head

    # setting position of turtle
    t1.up()
    t1.goto(0, -98)
    t1.down()

    t1.begin_fill()

    # making head
    for i in range(200):
        t1.fd(2)
        t1.rt(2)

    t1.end_fill()

    # drawing legs on left of body
    t1.up()
    t1.goto(-100, -40)
    t1.seth(110)
    t1.pensize(10)

    # left leg 1
    t1.down()
    t1.circle(90, 160)

    # left leg 2
    t1.up()
    t1.goto(-110, 30)
    t1.seth(110)
    t1.down()
    t1.circle(90, 160)

    # left leg 3
    t1.up()
    t1.goto(-100, 90)
    t1.seth(110)
    t1.down()
    t1.circle(90, 160)

    # drawing legs on right of body
    t1.up()
    t1.goto(0, -45)
    t1.seth(250)

    # right leg 1
    t1.down()
    t1.circle(90, -160)

    # right leg 2
    t1.up()
    t1.goto(10, 30)
    t1.seth(250)
    t1.down()
    t1.circle(90, -160)

    # right leg 3
    t1.up()
    t1.goto(0, 90)
    t1.seth(250)
    t1.down()
    t1.circle(90, -160)


def hearts():

    # setting up turtle
    t2 = turtle.Turtle()
    t2.color("#F901F5")       #pink
    t2.up()
    t2.goto(-50, 80)
    t2.seth(45)
    t2.down()

# drawing top heart

    t2.fd(7)
    t2.begin_fill()

    for i in range(25):   # top left of heart
        t2.fd(2)
        t2.rt(7)

    for i in range(2):  # left side of heart
        t2.fd(15)
        t2.rt(2)

    for i in range(15):   # bottom of heart
        t2.fd(1)
        t2.rt(6)

    for i in range(2):    # right side of heart
        t2.fd(15)
        t2.rt(2)

    for i in range(25):    # right curve of heart
        t2.fd(2)
        t2.rt(7)

    t2.fd(5)
    t2.end_fill()

    t2.ht()

# drawing lower heart

    # setting position of turtle

    t2.up()
    t2.goto(-50, 20)
    t2.seth(45)
    t2.down()

    t2.begin_fill()

    for i in range(25):   # heart right top
        t2.fd(2)
        t2.rt(7)

    for i in range(2):    # heart right side
        t2.fd(15)
        t2.rt(2)

    for i in range (15):   # bottom of heart
        t2.fd(1)
        t2.rt(6)

    for i in range(2):    # left side
        t2.fd(15)
        t2.rt(2)

    for i in range(25):    # heart left curve
        t2.fd(2)
        t2.rt(7)

    t2.fd(5)

    t2.end_fill()


def eyes():

    t3=turtle.Turtle()        # setting up turtle
    t3.color("#656265")      # grey
    t3.up()
    t3.ht()
    t3.goto(-5,-122)
    t3.seth(40)
    t3.down()

    t3.begin_fill()

# drawing eyes

    for i in range(50):    # left side eye
        t3.fd(1)
        t3.rt(8)

    t3.end_fill()

    t3.up()                # setting turtle position
    t3.goto(-25,-120)
    t3.seth(200)
    t3.down()

    t3.begin_fill()

    t3.circle(15,130)   # left oval eye
    t3.circle(5,50)
    t3.circle(15,130)
    t3.circle(5, 50)

    t3.end_fill()

    t3.up()             # setting turtle position
    t3.goto(-70,-122)
    t3.seth(200)
    t3.down()

    t3.begin_fill()

    for i in range(50):    # right side eye
        t3.fd(1)
        t3.rt(8)

    t3.end_fill()

    t3.up()            # setting turtle position
    t3.goto(-55,-120)
    t3.seth(200)
    t3.down()

    t3.begin_fill()

    t3.circle(15,130)   # right oval eye
    t3.circle(5,50)
    t3.circle(15,130)
    t3.circle(5, 50)

    t3.end_fill()


def flower():
    t4=turtle.Turtle()       # setting up turtle
    t4.up()
    t4.goto(200, -150)
    t4.color("#F1DF77")      # pale yellow
    t4.down()

    t4.begin_fill()

# drawing first flower

    # middle of flower

    t4.circle(10)
    t4.end_fill()
    t4.color("pink")
    t4.seth(150)

    for i in range(10):  # function to make petals
        t4.circle(15, 130)
        t4.circle(5, 50)
        t4.circle(15, 130)
        t4.circle(5, 50)
        t4.fd(5)
        t4.rt(35)

    # making the stem

    t4.pensize(3)
    t4.color("green")
    t4.seth(200)
    t4.circle(40, 130)
    t4.circle(-40, 130)

    # set position of turtle

    t4.up()
    t4.goto(250, 50)
    t4.seth(143.13)

# make second flower

    t4.pensize(1)
    t4.down()
    t4.color("#F1DF77")
    t4.begin_fill()
    t4.circle(10)
    t4.end_fill()
    t4.color("pink")
    t4.seth(-40)

    for i in range(10):  # function to make petals
        t4.down()
        t4.circle(15, 130)
        t4.circle(5, 50)
        t4.circle(15, 130)
        t4.circle(5, 50)
        t4.fd(5)
        t4.rt(35)

    # setting position of turtle for stem

    t4.up()
    t4.color("green")
    t4.fd(5)
    t4.rt(90)
    t4.fd(20)
    t4.seth(200)
    t4.down()
    t4.pensize(3)

    # drawing stem
    t4.circle(40, 130)
    t4.circle(-40, 130)

    # set position of turtle

    t4.up()
    t4.goto(290, 200)
    t4.seth(143.13)

# make third flower

    t4.pensize(1)
    t4.down()
    t4.color("#F1DF77")
    t4.begin_fill()
    t4.circle(10)
    t4.end_fill()
    t4.color("pink")
    t4.seth(-40)

    for i in range(10):  # function to make petals
        t4.down()
        t4.circle(15, 130)
        t4.circle(5, 50)
        t4.circle(15, 130)
        t4.circle(5, 50)
        t4.fd(5)
        t4.rt(35)

    # setting position for stem
    t4.up()
    t4.color("green")
    t4.fd(5)
    t4.rt(90)
    t4.fd(20)
    t4.seth(200)
    t4.down()

    # drawing stem

    t4.pensize(3)
    t4.circle(40, 130)
    t4.circle(-40, 130)

    # setting turtle position

    t4.up()
    t4.goto(-200, -130)
    t4.seth(143.13)

# making fourth flower

    t4.down()
    t4.pensize(1)
    t4.color("#F1DF77")
    t4.begin_fill()
    t4.circle(10)
    t4.end_fill()
    t4.color("pink")
    t4.seth(-40)

    for i in range(10):  # function to make petals
        t4.down()
        t4.circle(15, 130)
        t4.circle(5, 50)
        t4.circle(15, 130)
        t4.circle(5, 50)
        t4.fd(5)
        t4.rt(35)

    # setting turtle position for stem

    t4.up()
    t4.color("green")
    t4.fd(5)
    t4.rt(90)
    t4.fd(20)
    t4.seth(200)
    t4.pensize(3)
    t4.down()

    # drawing stem
    t4.circle(40, 130)
    t4.circle(-40, 130)

    t4.ht()


def main():

    spider()
    eyes()
    hearts()
    flower()

    ts=turtle.Screen()
    ts.exitonclick()


main()
