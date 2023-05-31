'''
Gioco del Black Jack
Script creato durante il corso 100 Days of Python by The AppBrewery
Script creato da Vincenzo Bruno
'''
import random
import art

# Liste e simboli per creare il mazzo di carte
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
vere_cards =['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
symbols = ['♥️', '♦️', '♣️', '♠️']


# Questa funzione funge da dealer. In base la tipologia fa giocare il player o il banco
# Ogni volta che esce una carta essa viene tolta dal mazzo
# Sono creati due mazzi di carte (uno numerico 'num' che serve per il conteggio
# ed uno di figure 'card' che serve come elemento visiso nel terminale). Questi mazzi sono creati prima del main loop while
def deal_card(n_carte, numero_carte, dec_card, dec_num, banco_card, banco_num, player_num, player_card, tipologia):
  '''

  :param n_carte: numero di carte da servire
  :param numero_carte:  numero di carte totali presenti nel mazzo
  :param dec_card: mazzo di carte (per le immagini)
  :param dec_num: mazzo di carte (per il conteggio)
  :param banco_card: carte del banco
  :param banco_num: carte del banco
  :param player_num: carte del giocatore
  :param player_card: carte del giocatore
  :param tipologia: decide chi sta giocando, il banco o il giocatore o entrambi
  :return: i tre mazzi di carte, del player, del banco , e le rimanenti nel mazzo
  '''
  #score_banco1=sum(banco_num)
  if tipologia == 0:# gioca solo l'utente
    for card in range(0, n_carte, 1):
      a = random.randint(0, numero_carte-1)
      player_num.append(dec_num[a])
      player_card.append(dec_card[a])
      dec_card.remove(dec_card[a])
      dec_num.remove(dec_num[a])
      numero_carte -= 1
    
  elif tipologia == 1:#gioca solo il banco
    for card in range(0, n_carte, 1):
      a = random.randint(0, numero_carte-1)
      banco_num.append(dec_num[a])
      banco_card.append(dec_card[a])
      dec_card.remove(dec_card[a])
      dec_num.remove(dec_num[a])
      numero_carte -= 1

  else: #inizia il gioco con due carte a testa
    for card in range(0, n_carte, 1):
      a = random.randint(0, numero_carte-1)
      player_num.append(dec_num[a])
      player_card.append(dec_card[a])
      dec_card.remove(dec_card[a])
      dec_num.remove(dec_num[a])
      numero_carte -= 1

      b = random.randint(0,numero_carte-1)
      banco_num.append(dec_num[b])
      banco_card.append(dec_card[b])
      dec_card.remove(dec_card[b])
      dec_num.remove(dec_num[b])
      numero_carte -= 1

  return player_card, banco_card, player_num, banco_num, numero_carte, dec_card, dec_num

# Questo metodo segna quanti soldi sono rimasti al giocatore o al banco
def soldi_rimasti(soldi_banco, soldi_player):
  '''

  :param soldi_banco: soldi rimasti al banco
  :param soldi_player: soldi rimasti al player
  :return: una varibile true/false per main loop while
  '''
  print(f"Ti sono rimasti {soldi_player} $")
  game_on = True
  if soldi_banco <= 0:
    game_on = False
    print("Il banco ha finito i soldi...cambia tavolo!")
  if soldi_player <= 0:
    game_on = False
    print("NON Hai soldi...torna con una ricarichetta!")
  return game_on

# Funzione che decide se si vuole continuare o meno il gioco
def continuo_o_no(game_on):
  '''

  :param game_on: varibile true/false per il main loop while
  :return: una varibile true/false per main loop while
  '''
  if game_on == True:
      continua = input("Vuoi fare un'altra puntata? Digita 'y' per sì o qualsiasi per no ").lower()
      if continua == 'y':
        game_on = True
        print('\n\n\n\n\n\n\n\n\n')
      else:
       game_on = False
  return game_on

# Funzione che calcola il punteggio del banco ed del player
def score_calc(banco_num, player_num, max_score, black_gioco):
  '''

  :param banco_num: sono le carte del banco
  :param player_num: sono le carte del player
  :param max_score: è il punteggio massimo (21)
  :param black_gioco: tiene traccia se hai sballato, fatto blackjack ed altro
  :return: i punteggi dei due giocatori ed il moitoraggio black_gioco
  '''
  #black_gioco=0
  score_banco = sum(banco_num)
  score_player = sum(player_num)
  if score_player == max_score and len(player_num) == 2:
    black_gioco = 1
    #print("Hai fatto Black Jack!")
  if score_player > 21 and 11 in player_num:
    #c=player_num.index[11]
    player_num.remove(11)
    player_num.append(1)
    score_player=sum(player_num)
  if score_player > max_score:
    black_gioco=2
    #print("Hai Sballato")
  if score_player > score_banco:
    black_gioco=3
  if score_banco == max_score and len(banco_num) == 2:
    black_gioco=4
    #print("Il Banco ha fatto Black Jack!")
  if score_banco > 21 and 11 in banco_num:
    banco_num.remove(11)
    banco_num.append(1)
    score_banco=sum(banco_num)
  if score_banco > max_score:
    black_gioco=5
    #print("Il Banco ha Sballato...Hai vinto!") 
  if score_player <= score_banco:
    black_gioco=6

  return black_gioco, score_banco, score_player

# Iniziamo il gioco
# Il banco ed il player partiranno con la stessa somma
print("Benvenuto al Black Jack...tenta la fortuna!")
soldi=int(input("Con quanto vuoi giocare?\n$ "))

soldi_banco = soldi
soldi_player = soldi
game_on = True

while game_on:
  dec_card = []
  dec_num = []
  print(art.logo)

  # creo i due mazzi di carte
  for card in range(0, 13, 1):
    
    for sim in range(0, 4, 1):
      a = str(vere_cards[card]) + symbols[sim]
      dec_card.append(a)
      dec_num.append(cards[card])

  # Inizializziamo tutte le liste che ci servono
  numero_carte = len(dec_card)
  banco_card = []
  banco_num = []
    
  player_num = []
  player_card = []
  black_gioco = 0
  print(f"Tu hai {soldi_player} $                 Il banco ha {soldi_banco} $")
  puntata = int(input("Quanto vuoi puntare?\n$ "))

  # Si comincia la partita dando due carte a testa e si calcola il punteggio
  first_round = deal_card(n_carte=2, numero_carte=numero_carte, dec_card=dec_card, dec_num=dec_num, banco_card=banco_card, banco_num=banco_num, player_num=player_num, player_card=player_card, tipologia=2)
  
  first_score = score_calc(banco_num=first_round[3],player_num=first_round[2],max_score=21,black_gioco=0)
  
  final_banco_card = first_round[1]
  final_banco_score = first_score[1]

  final_player_score = first_score[2]
  final_player_card = first_round[0]
  
  
  # Carte del giocatore
  print(f"Tu hai {final_player_card} ed il punteggio è {final_player_score}")
  # Carta del banco, l'altra è coperta
  print(f"Il banco ha {final_banco_card[0]} \n")
  
  
  banco_score = first_score[1]
  player_score = first_score[2]

  #controllo se ho fatto black jack e seguo le regole del gioco
  #Controllo ogni volta che il giocatore o il banco abbiamno abbastanza soldi
  game=True
  
  if black_gioco == 4:
    print("Il banco ha fatto Black Jack...Mi dispiace hai Perso")
    soldi_banco += puntata
    soldi_player -= puntata
    game_on = soldi_rimasti(soldi_banco, soldi_player)
    continuo_o_no(game_on)
    
  elif black_gioco == 1:
    print("Hai fatto Black Jack...Hai Vinto!")
    soldi_banco -= puntata
    soldi_player += puntata
    game_on = soldi_rimasti(soldi_banco, soldi_player)
    continuo_o_no(game_on)
  else:
    # continua la giocata
    game = True
    
    while game == True:
      richiesta = input("Vorresti un'altra carta? Digita 'y' per sì oppure 'n' per no ").lower()
      
      if richiesta == 'y':
        second_round = deal_card(n_carte=1, numero_carte=first_round[4], dec_card=first_round[5], dec_num=first_round[6], banco_card=first_round[1], banco_num=first_round[3], player_num=first_round[2], player_card=first_round[0], tipologia=0)
        second_score = score_calc(banco_num=second_round[3], player_num=second_round[2], max_score=21, black_gioco=0)
        final_player_score = second_score[2]
        final_player_card = second_round[0]
        player_score = final_player_score
        if player_score > 21:
          game = False
          black_gioco = 2
       
        print(f"Tu hai {final_player_card} ed il punteggio è {final_player_score}\n")
        print(f"Il banco ha {final_banco_card[0]} \n")
        first_round = second_round
      elif richiesta =='n':
        game = False
        print(f"Il banco ha {final_banco_card} ed il punteggio è {final_banco_score}\n")
    
        while player_score > banco_score and banco_score < 21:
          enesimo_round = deal_card(n_carte=1, numero_carte=first_round[4], dec_card=first_round[5], dec_num=first_round[6], banco_card=first_round[1], banco_num=first_round[3], player_num=first_round[2], player_card=first_round[0], tipologia=1)
          first_score = score_calc(banco_num=enesimo_round[3], player_num=enesimo_round[2], max_score=21, black_gioco=0)
          final_banco_score = first_score[1]
          final_banco_card = enesimo_round[1]
          banco_score = first_score[1]
          
          
          print(f"Il banco ha {final_banco_card} ed il punteggio è {final_banco_score}\n")
          
      else:
        print("Digita correttamente")
    
      
    print(f"Tu hai {final_player_card}  il BANCO ha {final_banco_card}\n")     
    print(f"Il TUO punteggio è {final_player_score} mentre il BANCO fa {final_banco_score}\n")
    
  
    if black_gioco == 5 or final_banco_score > 21:
      print("Il banco ha Sballato...Hai Vinto!")
      soldi_banco -= puntata
      soldi_player += puntata
      game_on = soldi_rimasti(soldi_banco, soldi_player)
      game_on = continuo_o_no(game_on)

    elif black_gioco == 2:
      print("Tu hai Sballato...Mi dispiace hai Perso!")
      soldi_banco += puntata
      soldi_player -= puntata
      game_on = soldi_rimasti(soldi_banco, soldi_player)
      game_on = continuo_o_no(game_on)

    elif black_gioco == 3:
      print("Il tuo punteggio è più alto...Hai Vinto!")
      soldi_banco -= puntata
      soldi_player += puntata
      game_on = soldi_rimasti(soldi_banco, soldi_player)
      game_on = continuo_o_no(game_on)

    elif black_gioco == 6:
      print("Il punteggio del banco è più alto...Mi dispiace hai Perso!")
      soldi_banco += puntata
      soldi_player -= puntata
      game_on = soldi_rimasti(soldi_banco, soldi_player)
      game_on = continuo_o_no(game_on)

    else:
      print("Il banco vince...Mi dispiace hai Perso!")
      soldi_banco += puntata
      soldi_player -= puntata
      game_on = soldi_rimasti(soldi_banco,soldi_player)
      game_on = continuo_o_no(game_on)

