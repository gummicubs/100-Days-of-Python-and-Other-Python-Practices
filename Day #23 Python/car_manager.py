from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
NUM_OF_CARS = 15

class Car:
    
    def __init__(self, xcoor, ycoor):
        self.segments = []
        self.travel_speed = STARTING_MOVE_DISTANCE
        self.color = random.choice(COLORS)
        self.starting_x = xcoor
        self.starting_y = ycoor
        for i in range(2):
            segment = Turtle()
            segment.shape('square')
            segment.penup()
            segment.goto(x = self.starting_x+20*i, y = self.starting_y)
            segment.color(self.color)
            segment.setheading(180)
            self.segments.append(segment)
        self.move()
            
    def move(self):
        for segment in self.segments:
            segment.forward(self.travel_speed)



class CarManager:
    
    def __init__(self):
        self.cars = []
        self.new_car_num = 1
        self.travel_speed = STARTING_MOVE_DISTANCE
        self.increase_speed = MOVE_INCREMENT
        
    def create_cars(self,):
        for i in range(NUM_OF_CARS):
            name = 'car'+str(i)
            name = Car(random.randint(-280, 280), random.randint(-280,280))
            self.cars.append(name)
            
    def move_cars(self):
        for car in self.cars:
            car.move()
            
    def create_new_cars(self, level):
        x = random.randint(1,100)
        if x < 11*level:
            name = 'new_car' + str(self.new_car_num)
            name = Car(300, random.randint(-280,280))
            name.travel_speed = self.travel_speed
            self.cars.append(name)
    
    def update_speed(self):
        self.travel_speed += self.increase_speed
        for car in self.cars:
            car.travel_speed = self.travel_speed
            
            
    def crash(self, ycorr):
        for car in self.cars:
            if abs(car.segments[1].xcor()) <self.travel_speed/2:
                for i in range(2):
                    if abs(ycorr - car.segments[i].ycor()) <=20:
                        return True

            
        

