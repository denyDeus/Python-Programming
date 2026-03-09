from turtle import *
from colorsys import *

tracer(200)
bgcolor("black")
hideturtle()
pensize(1.5)

for i in range(400):
    color(hsv_to_rgb(i / 500, 0.5, 1))
    for j in range(8):
        circle(20 + i * 0.05, 80)
        right(45)
    right(17)
    forward(i * 0.15)
    circle(15, 180)
    backward(i *  0.1)
done()