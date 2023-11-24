from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.createPlayer()
    
    def createPlayer(self):
        self.penup()
        self.goToStart()
        self.setheading(90)
        self.shape("turtle")
    
    def move(self):
        self.fd(MOVE_DISTANCE)
    
    def goToStart(self):
        self.goto(STARTING_POSITION)
    
    def isAtFinishLine(self):
        if self.ycor()>FINISH_LINE_Y:
            return True