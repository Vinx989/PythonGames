'''
Gioco dell'impiccato
Script creato durante il corso 100 Days of Python by The AppBrewery
Script creato da Vincenzo Bruno
'''

import hangman_words
import random
import hangman_art

# Scegliamo la parola da indovinare dalla lista a disposizione
chosen_word = random.choice(hangman_words.word_list)

print(hangman_art.logo)
print("Welcome to the Hangman Game\nTry to find the word\n")

# Abbiamo 6 tentativi a disposizione
lives = 6
print(hangman_art.stages[lives]) 


display = []

#si crea questa liste per poter registrare le lettere usate
used_letter = []
number_place = len(chosen_word)

# Il ciclo for serve per creare gli spazi della parola da indovinare
for i in range(0, number_place):
  display += "_"

print(f"{' '.join(display)}")

# Main while loop che tiene vivo il gioco
end_of_game = False
while end_of_game == False:
  # Inseriamo la prima lettera
  guess = input("\nChose a letter from the alfabet\n").lower()

  # Controlliamo se abbiamo indovinato una lettera presente
  # nella parola, ovviamente controlla se abbiamo già provato
  # la lettera scelta
  if guess in used_letter:
    print(f"You already used the letter {guess }")

  else:
    # Se non la indoviniamo allora si perde una vita
    if guess not in chosen_word:
      print(f"The letter {guess} is not part of the word\nTry again")
      lives = lives-1


    for i in range(0, number_place):
    # Controlla e stampa la lettera al posto giusto
     if guess == chosen_word[i]:
        display[i] = guess

  used_letter.append(guess)   
  print(hangman_art.stages[lives])
  print(f"{' '.join(display)}")

  # Controlla se se abbiamo ancora vite o se abbiamo
  # indovinato tutte le lettere nella parola
  # al termine delle vite o se indoviniamo la parola
  # il gioco temina
  if "_" not in display:
    end_of_game=True
    print("YOU WIN")

  elif lives == 0:
    end_of_game=True
    print("\nYOU LOSE")
    print(f"The word was {chosen_word}")

  else:
    end_of_game = False
  