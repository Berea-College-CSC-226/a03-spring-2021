"""
Collin Brown
brownc2
https://docs.google.com/document/d/1k7m8y_MAuB7psh1uGAU1rcZuKVMNPIBr6GtQE08DsAc/edit?usp=sharing
NOTE: Maximize the screen to see the whole picture!
"""

import turtle


def main():
    groundturtle = turtle.Turtle()                  # Creates 3 turtles, each assigned different roles in the picture's creation
    houseturtle = turtle.Turtle()
    treeturtle = turtle.Turtle()

    turtledisplay = turtle.Screen()                 # Sets up the window
    turtledisplay.colormode(255)
    turtledisplay.bgcolor((92, 175, 252))

    groundturtle.color((0, 143, 0))                 # Assigns colors to the turtles
    houseturtle.color((165, 145, 88))
    treeturtle.color((75, 40, 0))

    groundturtle.hideturtle()                       # Makes the turtles invisible
    houseturtle.hideturtle()
    treeturtle.hideturtle()

    groundturtle.pensize(30)                        # Prepares the ground turtle
    groundturtle.penup()
    groundturtle.speed(5)
    groundturtle.setpos(-700, -350)
    groundturtle.pendown()

    def draw_ground():
        """Draws green grass boustrophedonically"""
        for i in range(3):
            groundturtle.forward(1450)
            groundturtle.left(90)
            groundturtle.forward(25)
            groundturtle.left(90)
            groundturtle.forward(1450)
            groundturtle.right(90)
            groundturtle.forward(25)
            groundturtle.right(90)

    def draw_window_pane():
        """Draws and fills in 4 white window panes"""
        houseturtle.begin_fill()
        for y in range(4):
            houseturtle.pendown()
            houseturtle.forward(35)
            houseturtle.left(90)
            houseturtle.penup()
        houseturtle.end_fill()

    def draw_house():
        """Draws the house, the roof, the door, and the window frame"""
        houseturtle.begin_fill()
        for i in range (4):                     # Draws the house
            houseturtle.forward(200)
            houseturtle.left(90)
            houseturtle.forward(300)
            houseturtle.left(90)

        houseturtle.end_fill()                  # Gets ready to draw the door
        houseturtle.penup()
        houseturtle.color(106, 65, 5)
        houseturtle.forward(87)
        houseturtle.left(90)
        houseturtle.pendown()
        houseturtle.begin_fill()

        for q in range(2):                      # Draws the door and fills it
            houseturtle.forward(75)
            houseturtle.right(90)
            houseturtle.forward(30)
            houseturtle.right(90)

        houseturtle.end_fill()

        houseturtle.penup()                     # Positions the turtle to draw the roof
        houseturtle.setpos(0, 100)
        houseturtle.color(43, 17, 5)
        houseturtle.pendown()
        houseturtle.setx(-200)
        houseturtle.right(180)

        houseturtle.begin_fill()                # Draws and fills in the roof
        houseturtle.setpos(0, 200)
        houseturtle.setpos(200, 100)
        houseturtle.setpos(-200, 100)
        houseturtle.end_fill()

        houseturtle.penup()                     # Draws the window frame; will be filled in with draw_window_pane
        houseturtle.setpos(0, 35)
        houseturtle.color(100, 100, 100)
        houseturtle.pensize(5)
        houseturtle.pendown()
        houseturtle.forward(80)
        houseturtle.forward(-40)
        houseturtle.right(90)
        houseturtle.forward(40)
        houseturtle.forward(-80)
        houseturtle.right(90)
        houseturtle.forward(5)
        houseturtle.color("white")

        draw_window_pane()                      # Fills in a pane of the window frame with a white square

        houseturtle.setpos(40, -45)             # Next 3 lines are filling in the rest of the frame
        draw_window_pane()

        houseturtle.setpos(-5, -45)
        draw_window_pane()

        houseturtle.setpos(-5, 0)
        draw_window_pane()

        houseturtle.setpos(45, 40)              # Prepares to draw square around the window to finish the framing
        houseturtle.color(100, 100, 100)
        houseturtle.pendown()
        houseturtle.left(90)

        for u in range(4):                      # Draws the square
            houseturtle.forward(90)
            houseturtle.left(90)

    def draw_tree():
        "Creates a tree trunk as well as leaves"
        treeturtle.begin_fill()
        for t in range(2):                      # Draws the trunk
            treeturtle.forward(350)
            treeturtle.right(90)
            treeturtle.forward(40)
            treeturtle.right(90)
        treeturtle.end_fill()
        treeturtle.penup()
        treeturtle.forward(350)                 # Moves the turtle into position to create circular leaves
        treeturtle.right(90)
        treeturtle.forward(120)
        treeturtle.left(90)
        treeturtle.forward(50)
        treeturtle.color(20, 80, 30)
        treeturtle.pendown()
        treeturtle.begin_fill()
        treeturtle.circle(100)                  # Creates the leaves
        treeturtle.end_fill()
        treeturtle.penup()
        treeturtle.color(75, 40, 0)
        treeturtle.pendown()

    houseturtle.pensize(15)                         # Changes appearance and moves the turtle into position to draw grass
    houseturtle.penup()
    houseturtle.speed(5)
    houseturtle.setpos(-100, -202)
    houseturtle.pendown()

    draw_ground()                                   # Draws the grass

    draw_house()                                    # Draws the house

    treeturtle.pensize(10)                          # Prepares the turtle for the draw_tree function
    treeturtle.penup()
    treeturtle.speed(5)
    treeturtle.left(90)
    treeturtle.setpos(-450, -250)                   # Moves the turtle into position to begin drawing
    treeturtle.pendown()
    treeturtle.forward(-40)

    draw_tree()
    treeturtle.penup()
    treeturtle.setpos(437, -290)
    treeturtle.penup()
    draw_tree()

    turtledisplay.exitonclick()


main()
