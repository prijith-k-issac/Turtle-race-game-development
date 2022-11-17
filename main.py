import turtle
from turtle import Turtle, Screen
import random
s= Screen()


s.setup(width = 500, height = 400)
color = [ "red", "blue", "green", "yellow", "orange"]
user_bet = s.textinput(title = "Welcome to Turtle Race", prompt="Choose the color of turtle that you \
supports. [Colors available are : red, blue, green, yellow, orange]")
is_raise_on = True
y_axis_position = [-100, -50, 0, 50, 100]
all_turtle = []


for turtle_index in range(5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color[turtle_index])
    new_turtle.goto(-230, y_axis_position[turtle_index])
    all_turtle.append(new_turtle)

while is_raise_on:

    if turtle.xcor() > 160:
        is_raise_on = False
        if turtle.pencolor() == user_bet:
            print(f"Your {user_bet} turtle has won the match,congratulations")
        else:
            print(f"Your {user_bet} turtle lost the match.")

    for turtle in all_turtle:
        distance = random.randint(0, 10)
        turtle.forward(distance)


s.exitonclick()