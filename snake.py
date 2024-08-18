from turtle import Turtle

# Initial positions of the snake's segments
INIT_POS = [(0, 0), (-20, 0), (-40, 0)]

# Distance moved by the snake in each step
MOVE_DISTANCE = 20

# Direction constants (heading angles)
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake:
    def __init__(self):
        """
        Initialize the Snake object.

        This class creates a snake composed of multiple segments and controls its 
        movement and direction. The snake starts with three segments, and the 
        first segment acts as the head.
        """
        self.segments = []  # List to store the snake's segments
        self.create_snake()  # Create the initial snake with three segments
        self.head = self.segments[0]  # The first segment is the head of the snake

    def create_snake(self):
        """
        Create the initial three segments of the snake.

        This method adds three segments to the snake at the positions defined 
        in INIT_POS. The segments are aligned horizontally, forming the initial 
        body of the snake.
        """
        for pos in INIT_POS:
            self.add_segment(pos)  # Add each segment at the specified position

    def move(self):
        """
        Move the snake forward.

        The snake's segments move such that each segment follows the segment 
        in front of it. The head moves forward by the defined MOVE_DISTANCE.
        """
        # Move each segment to the position of the segment in front of it
        for index in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[index - 1].xcor()
            new_y = self.segments[index - 1].ycor()
            self.segments[index].goto(new_x, new_y)
        # Move the head forward
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        """
        Change the snake's direction to up.

        This method is triggered by the Up arrow key and changes the direction 
        of the snake's head to UP (90 degrees) unless it's currently moving down.
        """
        if self.head.heading() != DOWN:  # Prevent moving in the opposite direction
            self.head.setheading(UP)

    def left(self):
        """
        Change the snake's direction to left.

        This method is triggered by the Left arrow key and changes the direction 
        of the snake's head to LEFT (180 degrees) unless it's currently moving right.
        """
        if self.head.heading() != RIGHT:  # Prevent moving in the opposite direction
            self.head.setheading(LEFT)

    def down(self):
        """
        Change the snake's direction to down.

        This method is triggered by the Down arrow key and changes the direction 
        of the snake's head to DOWN (270 degrees) unless it's currently moving up.
        """
        if self.head.heading() != UP:  # Prevent moving in the opposite direction
            self.head.setheading(DOWN)

    def right(self):
        """
        Change the snake's direction to right.

        This method is triggered by the Right arrow key and changes the direction 
        of the snake's head to RIGHT (0 degrees) unless it's currently moving left.
        """
        if self.head.heading() != LEFT:  # Prevent moving in the opposite direction
            self.head.setheading(RIGHT)

    def add_segment(self, position):
        """
        Add a new segment to the snake at the specified position.

        This method creates a new segment (a Turtle object), positions it at the 
        given coordinates, and adds it to the snake's segment list.
        """
        segment = Turtle("square")  # Create a new segment shaped like a square
        segment.color("darkslategrey")  # Set the segment's color
        segment.penup()  # Prevent the segment from drawing a line when moving
        segment.goto(position)  # Position the segment at the specified coordinates
        self.segments.append(segment)  # Add the segment to the snake's body

    def extend(self):
        """
        Extend the snake by adding a new segment at the tail.

        This method adds a new segment to the snake at the position of the last 
        segment, effectively lengthening the snake's body.
        """
        self.add_segment(self.segments[-1].position())  # Add a segment at the tail's position

    def reset(self):
        """
        Reset the snake when the game is over.

        This method removes all segments from the screen and reinitializes the 
        snake with three segments at the starting positions.
        """
        # Move all segments off-screen and clear the segment list
        for segment in self.segments:
            segment.goto(10000, 10000)
        self.segments.clear()
        self.create_snake()  # Recreate the initial snake
        self.head = self.segments[0]  # Reassign the head to the first segment
