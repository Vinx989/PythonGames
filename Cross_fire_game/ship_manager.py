from turtle import Turtle
import random

# I parametri che avranno le navicelle nemiche
# come posizione numero di navicele e velocità dei proiettili
SHOOT_SPED = 10
SPEED_INCR = 2
X_POS_LEFT= -250
X_POS_RIGHT= 250
SEPARATION=50
NUM_SHIP=11
class Ship:
    def __init__(self):
        self.all_ship=[]
        self.all_shoot=[]
        self.y_pos_lx=[]
        self.y_pos_dx = []
        self.shoot_speed = SHOOT_SPED

    # Creo due file di navicelle in base al numero di navicelle
    # impostato in precedenza
    def create_battle(self):
        for ship in range(NUM_SHIP):
            new_y = SEPARATION * ship - 250
            new_ship = Turtle()
            new_ship.shapesize(stretch_len=1.5, stretch_wid=1.5)
            new_ship.penup()
            new_ship.color("blue")
            new_ship.goto(x=X_POS_LEFT, y=new_y)
            self.all_ship.append(new_ship)
            self.y_pos_lx.append(new_y)
            
        for ship in range(NUM_SHIP):
            new_y = SEPARATION * ship - 270
            new_ship = Turtle()
            new_ship.shapesize(stretch_len=1.5, stretch_wid=1.5)
            new_ship.penup()
            new_ship.setheading(180)
            new_ship.color("blue")
            new_ship.goto(x=X_POS_RIGHT, y=new_y)
            self.all_ship.append(new_ship)
            self.y_pos_dx.append(new_y)

    # Imposto in modo random quale navicella deve sparare
    # Lo rendo ancora più casuale scegliendo solo due possibilità
    # su sei
    def shoot(self):
        rand_num=random.randint(1,6)
        if rand_num == 2:
            new_fire = Turtle("square")
            new_fire.shapesize(stretch_wid=0.1,stretch_len=1.1)
            new_fire.color("white")
            new_fire.penup()
            new_fire.goto(x=X_POS_LEFT,y=random.choice(self.y_pos_lx))
            self.all_shoot.append(new_fire)
        elif rand_num == 1:
            new_fire = Turtle("square")
            new_fire.shapesize(stretch_wid=0.1,stretch_len=1.1)
            new_fire.color("white")
            new_fire.penup()
            new_fire.setheading(180)
            new_fire.goto(x=X_POS_RIGHT,y=random.choice(self.y_pos_dx))
            self.all_shoot.append(new_fire)

    # Faccio muovere il proiettile
    def move_shoot(self):
        for shoot in self.all_shoot:
            shoot.forward(self.shoot_speed)

    # Aumento la velocità all'aumentare del livello
    def level_up(self):
        self.shoot_speed +=SPEED_INCR