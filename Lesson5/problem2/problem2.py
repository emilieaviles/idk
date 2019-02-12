from turtle import *

bob = Turtle()

bob.shape("turtle")
bob.color("red")
bob.pensize(2)
bob.speed(9)

def drawTriangle():
	for x in range(3):
		bob.forward(200)
		bob.left(120)

for x in range(12):
	drawTriangle()
	bob.left(30)

mainloop()