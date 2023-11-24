import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
scoreboard=Scoreboard()
car_manager=CarManager()

screen.listen()
screen.onkey(player.move,"Up")

game_is_on = True
while game_is_on:
    
    time.sleep(0.1)
    screen.update()
    car_manager.move()
    car_manager.createCar()

    for i in car_manager.cars:
        if player.distance(i)<20:
            game_is_on=False
            scoreboard.game_over()
    
    if player.isAtFinishLine():
        player.goToStart()
        scoreboard.score+=1
        car_manager.accelerate()
        scoreboard.update_score()

screen.exitonclick()