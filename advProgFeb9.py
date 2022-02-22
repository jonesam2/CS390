import turtle
import random
import math


SIDE_LENGTH = 350
NUMBER_SIDES = 3
RADIUS = 50
PI = 3.141592653
NUMBER_RUNS = 300


def triangleArea():
    a = (SIDE_LENGTH/2)**2
    c = (SIDE_LENGTH)**2
    height = math.sqrt(c - a)
    area = 0.5 * (SIDE_LENGTH * height)
    area = round(area, 3)
    return area


def randomTrianglePoints(vertices):
    point1 = vertices[2]#gets points from vertices list
    point2 = vertices[0]
    point3 = vertices[1]
    x = random.random()
    y = random.random()#returns float between 0 & 1
    q = abs(x - y)
    s = q
    t = 0.5 * (x + y - q)
    u = 1 - 0.5 * (q + x + y)  #formula to find barycentric coordinates
    return (s * point1[0] + t * point2[0] + u * point3[0],
            s * point1[1] + t * point2[1] + u * point3[1])




def drawShape(turtle, sLength, sNum):
    angle = 360 / sNum
    vertices = []
    for i in range(sNum):
        turtle.pendown()
        turtle.fd(sLength)
        turtle.right(angle)
        vertices.append(turtle.pos())
    return vertices



def drawCircle(turtle, radius):
    turtle.pendown()
    turtle.circle(radius)


def randomSquarePoints():
    randCoordinates = []
    for run in range(NUMBER_RUNS):
        randX = random.uniform(-150, 200)
        randY = random.uniform(-250, 100)
        coor = (randX, randY)
        randCoordinates.append(coor)
    return randCoordinates

screen = turtle.Screen()
guy = turtle.Turtle()
guy.penup()
guy.goto(-150,100)
vert = drawShape(guy, SIDE_LENGTH, NUMBER_SIDES)
guy.penup()
guy.goto(random.randint(-50, 0), random.randint(-50, 0))
drawCircle(guy, RADIUS)
guy.penup()  #
guy.left(90)  #this gets turtle inside circle to find center
guy.forward(RADIUS)  #
xCenter = guy.xcor()
yCenter = guy.ycor()
circleArea = PI * (RADIUS**2)
if NUMBER_SIDES == 3:
    turtle.speed(100)
    triArea = triangleArea()
    points = [randomTrianglePoints(vert) for i in range(NUMBER_RUNS)]
    hits = 0
    print("Calculating results now...please stand by")
    for point in points:
        turtle.penup()
        turtle.goto(point)
        turtle.dot(4, 'red')
        distance = math.sqrt((xCenter - point[0]) ** 2 + (yCenter - point[1]) ** 2)
        if distance < RADIUS:
            hits += 1
    print("The area of the triangle is", triArea, "units")
    print("The area of the circle is", circleArea, "units")
    print("Actual ratio is:", circleArea / triArea)
    print("Calculated Ratio is:", hits / NUMBER_RUNS)
    print("The difference is:", (circleArea / triArea) -
          (hits / NUMBER_RUNS))
    turtle.exitonclick()
if NUMBER_SIDES == 4:
    corList = randomSquarePoints()
    hits = 0
    print("Calculating results now...please stand by")
    for num in corList:
        turtle.speed(100)
        turtle.penup()
        turtle.goto(num)
        turtle.dot(4, 'red')
        distance = math.sqrt((xCenter - num[0]) ** 2 + (yCenter - num[1]) ** 2)
        if distance < RADIUS:
            hits += 1
    squareArea = SIDE_LENGTH * SIDE_LENGTH
    print("The area of the square is", squareArea, "units")
    print("The area of the circle is", circleArea, "units")
    print("Actual ratio is:", circleArea / squareArea)
    print("Calculated Ratio is:", hits / NUMBER_RUNS)
    print("The difference is:", (circleArea / squareArea) -
          (hits / NUMBER_RUNS))
turtle.exitonclick()
