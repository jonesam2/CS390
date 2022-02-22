import random
import turtle

def orientTurtleToHome():
    turtle.pendown()
    turtle.setheading(turtle.towards(x, y))
    turtle.forward(200)
    turtle.penup()


while True:
    turtle.goto(0,0)

    #used to find angles
    angA = random.randint(1,180)
    angB = random.randint(1,180-angA)
    angC = 180 - angA - angB



    #draws triangle and saves coordinates, x, and y values
    # to be used later on
    turtle.pendown()
    turtle.forward(random.randint(1,200))
    corner1 = turtle.pos()
    x1 = turtle.xcor()
    y1 = turtle.ycor()
    turtle.left(180-angA)
    turtle.forward(random.randint(1,200))
    corner2 = turtle.pos()
    x2 = turtle.xcor()
    y2 = turtle.ycor()
    turtle.left(180-angB)
    turtle.goto(0,0)

    turtle.penup()


    #find centroid of triangle
    x = round((x1 + x2 + 0) / 3)
    y = round((y1 + y2 + 0) / 3)

    turtle.pencolor("purple") #change color of lines that bisect angles

    turtle.goto(corner1)
    orientTurtleToHome()

    turtle.goto(corner2)
    orientTurtleToHome()

    turtle.goto(0,0)
    orientTurtleToHome()

    turtle.clear()
    turtle.pencolor("black")