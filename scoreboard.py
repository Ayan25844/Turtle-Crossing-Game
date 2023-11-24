from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score=0
        self.hideturtle()
        self.goto(-290,260)
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.write(f"LEVEL: {self.score}",font=FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=FONT)