from turtle import Turtle, Screen
import random

# Define screen object
screen = Screen()

# Define screen size
screen.setup(width=500, height=400)

# Request user to choose a color
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
color = ["red", "orange", "yellow", "green", "blue", "purple"]

# Define turtle position
y_positions = [-70, -40, -10, 20, 50, 80]

# Define list of turtles
all_turtles = []


is_race_on = False

# For loop to define each turtle color and also put the turtles on the right starting position
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

# Only start race after user has chosen a color
if user_bet:
    is_race_on = True

# While loop that will be executed until one turtle reaches the finish line
while is_race_on:
    for turtle in all_turtles:
        # Generate random distance
        rand_distance = random.randint(0, 10)
        # Apply distance to turtle
        turtle.forward(rand_distance)
        # Verify if turtle has reached the finish line. If yes, end race and print if you were right or not on the bet.
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

# Close screen on click
screen.exitonclick()

