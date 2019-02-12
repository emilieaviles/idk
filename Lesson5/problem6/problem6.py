from turtle import *

metro = Turtle()

metro.shape("turtle")
metro.pensize(5)
metro.color("blue")
metro.speed(9)

def drawStar():
	for x in range(5):
		metro.forward(50)
		metro.left(144)

for y in range(3):
	drawStar()
	metro.penup()
	metro.forward(80)
	metro.pendown()

mainloop()