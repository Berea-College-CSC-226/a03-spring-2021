#Author: Draper Williams
#Username: williamsd2
#Google Doc Link: https://docs.google.com/document/d/1GR6GDkJ5CX9l9mPnJlzY8FL--fvOCdnbqLUZOOETwjc/edit?usp=sharing



import turtle  # import the turtle



def make_cube():
    """ draws cube"""
    drape.penup()
    drape.forward(50)
    drape.pendown()

    for i in range(4): # Makes first square
        drape.forward(100)
        drape.right(90)

    for i in range(1): # creates the remaining 2 squares to form 3D model

        drape.left(10)
        drape.forward(80)
        drape.right(10)
        drape.forward(90)
        drape.right(90)
        drape.fd(100)
        drape.right(79)
        drape.fd(73)
        drape.penup()
        drape.right(100)
        drape.fd(100)
        drape.pendown()
        drape.right(82)
        drape.forward(75)


def box_lines(): #adds in the line on the right square
    for i in range (1):
        drape.penup()
        drape.right(102.5)
        drape.pendown()
        drape.forward(35)
        drape.right(70)
        drape.fd(73)
        drape.right(17.5)
        drape.fd(96)
        drape.penup()


    for i in range(1): #adds in the gridline for the front square

        drape.pencolor('orange')
        drape.pensize(3)
        drape.left(90)
        drape.fd(58)
        drape.right(-90)
        drape.forward(49.5)
        drape.left(90)
        drape.pendown()
        drape.fd(100)
        drape.penup()
        drape.back(100)
        drape.right(90)
        drape.fd(45)
        drape.right(-10.5)
        drape.fd(45)

        drape.pencolor('maroon')
        drape.pensize(6)

        drape.right(280)
        drape.pendown()
        drape.fd(100)
        drape.left(90)

        drape.pencolor('purple')
        drape.pensize(2)
        drape.forward(100)
        drape.backward(50)
        drape.left(10)
        drape.forward(50)
        drape.penup()
        drape.backward(50)
        drape.pendown()
        drape.backward(50)

win = turtle.Screen() # creates turtle screen, sets background color and rgb colormode
win.bgcolor('black')
win.colormode(255)



drape = turtle.Turtle() #turtle attributes such as shape, pen color (RGB- chartreuse green), and pen size
drape.shape("turtle")

drape.pencolor(127,255,0)
drape.fillcolor('orange')
drape.pensize(2)

turtle.color('brown')  # adds text on screen, specifies font, size, alignment
style = ('Courier', 30, 'bold')
turtle.write('Boxxy Brown!', font=style, align='right')
turtle.hideturtle()




def main(): #calls cube and box line function
    make_cube()
    box_lines()

main()


