# Quiz a risposte multiple

Questo programma simula un quiz a scelta multipla. Appena si avvia il programma parte il timer ed appare la prima domanda. La domanda viene selezionata in modo random da un set di 50 domande. Tramite il cursore possiamo premere sul bottone della risposta che riteniamo corretta. Una volta premuto la domanda e la risposta si coloreranno di rosso o verde rispettivamente se la risposta è sbagliata o corretta. Fatto ciò il programma passa direttamente alla domanda successiva. Al termine del numero di domande impostate all'inizio o allo scadere del tempo il quiz terminerà e mostrerà il punteggio come risposte esatte su numero di domande fatte.

Il programma è stato creato utilizzando la libreria tkinter per l'interfaccia grafica (GUI) ed utilizzando il modulo request per comunicare con l'API della banca dati delle domande. Il programma prende spunto dal corso 100 days of Python ideato da 'The App Brewery'.

Le domande sono prese da 'Open Trivia database' (https://opentdb.com/)

Il programma è diviso nei seguenti moduli:

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
  
  ## Struttura
  
  Il programma viene lanciato facendo il run del file main.py dove, come prima cosa, si importa tutte le classi che servono dai rispettivi moduli. Il primo ciclo 'for' serve per poter creare il data-set di domande da cui attingere. Dopo di che, si creano gli oggetti necessari e si fa partire il programma. Alla fine si trovano due comandi 'print' che mostrano sul terminale il punteggio a quiz finito. Per quanto riguarda gli altri moduli possiamo dire che:
  
  - ### data.py:
  Contiene la richiesta APIRESTful per accedere alle domande da fare. Del file 'json', che estrapoliamo, la parte relativa ai 'results' è quella che contiene ciò che ci serve. I dati vengono forniti sottoforma di lista di dizionari e potete osservare la struttura della lista nei commenti che trovate in fondo al modulo.
- ### question_model.py:
  Questo modulo contiene la struttura delle domande. Viene richiesto di inserire la domanda, la risposta corretta, la lista delle possibili scelte e la categoria delle domande. Questo ci permetterà di creare un lista di oggetti facili da gestire.
- ### quiz_brain.py:
  Questo modulo contiene la parte relativa al funzionamento del quiz, come attributo richiede una lsta di oggetti (lista di domande). Qui, si inizializza lo score ed il numero di domande da soministrare (self.num_test). Le funzioni presenti nella classe sono 'still_has_question', che controlla se il numero di domande fatte è superirore alle domande da fare, la funzione 'next_question', che prepara la domanda da dare alla GUI scegliendo in modo random dalla lista di domande, ed il metodo 'check_answer' che controlla la risposta. 
- ### ui.py:
  Questo modulo contiene la parte relativa all'interfaccia grafica, ed è anche il modulo più corposo. Qui trovate più funzioni che permettono il funzionamento della GUI, ovvero:
  
    - #### __init__
      Qui si inizializza tutte le componenti dello schermo, si lancia lo schermo, si fa partire il timer e si prepara la prima domanda.
    - #### count_down
      Funzione che fa scorrere il timer e aggiorna il label del timer
    - #### get_next_question
      Metodo che ci permette di configurare la domandasuccessiva qualore ci siano ancora domande da fare o il tempo non sia ancora terminato
    - #### botA_pres, botB_pres, botC_pres, botD_pres
      Azione da fare ogni qual volta si preme un pulsante (A, B, C, D)
    - #### give_feedback
      Controla se la risposta è corretta ed illumina il canvas della domanda, passa alla domanda successiva ed aggiorna il punteggio
      
      
# Commenti

I commenti sono riportati per ogni blocco di codice.

Nei metodi si trova anche una descrizione delle costanti principali che vanno inserite

