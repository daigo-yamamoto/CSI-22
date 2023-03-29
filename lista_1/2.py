import turtle

wn = turtle.Screen()
wn.screensize(200, 200, 'light green')
t = turtle.Turtle()
t.color('hot pink')
t.pensize(3)


def draw_poly(t, n, sz):
    for lado in range(n):
        t.forward(sz)
        t.lt(360 / n)


draw_poly(t, 8, 50)
wn.mainloop()
