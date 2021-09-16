import turtle

count1=-40
count2=40

while(count1> -260):
    turtle.forward(200)
    turtle.penup()
    turtle.goto(0,count1)
    count1 = count1 - 40
    turtle.pendown()

turtle.penup()
turtle.home()
turtle.right(90)
turtle.pendown()

while(count2< 260):
    turtle.forward(200)
    turtle.penup()
    turtle.goto(count2, 0)
    count2 = count2 + 40
    turtle.pendown()
