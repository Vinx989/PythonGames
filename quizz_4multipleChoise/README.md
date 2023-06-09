# Quiz a risposte multiple

Questo programma simula un qui a scelta multipla. Appena si avvia il programma parte il timer ed appare la prima domanda che viene selezionata in modo random da un set di 50 domande. Tramite il cursore possiamo premere sul bottone della risposta che riteniamo corretta. Una volta premuto la domanda e la risposta si coloreranno di rosso o verde rispettivamente se la risposta è sbagliata o corretta. Fatto ciò il programma passa direttamente alla domanda successiva. Al termine del numero di domande impostate all'inizio o allo scadere del tempo il quiz terminerà e mostrerà il punteggio come risposte esatte su numero di domande fatte.

Il programma è stato creato utilizzando la libreria tkinter per l'interfaccia grafica (GUI), utilizza il modulo request per comunicare con l'API della banca dati delle domande. Il programma prende spunto dal corso 100 days of Python ideato da 'The App Brewery'.

Le domande sono prese da 'Open Trivia database' (https://opentdb.com/)

Il programma è diviso in moduli:

- ### data.py:
  Contiene la richiesta APIRESTful per accedere alle domande da fare
- ### main.py:
  Questo è il main che fa funzionare il tutto
- ### question_model.py:
  Questo modulo contiene la struttura delle domande
- ### quiz_brain.py:
  Questo modulo contiene la parte relativa al funzionamento del quiz
- ### ui.py:
  Questo modulo contiene la parte relativa all'interfaccia grafica
