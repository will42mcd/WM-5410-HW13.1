import turtle
from koch import *

size = 300  # Length of each side of the initial triangle
order = 2  # Depth of recursion

def main():
    screen = turtle.Screen()
    screen.setup(size+100, size+100)
    screen.screensize(size, size)
    screen.bgcolor("light green")
    screen.title("Blue Koch Snowflake")
    
    turtle.speed(100)
    turtle.penup()
    turtle.goto(-size / 2, size / 3)
    turtle.pendown()
    turtle.color("blue")
    
    koch_snowflake(turtle, order, size)
    
    turtle.hideturtle()
    turtle.done()


if __name__ == "__main__":
    main()