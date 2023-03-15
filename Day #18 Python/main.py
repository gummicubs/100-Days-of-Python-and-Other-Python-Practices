from turtle import Turtle, Screen
from random import randint
import pandas as pd
import matplotlib.pyplot as plt

timmy_the_turtle = Turtle()
timmy_the_turtle.shape('turtle')
timmy_the_turtle.color('red')
screen = Screen()
screen.colormode(255)
# timmy_the_turtle.pensize(10)
timmy_the_turtle.speed('fastest')



def move_square():
    for i in range(4):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(90)
    
def dash():
    for i in range(10):
        timmy_the_turtle.pendown()
        timmy_the_turtle.forward(2)
        timmy_the_turtle.penup()
        timmy_the_turtle.forward(2)
        

def shape():
    for i in range(3,11):
        timmy_the_turtle.pencolor(randint(1,255), randint(1,255), randint(1,255))
        for n in range(1,i+1):
            timmy_the_turtle.forward(100)
            timmy_the_turtle.right(360/i)
            
            
def random_walk():
    step = []
    how_far = []
    for n in range(100):
        timmy_the_turtle.pencolor(randint(1,255), randint(1,255), randint(1,255))
        timmy_the_turtle.penup()
        timmy_the_turtle.home()
        timmy_the_turtle.pendown()
        for i in range(100):
            x = randint(0,3)
            if x == 1:
                timmy_the_turtle.right(90)
            elif x == 2:
                timmy_the_turtle.left(90)
            elif x == 3:
                timmy_the_turtle.right(180)
            timmy_the_turtle.forward(25)    
        step.append(n+1)
        how_far.append(timmy_the_turtle.distance(0,0))
    return step, how_far
        
def spiral_graph():
    for i in range(72):
        timmy_the_turtle.pencolor(randint(1,255), randint(1,255), randint(1,255))
        timmy_the_turtle.circle(100)
        timmy_the_turtle.right(5)

spiral_graph()

# step, distance = random_walk()
# datas = {'trial': step, 'distance': distance}
# df = pd.DataFrame(data = datas)


# plt.rcParams.update({'figure.figsize':(7,5), 'figure.dpi':100})
# plt.hist(distance, 5)
# plt.gca().set(title='Frequency Histogram', ylabel='Frequency');
# plt.show()

screen.exitonclick()