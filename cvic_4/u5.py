import turtle

t = turtle.Turtle()
t.speed(100)

def menu():
    znakToInput = input()
    if (znakToInput == 's'):
       for i in range(4):
            t.forward(100)
            t.left(90)

    if (znakToInput == 't'):
       for i in range(3):
            t.forward(200)
            t.left(120)
    else:
        print("Zadali ste neplatny vstup.")

menu()        
turtle.mainloop()