from turtle import Turtle, Screen, shape
import pandas as pd


with open('50_states.csv') as file:
    states = pd.DataFrame(pd.read_csv(file))


screen = Screen()
screen.addshape('blank_states_img.gif')
shape('blank_states_img.gif')
screen.title('Name the US States')
# screen.screensize(800, 600)

num = 0
while num <50:
    num = 50-len(states)
    answer = screen.textinput(title = f'Name a State {num}/50', prompt = 'Name Another State Name')
    answer = answer.title()

    
    if answer in states['state'].values:
        state = Turtle()
        state.penup()
        state.ht()
        state.goto(x = float(states[states['state'] == answer]['x']), y = float(states[states['state'] == answer]['y']))
        state.write(answer)
        screen.update()
        states.drop(states.index[(states['state'] == answer)], inplace = True)
    elif answer == 'Exit':
        remaining = pd.DataFrame(states.state)
        remaining.to_csv('states_to_learn.csv')
        break

screen.mainloop()