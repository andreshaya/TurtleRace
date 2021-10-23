from turtle import Turtle, Screen
from random import randint

color = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
is_race_over = False


def make_turtles():
    for i in range(len(color)-1):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(color[i])
        new_turtle.penup()
        turtles.append(new_turtle)


def set_turtles():
    y_start = 100
    for turt in turtles:
        turt.goto(x=-235, y=y_start)
        y_start -= 50


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Enter a color: ").lower()
make_turtles()
set_turtles()

while not is_race_over:
    for turtle in turtles:
        rng = randint(0, 10)
        turtle.forward(rng)
        if turtle.xcor() > 230:
            is_race_over = True
            if user_bet == turtle.pencolor():
                print(f"You've won! {turtle.pencolor().title()} was the winner!")
            else:
                print(f"You've lost. {turtle.pencolor().title()} was the winner.")
screen.exitonclick()
