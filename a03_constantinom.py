#######################################################
# name: Micho Constantino
# username: constantinom
# doc link: https://docs.google.com/document/d/1vuegWv-k0J4_CCc6qPWSErOHajUehTDOTZVA5x3lb90/edit?usp=sharing
#######################################################
# notes to self
# drawing ricks, image waves background
# eyebrows defined, lip lines defined, pupils, dimple
# use rgb or hexadecimal
# ~ ~ ~

import turtle


def up(a03):
    a03.penup()

def make_headshape(a03):
    """
    give annaleigh's head a shape (black outline)
    :return: none
    """
    up(a03)
    a03.setpos(0,-50)
    a03.pensize(2)
    a03.pendown()

    a03.color("black", "purple")
    a03.begin_fill()
    a03.circle(70)
    a03.end_fill()
    up(a03)
    # describe

def make_nose(a03):
    '''
    My person's nose (black pen)
    :return: none
    '''
    up(a03)
    a03.setpos(0, 0)  # turtle will start making nose at (0,0)
    a03.speed(0)
    a03.pencolor("black")  # nose will be black
    a03.pendown()
    a03.fd(20)
    a03.lt(110)
    a03.fd(40)
    up(a03)
    # this makes Annaleigh's nose

def make_eyes(a03):
    """
    making annaleigh's eyes in cornflower blue
    :return: none
    """
    a03.shape("circle")
    up(a03)                 #making the first eye (right)
    a03.setpos(40,40)
    a03.pencolor(100,149,237)
    a03.pendown()
    a03.circle(10)
    up(a03)

    a03.setpos(38,38)           #making eyeball
    a03.color(100,149,237)
    a03.pendown()
    a03.begin_fill()
    a03.circle(5)
    a03.end_fill()
    up(a03)

    a03.setpos(-25,40)  #making left eye
    a03.color(100,149,237)
    a03.pendown()
    a03.circle(10)
    up(a03)

    a03.setpos(-28, 38)         #making eyeball
    a03.color(100,149,237)
    a03.pendown()
    a03.begin_fill()
    a03.circle(5)
    a03.end_fill()
    up(a03)
    a03.hideturtle()
    a03.setpos(0,0)

def make_eyebrows(a03):
    """
    annaleigh gets some thick 'indian red' eyebrows
    :param a03: 
    :return: none
    """
    up(a03)
    a03.setpos(15,55)
    a03.color(205,92,92)
    a03.pensize(5)

    a03.pendown()           #making right eyebrow
    a03.rt(100)
    a03.fd(20)
    a03.rt(45)
    a03.fd(10)

    up(a03)               # making left eyebrow
    a03.setpos(-13,55)
    a03.pendown()
    a03.lt(200)
    a03.fd(20)
    a03.lt(45)
    a03.fd(10)

def make_lips(a03):
    """
    giving annaleigh 'medium sea green' lips
    :param a03: 
    :return: none
    """
    up(a03)
    a03.setpos(0,-20)
    a03.color(60,179,113)
    a03.pensize(1)

    a03.pendown()
    a03.begin_fill()
    a03.rt(20)
    a03.fd(20)          # top first lip line

    a03.lt(160)
    a03.fd(26)          # first bottom lip line

    a03.lt(35)
    a03.fd(30)          # second bottom lip line

    a03.lt(160)
    a03.fd(20)          # second top line

    a03.lt(30)
    a03.fd(7)           # lip heart
    a03.rt(40)
    a03.fd(7)           # lip heart
    a03.end_fill()

def make_rightside_hair(a03):
    """
    giving annaleigh some hair
    :param a03:
    :return: none
    """
    up(a03)
    a03.pensize(4)
    a03.setpos(70,-50)

    a03.pendown()
    a03.color("black", "blue")
    a03.begin_fill()
    a03.lt(180)
    a03.fd(30)                      # bottom part of hair on rt

    a03.lt(110)
    a03.fd(155)                     # long part of hair on rt

    a03.lt(60)
    a03.fd(60)                      # wrapping over head
    a03.lt(25)
    a03.fd(50)                      # still wrapping

    a03.lt(90)
    a03.fd(30)                      # making the split in hair
    a03.lt(75)
    a03.fd(90)                      # going over forehead

    a03.rt(75)
    a03.fd(115)                     # closing rt side hair
    a03.end_fill()
    up(a03)

def make_leftside_hair(a03):
    """
    giving annaleigh some hair on her left side
    :return: none
    """
    up(a03)
    a03.setpos(-50,99)
    a03.color("black", "blue")

    a03.pendown()
    a03.begin_fill()
    a03.fd(25)
    a03.rt(20)
    a03.fd(115)
    a03.rt(70)
    a03.fd(30)
    a03.rt(117)
    a03.fd(148)
    a03.end_fill()



def main():
    """
    constructing face
    :return: none
    """

    turtle.colormode(255)  # change color modes
    wn = turtle.Screen()  # Makes a new turtle screen
    wn.title("Meet Annaleigh!")
    wn.bgcolor("pink")
    wn.bgpic("office.gif")

    a03 = turtle.Turtle()
    a03.speed(0)
    make_headshape(a03)
    make_nose(a03)
    make_eyes(a03)
    make_eyebrows(a03)
    make_lips(a03)
    make_rightside_hair(a03)
    make_leftside_hair(a03)
    wn.exitonclick()


main()
