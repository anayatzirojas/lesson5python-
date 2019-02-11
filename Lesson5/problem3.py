from turtle import*
import random
yaya= Turtle()

def drawhexagon():
	for x in range(6):
		yaya.forward(100)
		yaya.left(60)

drawhexagon()

mainloop()