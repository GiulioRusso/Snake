from turtle import Turtle

# init position
INIT_POS = [(0,0), (-20,0), (-40,0)]

# movement distance
MOVE_DISTANCE = 20

# heading from Turtle class
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake:
    def __init__(self):
        """
        Initialize the segment lists and snake head
        """
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """
        Create the first three segments of the snake
        """
        for pos in INIT_POS:
            self.add_segment(pos) # add the initial three segments into the initial positions

    def move(self):
        """
        Define movement logic
        """
        # overlap the tail segemnt to the following one
        for index in range(len(self.segments)-1, 0, -1): self.segments[index].goto(self.segments[index-1].xcor(), self.segments[index-1].ycor())
        # the head move forward
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        """
        Keyboard listener to Up arrow
        """
        if self.head.heading() != DOWN: # can't go into the opposite direction
            self.head.setheading(UP)

    def left(self):
        """
        Keyboard listener to Left arrow
        """
        if self.head.heading() != RIGHT: # can't go into the opposite direction
            self.head.setheading(LEFT)

    def down(self):
        """
        Keyboard listener to Down arrow
        """
        if self.head.heading() != UP: # can't go into the opposite direction
            self.head.setheading(DOWN)

    def right(self):
        """
        Keyboard listener to Right arrow
        """
        if self.head.heading() != LEFT: # can't go into the opposite direction
            self.head.setheading(RIGHT)

    def add_segment(self, position):
        """
        Add a new segment to the tail of the Snake
        """
        segment = Turtle("square")
        segment.color("darkslategrey")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        """
        Extend the Snake draw
        """
        self.add_segment(self.segments[-1].position()) # add the new segment into the position of the last segment of the Snake

    def reset(self):
        """
        Reinitialize the snake when the game is over
        """
        for segment in self.segments: segment.goto(10000, 10000) # move away the segments if the snake die
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]