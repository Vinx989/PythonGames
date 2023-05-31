# Black Jack Game

Questo programma è stato creato durante il corso online di 100 Days of Python ideato da 'The App Brewery'

Il programma ha lo scopo di simulare il gioco del Black Jack
Il programma è stato sviluppato nella modalità Player Vs COM. Inizialmente si sceglie la somma totale che si vuole portare al banco.
Il banco ed il giocatore avranno la stessa cifra.
Per ogni giocata si può scegliere quanto puntare.
Il gioco finisce quando finiscono i soldi di uno dei due oppure quando lo decide il Player

# Struttura del gioco

Nel gioco il tutto viene gestito dal main loop while con la condizione true/false indicata dalla variabile game_on.

Dopo aver dato le prime due carte ad entrambi i giocatori, il programma controlla se tu o il banco ha fatto black Jack. Se si, interrompe la puntata e va alla prossima. In caso contrario, il gioco continua con un altro loop while con la condizione true/false indicata dalla variabile game. Nell'eventualità che uno dei due superi il punteggio massimo consentito il gioco assegna la vittoria della puntata all'altro giocatore.

I metodi principali presenti nello script sono:

### deal_card
Questa funzione funge da dealer. In base la 'tipologia' fa giocare il player o il banco oppure entrambi. Ogni volta che esce una carta essa viene tolta dal mazzo.
Prima del main while loop sono creati due mazzi di carte (uno numerico 'num' che serve per il conteggio ed uno di figure 'card' che serve come elemento visiso nel terminale). 

### soldi_rimasti
Questo metodo segna quanti soldi sono rimasti al giocatore o al banco.

### continuo_o_no
Funzione che decide se si vuole continuare o meno il gioco a puntata finita.

### score_calc
Funzione che calcola il punteggio del banco ed del player. In questa funzione si determina se si ha sballato, fatto black jack o altro.

# Commenti

I commenti sono riportati per ogni blocco di codice. 

Nei metodi si trova anche una descrizione dei parametri che vanno inseriti 


