import math
import turtle

t = turtle.Turtle()
t.speed(100)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)

# draw flower class and create highest part of picture
def flower(t, n, r, angle):
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0/n)

# draw the lowest part of flower - lists
def list(t, n, r, angle):
    for i in range(n):
        petal(t, r, angle)
        t.lt(180/n)
    t.pd()
    
def list2(t, n, r, angle):
    for i in range(n):
        petal(t, r, angle)
        t.lt(90/n)
    t.pd()

# move turtle cursor 
def move(t, length):
    t.pu()
    t.fd(length)
    t.pd()
# draw middle part of flower
def line(t, distance, angle):
    t.right(90)
    for i in range(angle):
        t.right(30/angle)
        t.fd(distance)
    t.pd()

# main class to draw whole flower
def kvet_class():
    list(t, 2, 50.0, 50.0)
    line(t, 20, 10)
    flower(t, 7, 100.0, 52.0)
def kvet_class2():
    list(t, 2, 40.0, 80.0)
    line(t, 20, 7)
    flower(t, 10, 100.0, 36.0)
def kvet_class3():
    list(t, 2, 40.0, 80.0)
    line(t, 30, 4)
    flower(t, 22, 200.0, 17.0)

def three_flowers():
    t.pu()
    turtle.setpos(0,0)
    t.goto(-150, 0)
    t.pd()
    kvet_class()
    t.pu()
    t.goto(0, 0)
    t.left(30)
    t.pd()
    t.right(90)
    kvet_class2()
    t.pu()
    t.goto(150, 0)
    t.left(30)
    t.pd()
    t.right(90)
    kvet_class3()
    t.pu()
    

three_flowers()

t.hideturtle()
turtle.mainloop()