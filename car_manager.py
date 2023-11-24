import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.cars=[]
        self.createCar()
        self.move_speed=STARTING_MOVE_DISTANCE
    
    def createCar(self):
        choice=random.randint(1,6)
        if choice==1:
            car=Turtle("square")
            car.penup()
            car.goto(300,random.randint(-250,250))
            car.shapesize(stretch_wid=1,stretch_len=2)
            car.color(COLORS[random.randint(0,len(COLORS)-1)])
            self.cars.append(car)
    
    def move(self):
        for i in self.cars:
            i.backward(self.move_speed)
    
    def accelerate(self):
        self.move_speed+=MOVE_INCREMENT           