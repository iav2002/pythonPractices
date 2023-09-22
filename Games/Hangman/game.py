import random

# utilizamos la lista de palabras en otro 'modulo' por no decir clase
from hangman_words import word_list
# la palabra elegida viene de la lista, de manera random
chosen_word = random.choice(word_list)
word_length = len(chosen_word) # vemos la longitud de la palabra

end_of_game = False #Variable boolean para poder acabar el juego
lives = 6 #Cantidad de vidas (siempre)

#Importamos el logo (arte en ascci)
from hangman_art import logo
print(logo)

#Testeamos el codigo con la siguiente line
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_" # esto no me queda tan claro, pero en cuando creamos una array que contenga
    #Espacios vacios 

while not end_of_game: #se utiliza la variable boleana
    guess = input("Guess a letter: ").lower()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display: #display es nuestra palabra oculta.
        print(f"You've already guessed {guess}")

    #Check guessed letter,la parte mas jodida del codigo 
    for position in range(word_length): #para la posicion en el rango del tamaño de la palabra
        letter = chosen_word[position] #letra es igual a la posicion de la palabra original
        #si fuera 'camel' empezaria por C
        if letter == guess: # Es C == user input?, si no, va a por A etc etc.
            display[position] = letter #Si la condicion se cumple, la posicion de la palabra
            #que no se ve, de cambia por la guess. (se revlela)

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"the word was'{chosen_word}'!")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    from hangman_art import stages
    print(stages[lives]) #imprime directa mente de atras pa adelante. 

