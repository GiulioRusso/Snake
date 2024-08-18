from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Window set-up
WINDOW_LENGTH = 600  # Size of the game window
BOUNDARY = 20  # Distance from the edge of the window to the boundary
WINDOW_RIGHT_BOUNDARY = WINDOW_UP_BOUNDARY = WINDOW_LENGTH / 2 - BOUNDARY  # Right and top boundaries
WINDOW_LEFT_BOUNDARY = WINDOW_BOTTOM_BOUNDARY = -WINDOW_LENGTH / 2 + BOUNDARY  # Left and bottom boundaries

# Game parameters
COLLISION_DISTANCE = 15  # Distance to detect collision with food or tail

# Set up the screen
screen = Screen()
screen.setup(width=WINDOW_LENGTH, height=WINDOW_LENGTH)  # Set the screen size
screen.bgcolor("yellowgreen")  # Background color of the game window
screen.title("My Snake Game")  # Title of the game window
screen.tracer(0)  # Turn off automatic screen updates for smoother animations

# Create Snake, Food, and Scoreboard objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Listen to keyboard inputs
screen.listen()
screen.onkey(snake.up, "Up")  # Move snake up
screen.onkey(snake.down, "Down")  # Move snake down
screen.onkey(snake.right, "Right")  # Move snake right
screen.onkey(snake.left, "Left")  # Move snake left

# Main game loop
game_is_on = True
while game_is_on:
    # Update the screen and add a small delay to control the snake's speed
    screen.update()
    time.sleep(0.1)

    # Move the snake forward
    snake.move()

    # Check for collision with food
    if snake.head.distance(food) < COLLISION_DISTANCE:
        food.refresh()  # Reposition the food at a new random location
        snake.extend()  # Extend the snake by adding a new segment
        scoreboard.increase_score()  # Increase the score

    # Check for collision with the wall
    if snake.head.xcor() > WINDOW_RIGHT_BOUNDARY or snake.head.xcor() < WINDOW_LEFT_BOUNDARY or snake.head.ycor() > WINDOW_UP_BOUNDARY or snake.head.ycor() < WINDOW_BOTTOM_BOUNDARY:
        scoreboard.reset()  # Reset the scoreboard and update the high score
        snake.reset()  # Reset the snake to the initial position and size

    # Check for collision with the snake's own tail
    for segment in snake.segments[1:]:  # Skip the head (index 0)
        if snake.head.distance(segment) < COLLISION_DISTANCE:
            scoreboard.reset()  # Reset the scoreboard and update the high score
            snake.reset()  # Reset the snake to the initial position and size

# Exit the game when the screen is clicked
screen.exitonclick()
