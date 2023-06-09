# Classe che gestisce il funzionamento del quiz

import html
import random
import math

WORK_MIN = 1
WORK_SEC=WORK_MIN*60

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None
        self.num_test = 10


    # Controlla se il numero di domande fatte è superirore
    # alle domande da fare (self.num_text)
    def still_has_questions(self):
        return self.question_number < self.num_test

    # Prepara la domanda da dare alla GUI
    # scegliendo in modo random dalla lista di domande
    def next_question(self):
        self.current_question = random.choice(self.question_list)
        self.categoria = self.current_question.category
        self.question_list.remove(self.current_question)
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        a_text = []
        for item in self.current_question.choise:
            a_text.append(html.unescape(item))
        return f"Q.{self.question_number}: {q_text} ", a_text

    # Controlla la risposta
    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
