import turtle

wn = turtle.Screen()
wn.screensize(400, 400, 'light green')
t = turtle.Turtle()
t.color('blue')
t.pensize(2)
t.speed(100)

t.penup()
t.goto(-250, 0)
t.pendown()

for i in range(200):
    t.fd(i*2)
    t.rt(90)

t.penup()
t.goto(250, 0)
t.pendown()

for i in range(200):
    t.fd(i*2)
    t.rt(89.5)

wn.mainloop()
