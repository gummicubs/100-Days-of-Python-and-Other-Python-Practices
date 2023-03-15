from turtle import Turtle, Screen
from random import randint, choice

LEFT = -260
RIGHT = 260
YPOS = 20 

STEPS = 20

class Paddle:
    
    
    def __init__(self, player):
        self.body = []
        self.player = player
        for i in range(3):
            name = 'squ'+str(i)
            name = Turtle()
            name.color('white')
            name.shape('square')
            name.penup()
            name.speed('fastest')
            if self.player == 1:
                name.goto(x = LEFT, y = -YPOS*i)
            else:
                name.goto(x= RIGHT, y= -YPOS*i)
            self.body.append(name)
            
        
    def move_up(self):
        if self.body[0].ycor() < 240:
            for squ in self.body:
                squ.setheading(90)
                squ.forward(STEPS)
            
            
    def move_down(self):
        if self.body[2].ycor() > -280:
            for squ in self.body:
                squ.setheading(270)
                squ.forward(STEPS)
            

class Ball(Turtle):
    
    
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.speed('fastest')
        self.penup()
        self.game_on = True
        self.next()
        


    def move(self):
        self.forward(10)
        self.reflect()
        
        
    def next(self):
        self.game_on = True
        self.home()
        self.setheading(choice([randint(145, 179), randint(0,45), randint(315,359), randint(181,225)]))
        
    
    def reflect(self):
        if self.ycor() >=260 or self.ycor() <=-280:
            self.setheading(360-self.heading())
            
        
    def hit_walls(self):
        if self.xcor() >=280:
            self.game_on = False
            return 1
        elif self.xcor() <=-280:
            self.game_on = False
            return 2
        
        
    def left_paddle_reflect(self,paddle):
        if self.distance(x=paddle.body[1].xcor(), y=paddle.body[1].ycor()) < 10:
            if self.heading() > 90 and self.heading() < 180:
                self.setheading(180 - self.heading())
            elif self.heading() > 180 and self.heading() <270:
                self.setheading(self.heading()+90)
                
        elif self.distance(x=paddle.body[0].xcor(), y=paddle.body[0].ycor()) < 10:
            if self.heading() > 90 and self.heading() < 180:
                    self.setheading(180+30 - self.heading())
            elif self.heading() > 180 and self.heading() <270:
                self.setheading(self.heading()+90-30)
                
        elif self.distance(x=paddle.body[2].xcor(), y=paddle.body[2].ycor()) < 10:
            if self.heading() > 90 and self.heading() < 180:
                    self.setheading(180+30 - self.heading())
            elif self.heading() > 180 and self.heading() <270:
                self.setheading(self.heading()+90-30)    
               
                           
        
    def right_paddle_reflect(self, paddle):
        if self.distance(x=paddle.body[1].xcor(), y=paddle.body[1].ycor()) < 10:
            if self.heading() >0 and self.heading() < 90:
                self.setheading(90+self.heading())
            elif self.heading() >270 and self.heading() < 360:
                self.setheading(540-self.heading())
                
        elif self.distance(x=paddle.body[0].xcor(), y=paddle.body[0].ycor()) < 10:
            if self.heading() >0 and self.heading() < 90:
                self.setheading(90+30+self.heading())
            elif self.heading() >270 and self.heading() < 360:
                self.setheading(540-30-self.heading())            

        elif self.distance(x=paddle.body[2].xcor(), y=paddle.body[2].ycor()) < 10:
            if self.heading() >0 and self.heading() < 90:
                self.setheading(90+30+self.heading())
            elif self.heading() >270 and self.heading() < 360:
                self.setheading(540-30-self.heading())  



class Scoreboard(Turtle):
    
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.ht()
        self.goto(x=0, y=260)
        self.score1 = 0
        self.score2 = 0
        self.write(f'Player 1: {self.score1}                 Player 2: {self.score2}',move = False, align='center', font = ('Cambria', 20, 'normal'))
        
    
    def update_score(self, winner):
        if winner == 1:
            self.score1 +=1
        elif winner == 2:
            self.score2 +=1
        self.clear()
        self.write(f'Player 1: {self.score1}                 Player 2: {self.score2}',move = False, align='center', font = ('Cambria', 20, 'normal'))
        
        
    def game_over(self):
        self.home()
        self.write(f'GAME OVER',move = False, align='center', font = ('Cambria', 20, 'normal'))    