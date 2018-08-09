#Making square shape using turtle
#Programmed by Marufur Rahman.

import turtle

#create window and set title of window
wn = turtle.Screen()
wn.title('Square')
t = turtle.Turtle()

#shape is lope for 8 times
for i in range(32):
	t.forward(100)
	t.right(90)

#wait for user to end
turtle.exitonclick()
