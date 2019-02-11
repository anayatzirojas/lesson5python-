from turtle import*
import random
yaya= Turtle()

def drawhexagon(side):
	for x in range(6):
		yaya.forward(side)
		yaya.left(60)

drawhexagon(20)
drawhexagon(30)
drawhexagon(40)
drawhexagon(50)
drawhexagon(60)
drawhexagon(70)
drawhexagon(80)
drawhexagon(90)
drawhexagon(100)


mainloop()