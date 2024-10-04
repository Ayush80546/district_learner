from turtle import Turtle, Screen
import pandas

screen = Screen()
image = "mp_blank_district.gif"
screen.addshape(image)
mp_map = Turtle(image)

dataframe = pandas.read_csv("mp_districts.csv")
# Dictionary comprehension
coordinate_dict = {row.state: [row.x, row.y] for (index, row) in dataframe.iterrows()}

guessed_list = []
with open("remaining.txt", "w") as file:
    file.write("   ")
while len(guessed_list) < 52:
    user_guess = screen.textinput(title=f"score :{len(guessed_list)}/52", prompt="Guess the district").title()
    if user_guess == "Exit":
        missing = [key for (key, value) in coordinate_dict.items() if key not in guessed_list]
        with open("remaining.txt", "a") as file:
            for district in missing:
                file.write(f"{district}\n")
        break
    elif user_guess in coordinate_dict:
        guessed_list.append(user_guess)
        new_x = coordinate_dict[user_guess][0]
        new_y = coordinate_dict[user_guess][1]
        turtle_writer = Turtle()
        turtle_writer.penup()
        turtle_writer.hideturtle()
        turtle_writer.goto(new_x, new_y)
        turtle_writer.write(user_guess)

screen.exitonclick()
