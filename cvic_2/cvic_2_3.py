# uloha 3 with corners
import math
import turtle

t = turtle.Turtle()
t.speed(0)
# uloha 1
def square(length, n):
    for i in range(n):
        t.fd(length)
        t.right(360/n)
#uloha 2
def bob(length, n):
    square(length, n)

bob(100, 5)
t.hideturtle()
turtle.mainloop()