from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        """
        Initialize a new Food object.
        
        This class inherits from the Turtle class and represents food in the game.
        The food is initialized as a small circle that can be moved to a random 
        position on the screen.
        """
        super().__init__()  # Initialize the parent class (Turtle)
        self.shape("circle")  # Set the shape of the food to be a circle
        self.penup()  # Disable drawing when moving the food
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Resize the food to make it smaller
        self.color("darkslategrey")  # Set the color of the food
        self.speed("fastest")  # Set the speed of the turtle to the fastest (no animation delay)
        self.refresh()  # Place the food at a random position on the screen
    
    def refresh(self):
        """
        Move the food to a random position on the screen.
        
        The food is placed within the range of coordinates (-280, 280) for x-axis
        and (-280, 250) for y-axis. This allows the food to appear at a random 
        location within the defined boundaries of the game screen.
        """
        self.goto(x=random.randint(-280, 280), y=random.randint(-280, 250))
