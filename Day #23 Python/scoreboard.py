from turtle import Turtle

FONT = ("Courier", 24, "normal")
XCOR = -210
YMAX = 260


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('black')
        self.ht()
        self.goto(XCOR, YMAX)
        self.level()
        
    def level(self):
        self.score += 1
        self.clear()
        self.write(f'LEVEL: {self.score}', move = False, align = 'center', font = FONT)
    
    def game_over(self):
        self.home()
        self.write(f'GAME OVER', move = False, align = 'center', font = FONT)
        
