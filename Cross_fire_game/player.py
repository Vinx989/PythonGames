from turtle import Turtle

# Numero di step per ogni comando
STEPS = 10
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.goto(x=0, y=-300)
        self.left(90)

    # Il giocatore potrà muoversi in alto o in basso
    def go_up(self):
        self.forward(STEPS)
        
    def go_down(self):
        self.back(STEPS)

    # Riporto il player al punto di partenza
    def refresh(self):
        self.goto(0,-300)
        