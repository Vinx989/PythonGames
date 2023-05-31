'''
Questo gioco di sasso carta e forbice è stato creato durante il coso
100 Days of Pytho ideato da 'The App Brewery'

Il gioco prevede la possibilità di giocare contro il COM e di vincere
al meglio delle 3

Il gioco è stato crato solo con l'utilizzo di cicli for ed if/else
'''

# the ASCII art per creare un effetto visivo
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

#inizia il gioco
print("Welcome to the rock, paper and scissor game!\nTry to win over 3 games")

my_score = 0
com_score = 0

# Fa giocare i giocatori per tre volte e poi controlla chi ha vinto
# Ad ogni ciclo stampa il punteggio
for i in range(0, 3, 1):
 # inserisco la mia scelta
 mia_scelta=input("Insert 'r' for Rock, 's' for scissor, or 'p' for paper\n")

 mia_scelta=mia_scelta.lower()
 com_scelta=random.randint(0,2)
 com_fig=[paper, scissors, rock]
 com_name=['paper', 'scissors', 'rock']
 
 # Con questo ciclo if vedo se l'utente ha digitato correttamente
 if mia_scelta == 'r' or mia_scelta == 's' or mia_scelta == 'p':

  # Per ogni mia possibilità faccio giocare il PC ed analizzo i casi di vittoria, pareggio sconfitta
  if mia_scelta == 'r':
    print(rock)
    print(f"The PC chose {com_name[com_scelta]}")
    print(com_fig[com_scelta])

    if com_scelta == 2:
      print("You Drow!")
    elif com_scelta == 1:
      print("You Win!")
      my_score += 1
    else:
      print("You Lose!")
      com_score += 1
      
  elif mia_scelta == 's':
    print(scissors)
    print(f"The PC chose {com_name[com_scelta]}")
    print(com_fig[com_scelta])
    if com_scelta == 1:
      print("You Drow!")
    elif com_scelta == 0:
      print("You Win!")
      my_score += 1
    else:
      print("You Lose!")
      com_score += 1
      
  elif mia_scelta == 'p':
    print(paper)
    print(f"The PC chose {com_name[com_scelta]}")
    print(com_fig[com_scelta])
    if com_scelta == 0:
      print("You Drow!")
    elif com_scelta == 3:
      print("You Win!")
      my_score += 1
    else:
      print("You Lose!")
      com_score += 1
  else:
    print("Something went wrong!")
  
 else:
  print("Error in typing!\nRun it again!")

# Controllo il programma e finisco il gioco
if my_score > com_score:
 print(f"Wow You WIN! The score is \nYou {my_score} Vs COM {com_score}")

if my_score < com_score:
 print(f"I am sorry... You Lost! The score is \nYou {my_score} Vs COM {com_score}")

if my_score == com_score:
 print(f"Seems nobody wins! The score is \nYou {my_score} Vs COM {com_score}")



