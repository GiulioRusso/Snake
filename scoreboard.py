from turtle import Turtle

# font features
ALIGNMENT = "center"
FONT = ("Menlo", 24, "normal")

# scoreboard set-up
SCOREBOARD_X = 0
SCOREBOARD_Y = 270

class Scoreboard(Turtle):

    def __init__(self):
        """
        Initialize the scoreboard
        """
        super().__init__()
        self.score = 0
        # read high score from file data.txt
        with open("./data.txt") as data:
            self.high_score = int(data.read())
        self.color("darkslategrey")
        self.hideturtle()
        self.penup()
        self.goto(x=SCOREBOARD_X, y=SCOREBOARD_Y)
        self.update_scoreboard()
        
    def update_scoreboard(self):
        """
        Update scoreboard text
        """
        self.clear()
        self.write(f"SCORE: {self.score}   HIGH SCORE: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """
        Increase the score text
        """
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        """
        Game over print when game is over
        """
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
    
    def reset(self):
        """
        Reset the scoreboard and update the high score
        """
        if self.score > self.high_score:
            # update high score on file data.txt
            with open("snake-game/data.txt", mode='w') as data:
                data.write(f"{self.score}")
            self.high_score = self.score

        self.score = 0

        self.update_scoreboard()
