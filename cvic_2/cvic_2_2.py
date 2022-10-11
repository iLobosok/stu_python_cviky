import math
import turtle

t = turtle.Turtle()
t.speed(0)
# uloha 1
def square(length):
    for i in range(4):
        t.fd(length)
        t.right(90)
#uloha 2
def bob(length):
    square(length)

bob(100)
t.hideturtle()
turtle.mainloop()