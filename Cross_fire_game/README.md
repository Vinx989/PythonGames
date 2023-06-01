## Space Cross Fire  Game

Lo scopo del gico è quello di superare una zona di guerra spaziale senza farsi colpire dal fuoco nemico. Il gioco preve il superamento di 10 livelli
e per ogni livello superato aumenta la velocità dei proiettili. Questo gioco è stato creat utilizzando la libreria grafica turtle
ed è stato suddiviso in moduli 
- player: gestisce le funzionalità del giocatore
- Ship_manager: regola le funzionalità e la posizione delle navicelle nemiche
- scoreboard: regola il punteggio ed il livello


# Struttura

Il gioco è suddiviso in moduli in modo da rendere più leggibile loscript. I moduli sono i seguenti:

- ## main 
  In questo modulo trovate il main loop while che garantisce il funzionamento del gioco fin tanto che non veniamo colpiti da un proiettile o non finiamo tutti i livelli
  
- ## Player
  In questo modulo trovate tutti i comandi relativi al giocatore. Di base troviamo 3 metodi:
  - #### go_up/go_down
    Il giocatore potrà muoversi in alto o in basso 
  - ### refresch
    riporta il giocatore alla posizione iniziale ogni volta che si super un livello
 
 - ## ship_manager
   In questo modulo troviamo le funzionalità e la creazione delle navicelle nemiche. Ci sono 4 metodi:
   - ### create_battle
      Crea due file di navicelle in base al numero di navicelle impostato in partenza nella variabile NUM_SHIP
   - ### shoot
      Imposto in modo random quale navicella deve sparare
   - ### move_shoot
      Fa muovere il proiettile
   - ### level_up
      Aumenta la velocità all'aumentare del livello
