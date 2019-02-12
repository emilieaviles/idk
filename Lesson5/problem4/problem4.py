from turtle import *

ihatethis = Turtle()

ihatethis.color("black")
ihatethis.pensize(4)
ihatethis.shape("turtle")
ihatethis.speed(7)

def drawHexagon(side):
	for x in range(6):
		ihatethis.forward(side)
		ihatethis.left(60)

for y in range(25,200,25):
	drawHexagon(y)

mainloop()