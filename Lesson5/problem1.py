from turtle import*
import random
yaya = Turtle()

def drawtriangle():
	for x in range(3):
		yaya.forward(100)
		yaya.left(120)
yaya.color("orange")

drawtriangle()
mainloop()