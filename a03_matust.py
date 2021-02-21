##########################################################################################
# Name: Tallis Matus
# Username: Matust
#########################################################################################


import turtle
wn = turtle.Screen()
wn.bgcolor("purple")


def person():
    sam = turtle.Turtle()
    sam.color("#6464C8")
    sam.speed(0)
    sam.left(80)
    sam.forward(40)
    sam.right(80)
    sam.forward(20)
    sam.right(80)
    sam.forward(40)
    sam.back(40)
    sam.left(80)
    sam.back(10)
    sam.left(90)
    sam.forward(30)
    sam.left(60)
    sam.forward(25)
    sam.back(25)
    sam.right(120)
    sam.forward(25)
    sam.back(25)
    sam.left(60)
    sam.forward(30)
    sam.penup()
    sam.forward(20)
    sam.right(90)
    sam.forward(20)
    sam.left(90)
    sam.pendown()
    sam.circle(20)


def text():
    sam = turtle.Turtle()
    sam.color("#6464C8")
    sam.penup()
    sam.setpos(-10.0, -40.0)
    sam.pendown()
    sam.pensize(50)
    sam.write("Hello!", font=("bold", 20, "normal"))


def main():
    person()
    text()


main()

wn.exitonclick()
