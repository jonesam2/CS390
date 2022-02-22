import turtle


def drawStitchesHorizontal(nums):
    x = -300
    y = 300
    turtle.color("red")
    for num in nums:
        if num == 1:
            for j in nums[::2]:  # only iterate half the length of line because you move twice in the loop each time
                turtle.pendown()
                turtle.forward(sizeOfLine)
                turtle.penup()
                turtle.forward(sizeOfLine)
        if num == 0:
            for j in nums[::2]:
                turtle.penup()
                turtle.forward(sizeOfLine)
                turtle.pendown()
                turtle.forward(sizeOfLine)
        turtle.penup()
        y -= sizeOfLine
        turtle.goto(x, y)


def drawStitchesVertical(nums):
    x = -300
    y = 300 + sizeOfLine
    turtle.color("blue")
    turtle.setheading(270)
    turtle.goto(x, y)
    for num in nums:
        if num == 1:
            for j in nums[::2]:
                turtle.pendown()
                turtle.forward(sizeOfLine)
                turtle.penup()
                turtle.forward(sizeOfLine)

        if num == 0:
            for j in nums[::2]:
                turtle.penup()
                turtle.forward(sizeOfLine)
                turtle.pendown()
                turtle.forward(sizeOfLine)

        turtle.penup()
        x += sizeOfLine
        turtle.goto(x, y)


list1 = []
list2 = []
x = -300
y = 300
sizeOfLine = 25


inputForList = input("Please enter an even amount of 0s and 1s for the first list.")

for i in inputForList:
    i = int(i)
    list1.append(i)

inputForList2 = input("Please enter an even amount of 0s and 1s for the second list.")
for i in inputForList2:
    i = int(i)
    list2.append(i)
turtle.Screen()
turtle.penup()
turtle.speed(20)
turtle.goto(x, y)

drawStitchesHorizontal(list1)
drawStitchesVertical(list2)

turtle.hideturtle()
turtle.exitonclick()
