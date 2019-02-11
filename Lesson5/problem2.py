from turtle import*
import random
yaya= Turtle()

def drawtriangle():
	for x in range(3):
		yaya.forward(100)
		yaya.left(120)

for x in range(12):
	drawtriangle()
	yaya.left(30)

mainloop()