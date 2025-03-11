from os import system
from art import logo

print(logo)

print("Welcome to the secret auction program.")

auction_details={}

def new_bidder(name, bid):
    auction_details[name] = bid
    
def find_highest_bidder(auction_details):
    highest_bid = 0

    for bidder, bid_amount in auction_details.items():
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}.")

auction = True

while auction:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    new_bidder(name, bid)
    another_bidder = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if another_bidder == "yes":
        system("clear")
    if another_bidder == "no":
        auction = False
        system("clear")
        find_highest_bidder(auction_details)
