'''
Space cross Fire Game
Lo scopo del gico è quello di superare una zona di guerra spaziale senza farsi
colpire dal fuoco nemico. Il gioco preve il superamento di 10 livelli
e per ogni livello superato aumenta la velocità dei proiettili.
Questo gioco è stato creat utilizzando la libreria grafica turtle
ed è stato suddiviso in moduli
player: gestisce le funzionalità del giocatore
Ship_manager: regola le funzionalità e la posizione delle navicelle nemiche
scoreboard: regola il punteggio ed il livello

'''
from turtle import Turtle, Screen
from player import Player
from ship_manager import Ship
from scorebord import Level
import time

# Inizializzo lo schermo
screen=Screen()
screen.setup(width=600, height=650)
screen.bgcolor("black")
screen.title("Cross Space Fire Game")
screen.tracer(0)

# Disegno il traguardo
penna=Turtle()
penna.pensize(5)
penna.penup()
penna.goto(-300,280)
penna.color("white")

for i in range(20):
    penna.pendown()
    penna.forward(20)
    penna.penup()
    penna.forward(20)

# Istanzio il livello ed posiziono il player
livello = Level()

timmy = Player()

screen.listen()
screen.onkey(timmy.go_up, "Up")
screen.onkey(timmy.go_down, "Down")

# Creo le navicelle nemiche
battle_field= Ship()

battle_field.create_battle()

# Main while loop del gico
game_on=True

while game_on:
    screen.update()
    time.sleep(0.1)
    battle_field.shoot()
    battle_field.move_shoot()
    
    # Determino se ha superato o no
    if timmy.ycor() > 300:
        livello.increase()
        battle_field.level_up()
        timmy.refresh()
    
    # Determino se il proiettile ha colpito oppure no
    # Se vengo colpito il gioco finisce
    for shoot in battle_field.all_shoot:
        if timmy.distance(shoot) < 15:
            livello.game_over()
            game_on = False

    # Dopo l'arrivo controllo se ho finito il gioco oppure no
    if livello.level > 9:
        livello.victory()
        game_on = False

screen.exitonclick()