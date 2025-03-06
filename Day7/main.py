import random
from hangman_words import word_list
from hangman_art import stages, logo2, logo3

print(logo3)

chosen_word = random.choice(word_list)

placeholder = ""
for letter in chosen_word:
    placeholder += "_"
print(placeholder)

game_over = False

correct_letters = []
lives = 6
guessed_letters = []

while not game_over:
    print(stages[lives])

    guess = input("Please guess a letter: ").lower()
    if len(guess) > 1:
        print("Please guess one letter at a time")
    else:

        if guess in guessed_letters:
            print(f"You already guessed {guess}, guess again.")
        else: 
            guessed_letters.append(guess)

            display = ""

            for letter in chosen_word:
                if letter == guess:
                    display += letter
                    correct_letters.append(letter)
                elif letter in correct_letters:
                    display += letter
                else:
                    display += "_"

            print(display)

            if guess not in chosen_word:
                lives -= 1
                print(f"You guessed {guess}, that's not in the word. You lose a life.")
                if lives == 0:
                    game_over = True
                    print(stages[0])
                    print("You lose!")
                    print(f"The word was {chosen_word}.")

            if "_" not in display:
                game_over = True
                print("You win!")
                print(f"The word was {chosen_word}.")
                print(logo2)
