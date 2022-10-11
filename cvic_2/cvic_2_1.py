import math
import turtle

t = turtle.Turtle()
t.speed(0)
# uloha 1
def square():
    for i in range(4):
        t.fd(100)
        t.right(90)
#uloha 2
def bob():
    square()

bob()
t.hideturtle()
turtle.mainloop()