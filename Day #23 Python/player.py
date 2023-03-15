from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('black')
        self.reset()
        self.setheading(90)
        self.shape('turtle')
        self.speed('fastest')
        
    def reset(self):
        self.goto(STARTING_POSITION)
        
    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def next_level(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.reset()
            return True
        
    def collide(self, car):
        if car.xcor() >=-20 and car.cor()<=20:
            if abs(self.ycor()-car.ycor()) <=15:
                return True