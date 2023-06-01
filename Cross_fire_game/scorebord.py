from turtle import Turtle

# Imposto lo stile delle scritte
STYLE = ('Courier', 20, 'bold')
ALLIG = "center"
level_in = 0


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level = level_in
        self.penup()
        self.color("white")
        self.hideturtle()
        self.setposition(-220, 290)
        self.update_score()

    # Scrivo il livello
    def update_score(self):
        self.write(f"LEVEL: {self.level}", font=STYLE, align=ALLIG)

    # Scrivo gioco finito
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", font=STYLE, align=ALLIG)

    # Aumento il livello
    def increase(self):
        self.level += 1
        self.clear()
        self.update_score()

    # Annuncio la vittoria
    def victory(self):
        self.goto(0,0)
        self.write("YOU WIN", font=STYLE, align=ALLIG)