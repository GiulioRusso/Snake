from turtle import Turtle

# Font settings for displaying text on the scoreboard
ALIGNMENT = "center"
FONT = ("Menlo", 24, "normal")

# Scoreboard position on the screen
SCOREBOARD_X = 0
SCOREBOARD_Y = 270

class Scoreboard(Turtle):

    def __init__(self):
        """
        Initialize the Scoreboard.

        This class inherits from the Turtle class and manages the display of the 
        player's current score and the high score. The high score is read from 
        a file called 'data.txt'. The scoreboard is positioned at the top center 
        of the screen.
        """
        super().__init__()  # Initialize the parent class (Turtle)
        self.score = 0  # Initialize the current score to zero
        # Read the high score from 'data.txt'
        with open("./data.txt") as data:
            self.high_score = int(data.read())
        self.color("darkslategrey")  # Set the text color
        self.hideturtle()  # Hide the turtle cursor (only show text)
        self.penup()  # Disable drawing when moving the turtle
        self.goto(x=SCOREBOARD_X, y=SCOREBOARD_Y)  # Position the scoreboard
        self.update_scoreboard()  # Display the initial scoreboard text
        
    def update_scoreboard(self):
        """
        Update and display the current score and high score.

        Clears the previous text and writes the updated score and high score 
        at the scoreboard's position.
        """
        self.clear()  # Clear previous scoreboard text
        self.write(f"SCORE: {self.score}   HIGH SCORE: {self.high_score}", 
                   align=ALIGNMENT, font=FONT)  # Display the updated scores

    def increase_score(self):
        """
        Increment the score by one and update the scoreboard.
        """
        self.score += 1  # Increase the score by one
        self.update_scoreboard()  # Refresh the scoreboard display

    def game_over(self):
        """
        Display 'GAME OVER' message at the center of the screen.
        """
        self.goto(0, 0)  # Move to the center of the screen
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)  # Display the message
    
    def reset(self):
        """
        Reset the scoreboard after the game ends and update the high score if necessary.

        If the current score is higher than the recorded high score, update the 
        high score in the 'data.txt' file. Then, reset the current score to zero 
        and update the scoreboard display.
        """
        if self.score > self.high_score:
            # Write the new high score to 'data.txt'
            with open("./data.txt", mode='w') as data:
                data.write(f"{self.score}")
            self.high_score = self.score  # Update the high score

        self.score = 0  # Reset the current score
        self.update_scoreboard()  # Refresh the scoreboard display
