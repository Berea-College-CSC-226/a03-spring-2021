#################################################################################
# Author: Faisal Kimbugwe
#
# Username:Kimbugwef,
#
# Assignment:T03: Boustrophedon Turtles and Functions
# Purpose:Explore functions in Python
# Google doc: https://docs.google.com/document/d/1qwa13_TLXOfNajBpRWFvpfNPlJGQ3zjhr1_mjwwLB_Q/edit?usp=sharing
#################################################################################
# Acknowledgements:
#
#
#
#################################################################################

import turtle


def draw_rectangle(t, height, width):
    """
        function to draw the outer square of the assignment
        :param width: distance
        :param height: distance
        :param t: a Turtle object
        :return: None
        """

    t.color("black")
    # t.pensize(3)
    t.color("Black", "#996633")
    t.begin_fill()
    for i in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()


def dimension_3_top(dim):
    """
    This function make the to 3d
    :param dim: a Turtle object
    :return: None
    """
    dim.color("Black", "#996633")
    dim.begin_fill()
    dim.left(90)
    dim.forward(10)
    dim.left(90)
    dim.forward(350)
    dim.left(30)
    dim.forward(120)
    dim.left(60)
    dim.forward(10)
    dim.left(120)
    dim.forward(120)
    dim.right(30)
    dim.forward(350)
    dim.end_fill()


def draw_tabletop(table):
    """
    This function draws the Top of the table.
    :param table: a Turtle object
    :return: None
    """
    table.left(180)
    # table.color("#996638")
    table.color("Black", "#996638")
    table.begin_fill()
    for side in range(2):
        table.right(150)
        table.forward(120)
        table.right(30)
        table.forward(350)
    table.end_fill()
    dimension_3_top(table)
    # ...


def make_text(sape, txt):
    """
    Writes text to the screen.

    :param txt: a string to be put in later
    :param sape: a Turtle object
    :return: None
    """
    # sape.color(0,0,0)
    # sape.up()
    # sape.setpos(-50,120)
    # sape.down()
    sape.write(txt, move=False, align='center', font=("Arial", 12, ("bold", "normal")))


def drawer_bottom(shape):
    """
    draws a fancy design at bottom of drawers.

    :param shape: a Turtle object
    :return: None
    """
    shape.color("black")
    shape.left(90)
    shape.forward(30)
    shape.left(90)
    shape.forward(130)
    shape.left(90)
    shape.forward(30)
    shape.left(90)
    shape.forward(25)
    shape.left(90)
    shape.forward(15)
    shape.right(90)
    shape.forward(80)
    shape.right(90)
    shape.forward(15)
    shape.left(90)
    shape.forward(25)


def side_table(side):
    """
    This function to draw side of table
    :param side: a Turtle object
    :return: None
    """
    # drawing the other side of table
    side.up()
    side.goto(150, -200)
    side.left(180)
    side.down()
    side.color("black", "#996638")
    side.begin_fill()
    side.right(150)
    side.forward(100)
    side.left(60)
    side.forward(200)
    side.left(120)
    side.forward(100)
    side.left(60)
    side.forward(200)
    side.end_fill()


def draw_drawer(drawer):
    """
    This function draws drawers for the table
    :param drawer: a Turtle object
    :return: None
    """
    draw_rectangle(drawer, 200, 150)
    pos = drawer.position()
    draw_rectangle(drawer, 200, 10)
    drawer.up()
    drawer.forward(140)
    drawer.down()

    draw_rectangle(drawer, 200, 10)

    drawer_bottom(drawer)

    # sets and draws drawer 3
    drawer.up()
    drawer.left(90)
    drawer.forward(35)
    drawer.down()
    draw_rectangle(drawer, 130, 80)

    p = drawer.position()  # introduced a variable p for this location as i will return to it

    # setting position for text for the drawer label
    drawer.up()
    drawer.left(90)
    drawer.forward(65)
    drawer.right(90)
    drawer.forward(40)
    drawer.down()
    make_text(drawer, "drawer 3")

    # draws drawer 2
    drawer.up()
    drawer.goto(p)
    drawer.forward(85)
    drawer.down()
    draw_rectangle(drawer, 130, 70)

    # setting position for text and labeling the drawer. I aimed for the center
    drawer.up()
    drawer.left(90)
    drawer.forward(65)
    drawer.right(90)
    drawer.forward(35)
    drawer.down()
    make_text(drawer, "drawer 2")

    # position change for the next part of the drawing
    drawer.up()
    drawer.goto(pos)
    drawer.forward(200)
    drawer.left(90)
    drawer.down()

    drawer.forward(190)  # just a connector

    draw_rectangle(drawer, 200, 10)  # draws a leg or table stand

    pos2 = drawer.position()  # introduced the pos2 variable as i return to this position later on

    # draws a drawer
    drawer.up()
    drawer.forward(-190)
    drawer.down()
    draw_rectangle(drawer, 70, 190)

    # labeling the drawers
    drawer.up()
    drawer.forward(95)
    drawer.left(90)
    drawer.forward(35)
    drawer.down()
    make_text(drawer, "drawer 1")

    drawer.left(90)  # changes the heading for the side function

    side_table(drawer)  # Calls function to draw a side of the table

    drawer.up()
    drawer.goto(pos2)
    drawer.right(90)
    drawer.forward(20)
    drawer.down()
    # ...


# Draw_drawer(mup)

def main():
    """
    Docstring for main
    """
    wn = turtle.Screen()
    wn.bgcolor('LightGreen')

    mup = turtle.Turtle()
    # sets the position for the pen to draw
    mup.up()
    mup.goto(0, -200)
    mup.down()
    draw_drawer(mup)
    mup.right(180)
    draw_tabletop(mup)

    wn.exitonclick()


main()
