import random
import os
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def calculate_score(hand):
    score = sum(hand)
    while score > 21 and 11 in hand: # handle ace as 11 or 1
        hand[hand.index(11)] = 1
        score = sum(hand)
    return score


def deal_computer_cards():
    computer_cards = random.choices(cards, k=2)
    while calculate_score(computer_cards) < 17: # check to see if dealer must hit
        computer_cards.append(random.choice(cards))
    return computer_cards

    
def play_blackjack():
    player_cards = random.choices(cards, k=2)
    player_score = calculate_score(player_cards)

    computer_cards = deal_computer_cards()
    computer_score = calculate_score(computer_cards)

    # Blackjack check
    if player_score == 21 and len(player_cards) == 2:
        print(f"    Your cards: {player_cards}, current score: {player_score}")
        print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
        if computer_score == 21 and len(computer_cards) == 2:
            print("Both have Blackjack! It's a tie!")
        else:
            print("Blackjack! You win!")
        return # Skip the rest of the loop and start a new game

    print(f"    Your cards: {player_cards}, current score: {player_score}")
    print(f"    Computer's first card: {computer_cards[0]}")

    while player_score <= 21:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if another_card == 'y':
            player_cards.append(random.choice(cards))
            player_score = calculate_score(player_cards)

            print(f"    Your cards: {player_cards}, current score: {player_score}")
            print(f"    Computer's first card: {computer_cards[0]}")

            if player_score > 21:
                print(f"   Your final hand: {player_cards}, final score: {player_score}")
                print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
                print("You went over. You lose.")
                break

        elif another_card == 'n':
            print(f"    Your final hand: {player_cards}, final score: {player_score}")
            print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
            break

    if computer_score > 21:
        print("Opponent went over. You win!")
    elif computer_score == player_score:
        print("It's a tie!") 
    elif player_score <= 21 and player_score > computer_score:
        print("You win!")
    elif computer_score > player_score:
        print("You lose!")


while input("Play a game of Blackjack? 'y' or 'n': ") == 'y':
    os.system('cls' if os.name== 'nt' else 'clear')
    print(logo) 
    play_blackjack()
