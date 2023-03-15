from turtle import Turtle
from random import randint

class Snake():
    
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        
        
    def create_snake(self):   
        for i in range(3):
            name = 'snake'+str(i)
            name = Turtle()
            name.shape('circle')
            name.color('white')
            name.penup()
            name.goto(x = -i*20, y = 0)
            self.segments.append(name)

    
    def move(self):
        lastx, lasty = self.segments[-1].xcor(), self.segments[-1].ycor()
        for i in range(len(self.segments)-1):
            self.segments[len(self.segments)-i-1].goto(self.segments[len(self.segments)-i-2].xcor(), self.segments[len(self.segments)-i-2].ycor())
        self.segments[0].forward(20)    
        return lastx, lasty

    def add_segment(self):
        name = 'snake'+str(len(self.segments))
        name = self.segments[len(self.segments)-1].clone()
        # name.shape('circle')
        # name.color('white')
        # name.penup()
        # name.goto(spot)
        self.move()
        self.segments.append(name)


    def up(self):
        if self.segments[0].heading() !=270:
            self.segments[0].setheading(90)
    
    
    def down(self):
        if self.segments[0].heading() !=90:
            self.segments[0].setheading(270)
        
        
    def right(self):
        if self.segments[0].heading() !=180:
            self.segments[0].setheading(0)
    
    
    def left(self):
        if self.segments[0].heading() !=0:
            self.segments[0].setheading(180)


    def checks_walls(self):
        if self.segments[0].xcor() >= 280 or self.segments[0].xcor() <=-280:
            return 'off'
        elif self.segments[0].ycor() >= 270 or self.segments[0].ycor() <=-280:
            return 'off'
        else:
            return 'on'


class Food(Turtle):
    
    
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed('fastest')
        self.color('yellow')
        self.refresh()
        
        
    def refresh(self):
        self.goto(x = randint(-280, 280), y= randint(-280, 250))
        
        
class Scoreboard(Turtle):
    
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(x = 0, y = 280)
        self.ht()
        
    
    def update_score(self, point):
        self.score += point
        self.clear()
        self.write(f'Points: {self.score}', move=False, align='center', font=('Arial', 14, 'normal'))
        
    
    def game_over(self):
        self.home()
        self.write('GAME OVER', move=False, align='center', font=('Arial', 30, 'normal'))
