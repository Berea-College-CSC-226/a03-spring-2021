######################################################################
# Author: Silas Fair

# Username: silasfair121221

# Purpose: to explore functions.
# Assignment: a03 Robotic Turtles
# Google doc: https: // docs.google.com / document / d / 1KDIwNwJADTEgJYi7NEQmzvrbp5VQgv77enoHrVa4nX4 / edit?usp = sharing
######################################################################
import turtle


def draw_rectangle(t, w, h, col):
        """
        make t draw a rectangle of w width, h height and col color
        """
        t.fillcolor(col)
        t.begin_fill()
        t.fd(w)
        t.right(90)
        t.fd(h)
        t.right(90)
        t.fd(w)
        t.right(90)
        t.fd(h)
        t.end_fill()

def draw_eyes(t, wn):
        """
        make turtle 't' draw eyes
        """
        wn.colormode(255)
        eye_whites_color = (254, 240, 227)
        eye_pupil_color = (0,0,0)
        t.fillcolor(eye_whites_color)
        t.penup()
        t.fd(100)
        t.pendown()
        t.begin_fill()
        t.circle(20)
        t.end_fill()
        # pupil
        t.fillcolor(eye_pupil_color)
        t.begin_fill()
        t.circle(12)
        t.end_fill()
        t.penup()
        t.fd(-200)
        t.pendown()
        t.fillcolor(eye_whites_color)
        t.begin_fill()
        t.circle(20)
        t.end_fill()
        # pupil
        t.fillcolor(eye_pupil_color)
        t.begin_fill()
        t.circle(12)
        t.end_fill()


def draw_nose_and_mouth(t, wn):
        """
        make turtle 't' draw nose and mouth
        """
        wn.colormode(255)
        t.color((0,0,0))
        t.seth(250)
        t.fd(100)
        t.seth(0)
        t.fd(25)
        # start drawing mouth
        t.seth(270)
        t.penup()
        t.fd(10)
        t.pendown()
        t.seth(0)
        t.back(100)
        wn.colormode(255)
        lip_color = (191, 112, 104)
        draw_rectangle(t, 200, 10, lip_color)
        t.seth(270)
        t.fd(20)
        t.seth(0)
        draw_rectangle(t, 200, 20, lip_color)


def draw_head(t, sz, wn):
        """draw the head"""
        wn.colormode(255)
        skin_color = (229, 194, 152)
        t.fillcolor(skin_color)
        t.seth(90)
        t.fd(sz)
        t.seth(180)
        t.fd(sz/2)
        t.seth(0)
        t.begin_fill()
        for i in range(8):
                t.fd(sz)
                t.right(45)
        t.end_fill()


def draw_hair(t):
        """Draw the hair"""
        t.seth(90)
        t.fd(170)
        t.speed("fastest")
        for i in range(100):
                t.fd(20+i)
                t.right(i+100)



def main():
        wn = turtle.Screen()
        wn.colormode(255)
        wn.bgcolor(100,233,122)
        head = turtle.Turtle()
        head.speed("fastest")
        hair = turtle.Turtle()
        nose_mouth = turtle.Turtle()
        nose_mouth.speed("fastest")
        eyes = turtle.Turtle()
        eyes.speed("fastest")

        # call the drawing functions
        draw_head(head,180,wn)
        draw_eyes(eyes, wn)
        draw_nose_and_mouth(nose_mouth, wn)
        draw_hair(hair)

        turtle.exitonclick()


main()

