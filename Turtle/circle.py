import turtle

screen = turtle.Screen()
screen.bgcolor('white')

t = turtle.Turtle()
t.shape('turtle')
t.speed(0)
t.width(2)

def turtle():
    for i in range(100):
        t.circle(100)
        t.rt(5)

turtle()



turtle.done()