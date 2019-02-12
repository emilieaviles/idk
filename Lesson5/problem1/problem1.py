from turtle import *

chair = Turtle()

chair.shape("turtle")
chair.color("red")
chair.pensize(2)
chair.speed(6)

def drawTriangle():
	for x in range(3):
		chair.forward(200)
		chair.left(120)

for x in range(1):
	drawTriangle()

mainloop()