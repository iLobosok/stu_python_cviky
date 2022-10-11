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


# move turtle cursor 
def move(t, length):
    t.pu()
    t.fd(length)
    t.pd()
# draw middle part of flower
def line(t, distance, angle):
    t.right(90)
    for i in range(distance):
        t.right(90/angle)
        t.fd(distance)
    t.pd()

# main class to draw whole flower
def full_flower1():
    list(t, 2, 70.0, 40.0)
    line(t, 13, 55)
    flower(t, 7, 75.0, 52.0)
def full_flower2():
    list(t, 2, 100.0, 25.0)
    line(t, 12, 55)
    flower(t, 10, 75.0, 52.0)
def full_flower3():
    list(t, 2, 90.0, 70.0)
    line(t, 11, 55)
    flower(t, 15, 75.0, 52.0)

def three_flowers():
   t.setpos(0,0)
   t.pu()
   t.goto(-150, 40)
   t.pd()
   full_flower1()
   t.pu()
   t.goto(0,0)
   t.pd()
   t.right(70)
   full_flower2()
   t.pu()
   t.goto(180, 30)
   t.right(65)
   t.pd()
   full_flower3()
   
   

    

three_flowers()

t.hideturtle()
turtle.mainloop()