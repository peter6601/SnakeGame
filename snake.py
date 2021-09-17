from turtle import  Turtle
import  time
start_position = [(0, 0), (-20, 0), (-40, 0)]
start_colors = ["yellow", "red", "white"]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:


    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(0, len(start_position)):
            self.add_segment(start_position[i])

    def add_segment(self, position):
        segment = Turtle("square")
        color_position = (len(self.segments)) % len(start_colors)
        segment.color(start_colors[color_position])
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
             self.segments[0].setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)


# for position in start_position:
#     segment = Turtle("square")
#     segment.color("white")
#     segment.penup()
#     segment.goto(position)
#     segments.append(segment)