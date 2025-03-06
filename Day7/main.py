import random
from hangman_words import word_list
from hangman_art import stages, logo2, logo3

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for letter in chosen_word:
    placeholder += "_"

print(placeholder)

game_over = False

correct_letters = []
lives = 6

while not game_over:
    print(stages[lives])

    guess = input("Please guess a letter: ").lower()

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
        if lives == 0:
            game_over = True
            print(stages[0])
            print("You lose!")

    if "_" not in display:
        game_over = True
        print("You win!!")
