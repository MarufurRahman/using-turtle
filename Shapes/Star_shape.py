#Making star shape using turtle
#Programmed by Marufur Rahman.

import turtle

#create window and set title of window
wn = turtle.Screen() 
wn.title('Star')
t = turtle.Turtle()

#shape is loop for 8 times
for i in range(32):
	t.forward(100)
	t.right(150)

#wait for user to end
turtle.exitonclick()
