from turtle import *

ihatethis = Turtle()

ihatethis.color("black")
ihatethis.pensize(4)
ihatethis.shape("turtle")
ihatethis.speed(7)

def drawHexagon():
	for x in range(6):
		ihatethis.forward(80)
		ihatethis.right(60)

for y in range(1):
	drawHexagon()

mainloop()