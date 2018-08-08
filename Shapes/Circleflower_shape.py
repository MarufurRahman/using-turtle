#Making circleflower shape using turtle
#Programmed by Marufur Rahman

import turtle

#create window and set title of window
wn = turtle.Screen() 
wn.title('Circle Flower')
t = turtle.Turtle()

#shape is loop for 100 times
for i in range(100):
	t.circle(5*i)
	t.circle(-5*i)
	turtle.left(i)

#wait for user to end
turtle.exitonclick()