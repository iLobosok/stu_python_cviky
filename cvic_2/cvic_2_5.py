import math
import turtle

t = turtle.Turtle()
t.speed(0)
# uloha 1
def arc(t,r,angle):
    for _ in range(angle):
        turtle.forward(r)
        turtle.right(90 / angle)

arc(t,5.0,4)