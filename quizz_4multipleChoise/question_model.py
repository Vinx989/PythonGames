# Crea l'oggetto domanda con relative risposte e categorie
class Question:

    def __init__(self, q_text, q_answer, q_choise, q_category):
        self.text = q_text
        self.answer = q_answer
        self.choise = q_choise
        self.category = q_category
