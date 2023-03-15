from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width = 500, height = 400)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
names = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple']

y_start = 125
for i in range(len(colors)):
    names[i] = Turtle()
    names[i].shape('turtle')
    names[i].color(colors[i])
    names[i].penup()
    names[i].goto(x = -230, y = y_start)
    y_start -=50


user_guess = screen.textinput(title = 'Turtle Gamble', prompt = 'Which turtle do you think will win?')

while user_guess != '':
    for i in range(len(names)):
        names[i].forward(randint(0,10))
        if names[i].xcor() >= 230:
            print(f'The winner of the race is {colors[i].title()}!')
            user_guess = ''
        
# tim = Turtle()


# def clockwise():
#     tim.right(10)
    
# def counter_clockwise():
#     tim.left(10)
    
# def forward():
#     tim.forward(10)

# def backward():
#     tim.backward(10)
    
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()

# screen.listen()
# screen.onkeypress(fun = forward, key = 'w')
# screen.onkeypress(fun = backward, key = 's')
# screen.onkeypress(fun = counter_clockwise, key = 'a')
# screen.onkeypress(fun = clockwise, key = 'd')
# screen.onkey(fun = clear, key = 'c')

screen.exitonclick()

