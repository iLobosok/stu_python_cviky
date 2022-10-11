import turtle
t = turtle.Turtle()
t.speed(1000)
count = 30
for i in range (count):
    for i in range(count):
        t.forward(20)
        t.right(360/count)
    t.left(360/count)
t.done