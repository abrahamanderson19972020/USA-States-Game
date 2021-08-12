from turtle import Turtle, Screen
import pandas as pd
from scoreboard import Scoreboard
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")

screen = Screen()
screen.title("US States Game")
screen.addshape("blank_states_img.gif")
screen.tracer(0)
my_turtle = Turtle()
my_turtle.shape("blank_states_img.gif")
user_score = Scoreboard()
df = pd.read_csv("50_states.csv")
# This returns the location of mouse clicks, by using these click I created a 50_states csv file
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()
guessed_states = list()
states = df["state"].to_list()
print(states)
is_game_on = True
while is_game_on:
    screen.update()
    answer = screen.textinput(title= f"{user_score.score}/50 States Correct ", prompt="What is state's name:")
    if answer.title() == "Exit":
        user_score.color("maroon1")
        user_score.goto(0,0)
        user_score.write(f"You knew {user_score.score} states correctly.Try again!", align=ALIGNMENT, font=FONT)
        states_to_learn = list()
        for state in states:
            if states not in guessed_states:
                states_to_learn.append(states)
                with open("states_to_learn.csv", "w") as file:
                    for state in states_to_learn:
                        file.write(str(state))
        break
    if answer.title() in df["state"].values:
        user_score.increase_score()
        guessed_states.append(answer.title())
        x = df[df["state"] == answer.title()]["x"].values
        y = df[df["state"] == answer.title()]["y"].values
        new_turtle = Turtle()
        new_turtle.color("black")
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.goto(int(x[0]), int(y[0]))
        print(x[0])
        print(y[0])
        new_turtle.write(answer.title(), align=ALIGNMENT, font=FONT)
        if user_score.score == 50:
            is_game_on = False

screen.exitonclick()