from turtle import*
import random

bgcolor ("black")

def triangle (traingle_size):
    for i in range(1):
        forward(100)
        left (90)
        forward (100)
        left (135)
        forward (142)

for n in range (100):
    speed(15)
    penup()
    goto(random.triangular(-400, 400), random.triangular(-400, 400))
    pendown()


    red_amount = random.triangular(0.2, 0.0, 0.1)
    blue_amount = random.triangular(0.3, 0.6, 0.0)
    green_amount = random.triangular(0.4, 0.2, 0.0)
    pencolor ((red_amount, blue_amount, green_amount))

    triangle_size = random.triangular (2,10)
    pensize (random.triangular(1, 4))

    for i in range(5):
        triangle (triangle_size)
        left (100)
        right (100)

done()

        

