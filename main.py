import random
from turtle  import Turtle, Screen
sides = int(input("how many sides: "))
turtle=Turtle()
screen=Screen()
turtle.speed(0)



for x in range(sides):
    turtle.down()
    turtle.fd(0.1)
    turtle.left(360/sides)

screen.exitonclick()
