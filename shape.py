import turtle as t

t.speed(0)
t.bgcolor('black')
t.pencolor('red')

for i in range(160):
    t.right(i)
    t.circle(125,i)
    t.forward(i)
    t.right(90)

t.done()