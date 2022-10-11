import math
import turtle

t = turtle.Turtle()
t.speed(0)
# uloha 1
def circle(t,r,n):
    for _ in range(n):
        turtle.forward(r)
        turtle.right(360 / n)

circle(t,5.0,100)