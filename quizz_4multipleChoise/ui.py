# Librerie che ci servono per impostare la GUI

from tkinter import *
from quiz_brain import QuizBrain
from PIL import Image, ImageTk
import random
import math

# Colore sfondo dell'interfaccia
THEME_COLOR = "#068DA9"

count = 1 * 60
timer = None
time_left = True
class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR, height=1000, width=1000)
        self.canvas = Canvas(height=150, width=450, bg="white")
        self.question_text = self.canvas.create_text(210, 75, text="Kanye Quote Goes HERE", width=400, font=("Arial", 16, "italic"),
                                fill="black")
        self.canvas.grid(column=0, row=1, columnspan=3, pady=30)

        # Settiamo le caselle per le possibili risposte
        # Risposta A
        self.canvasA = Canvas(height=60, width=380, bg="white")
        self.answerA = self.canvasA.create_text(190, 30, text="Kanye Quote Goes HERE", width=370,
                                                     font=("Arial", 16, "italic"),
                                                     fill="black")
        self.canvasA.grid(column=1, row=2, columnspan=2, pady=10)

        imag_btA = Image.open("./images/bot_A.png")
        imag_botA = ImageTk.PhotoImage(imag_btA.resize((60,60), Image.ANTIALIAS))
        self.butt_botA = Button(image=imag_botA, highlightthickness=0, command=self.botA_pres)
        self.butt_botA.grid(column=0, row=2)

        # Risposta B
        self.canvasB = Canvas(height=60, width=380, bg="white")
        self.answerB = self.canvasB.create_text(190, 30, text="Kanye Quote Goes HERE", width=370,
                                                      font=("Arial", 16, "italic"),
                                                      fill="black")
        self.canvasB.grid(column=1, row=3, columnspan=2, pady=10)

        imag_btB = Image.open("./images/bot_B.png")
        imag_botB = ImageTk.PhotoImage(imag_btB.resize((60, 60), Image.ANTIALIAS))
        self.butt_botB = Button(image=imag_botB, highlightthickness=0, command=self.botB_pres)
        self.butt_botB.grid(column=0, row=3)

        # Risposta C
        self.canvasC = Canvas(height=60, width=380, bg="white")
        self.answerC = self.canvasC.create_text(190, 30, text="Kanye Quote Goes HERE", width=370,
                                                font=("Arial", 16, "italic"),
                                                fill="black")
        self.canvasC.grid(column=1, row=4, columnspan=2, pady=10)

        imag_btC = Image.open("./images/bot_C.png")
        imag_botC = ImageTk.PhotoImage(imag_btC.resize((60, 60), Image.ANTIALIAS))
        self.butt_botC = Button(image=imag_botC, highlightthickness=0, command=self.botC_pres)
        self.butt_botC.grid(column=0, row=4)

        # Risposta D
        self.canvasD = Canvas(height=60, width=380, bg="white")
        self.answerD = self.canvasD.create_text(190, 30, text="Kanye Quote Goes HERE", width=370,
                                                font=("Arial", 16, "italic"),
                                                fill="black")
        self.canvasD.grid(column=1, row=5, columnspan=2, pady=10)

        imag_btD = Image.open("./images/bot_D.png")
        imag_botD = ImageTk.PhotoImage(imag_btD.resize((60, 60), Image.ANTIALIAS))
        self.butt_botD = Button(image=imag_botD, highlightthickness=0, command=self.botD_pres)
        self.butt_botD.grid(column=0, row=5)

        # Impostiamo il label che ci indica il punteggio
        self.score_lab = Label(text=f"Score: {self.quiz.score}", font=("Arial", 12, "bold"), fg="white", bg=THEME_COLOR)
        self.score_lab.grid(column=2, row=0)

        self.categoria_lab = Label(text="Category: ", font=("Arial", 12, "bold"), fg="white", bg=THEME_COLOR)
        self.categoria_lab.grid(column=0, row=0,columnspan=2)

        self.timer_lab = Label(text="Time left: ", font=("Arial", 12, "bold"), fg="white", bg=THEME_COLOR)
        self.timer_lab.grid(column=0, row=6, columnspan=2)


        self.get_next_question()
        self.count_down(count)


    def count_down(self, count):
        count_minut = math.floor(count / 60)
        count_seconds = count % 60
        if count_minut < 10:
            count_minut = "0" + str(count_minut)
        if count_seconds < 10:
            if count_seconds == 0:
                count_seconds = "00"
            else:
                count_seconds = "0" + str(count_seconds)
        self.timer_lab.config(text=f"Timeleft: '{count_minut}:{count_seconds}'")
        if count > 0:
            global timer
            timer = self.window.after(1000, self.count_down, count - 1)
        else:
            global time_left
            time_left = False



        # time_left = True
        # self.count_min, self.count_sec = self.count_down(WORK_MIN)
        # if self.count_min == '00' and self.count_sec == '00':
        #     time_left = False

        self.window.mainloop()

    # Metodo che ci permette di configurare la domanda
    def get_next_question(self):
        self.canvas.config(bg="white")
        self.canvasA.config(bg="white")
        self.canvasB.config(bg="white")
        self.canvasC.config(bg="white")
        self.canvasD.config(bg="white")

        # Se ci sono ancora domande prepara il tutto

        if self.quiz.still_has_questions() and time_left:
            self.butt_botA.config(state="normal")
            self.butt_botB.config(state="normal")
            self.butt_botC.config(state="normal")
            self.butt_botD.config(state="normal")

            q_text, a_text = self.quiz.next_question()
            self.categoria_lab.config(text=f"Category: '{self.quiz.categoria}'")
            self.canvas.itemconfig(self.question_text, text=q_text)

            self.answA = random.choice(a_text)
            a_text.remove(self.answA)
            self.canvasA.itemconfig(self.answerA, text=self.answA)

            self.answB = random.choice(a_text)
            a_text.remove(self.answB)
            self.canvasB.itemconfig(self.answerB, text=self.answB)

            self.answC = random.choice(a_text)
            a_text.remove(self.answC)
            self.canvasC.itemconfig(self.answerC, text=self.answC)

            self.answD = a_text[0]
            self.canvasD.itemconfig(self.answerD, text=self.answD)
        else:

            self.canvas.itemconfig(self.question_text, text=f"End of the quiz\nYour score is {self.quiz.score}/{self.quiz.question_number}")
            self.butt_botA.config(state="disabled")
            self.butt_botB.config(state="disabled")
            self.butt_botC.config(state="disabled")
            self.butt_botD.config(state="disabled")


    # Azione da fare ogni qual volta si preme un pulsante (A; B, C, D)
    def botA_pres(self):
        is_right = self.quiz.check_answer(self.answA)
        if is_right == True:
            self.canvasA.config(bg="green")
        else:
            self.canvasA.config(bg="red")
        self.give_feedback(is_right)

    def botB_pres(self):
        is_right = self.quiz.check_answer(self.answB)
        if is_right == True:
            self.canvasB.config(bg="green")
        else:
            self.canvasB.config(bg="red")
        self.give_feedback(is_right)


    def botC_pres(self):
        is_right = self.quiz.check_answer(self.answC)
        if is_right == True:
            self.canvasC.config(bg="green")
        else:
            self.canvasC.config(bg="red")
        self.give_feedback(is_right)

    def botD_pres(self):
        is_right = self.quiz.check_answer(self.answD)
        if is_right == True:
            self.canvasD.config(bg="green")
        else:
            self.canvasD.config(bg="red")
        self.give_feedback(is_right)

    # Controla se la risposta è corretta ed illumina il canvas della domanda
    def give_feedback(self, is_right):
        self.butt_botA.config(state="disabled")
        self.butt_botB.config(state="disabled")
        self.butt_botC.config(state="disabled")
        self.butt_botD.config(state="disabled")
        if is_right == True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)
        self.score_lab.config(text=f"Score:{self.quiz.score}")












