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

def row():
	for x in range(3):
		drawStar()
		metro.penup()
		metro.forward(80)
		metro.pendown()

for y in range(4):
	row()
	metro.penup()
	metro.backward(240)
	metro.left(90)
	metro.forward(70)
	metro.right(90)
	metro.pendown()

mainloop()