import turtle

# set window size
turtle.setup(800, 600)

# get reference to turtle window
window = turtle.Screen()
window.bgcolor('blue')

# set window title bar
window.title('My First Turtle Graphics Program')

the_turtle = turtle.getturtle()
the_turtle.hideturtle()
turtle.colormode(255)
the_turtle.pencolor(238, 0, 0)

the_turtle.setposition(100, 0)
the_turtle.setposition(100, 100)
the_turtle.setposition(0, 100)
the_turtle.setposition(0, 0)

turtle.exitonclick()

#raw_input()
