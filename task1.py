import turtle

# Create a Turtle object
t = turtle.Turtle()

# Move the pen to the starting position
t.penup()
t.goto(-100, 0)
t.pendown()

# Draw a triangle
for i in range(3):
    t.forward(100)
    t.left(120)

# Hide the Turtle object and exit
t.hideturtle()
turtle.done()
