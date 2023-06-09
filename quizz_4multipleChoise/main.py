'''
Quizzettone. vediamo quanto sei bravo
Il programma è un quiz che viene fatto tramite GUI utilizzanto la
libreia tkinter di python. Il programma seleziona dieci domande in modo random
da un dataset. Per rispondere alle domande bisogno premere con il cursore del mouse
sul pulsante corrispondente alla possibili scelte.
Il programma prende spunto dal corso 100 days of Python ideato da 'The App Brewery'
Programma Scritto da Vincenzo Bruno
'''

# Importiamo i moduli necessari
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# Questa parte prepara il set di domande partendo dal file data.py
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    question_choise = question["incorrect_answers"]
    question_category = question["category"]
    question_choise.append(question_answer)
    new_question = Question(question_text, question_answer, question_choise, question_category)
    question_bank.append(new_question)


# Inizializza gli oggetti principali e
# fa partire il quiz
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# Fa il print dello score per farti notare che è finito il gioco
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
