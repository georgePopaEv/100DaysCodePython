from turtle import Turtle,Screen
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISNTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.segments_snake = []
        self.create_snake()
        self.head = self.segments_snake[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            snake = Turtle('square')
            snake.color('white')
            snake.penup()
            snake.goto(position)
            self.segments_snake.append(snake)

    def move_snake(self):
        for seg_num in range(len(self.segments_snake) - 1, 0, -1):
            new_x = self.segments_snake[seg_num - 1].xcor()
            new_y = self.segments_snake[seg_num - 1].ycor()
            self.segments_snake[seg_num].goto(new_x, new_y)
        self.segments_snake[0].forward(MOVE_DISNTANCE)


    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_new_element_to_snake(self):
        snake = Turtle('square')
        snake.color('white')
        snake.penup()
        position = [self.segments_snake[-1].xcor(), self.segments_snake[-1].ycor()]
        snake.goto(position)
        self.segments_snake.append(snake)

    def colide_with_tail(self):
        for segm in self.segments_snake[2:]:
            if self.head.distance(segm) < 10:
                return True
        # for i in range(2,len(self.segments_snake)-1):
        #     if self.head.xcor() == self.segments_snake[i].xcor() and self.head.ycor() == self.segments_snake[i].ycor():
        #         return True


