
import csv
import db
from random import randint
import random
import sys


def card_value(card): # a function to get value of card from suits
    if card[:1] in ('JACK', 'KING', 'QUEEN'): # if card is Jack, King, or Queen
        return int(10)
    elif card[:1] in ['2', '3', '4', '5', '6', '7', '8', '9']: #if card is a number
        return int(card[:1])
    elif card[:1] == 'ACE':                    # if card is ace
        return int(11)

def take_card(deck):  # a function to get card from deck
    return deck[randint(0, len(deck) - 1)]

def remove_card(deck, card):             # function to remove card from deck
    return deck.remove(card)


#display menu
print("BLACKJACK!")
print("Blackjack payout is 3:2\n")

# getting user input
#starting_money = input("Starting money:    ")
#bet_amount = input("Bet amount:        ")

total_money = 100
bet_money = 0
play_money = ''

#play_again = input("Play again? (y/n):  ")
#while play_again != "n":

while True: # Bring to bring back the user to choose if to play or not
    values = ['2', '3', '4', '5', '6', '7', '8', '9', 'JACK', 'KING', 'QUEEN', 'ACE'] # card and value it holds
    suits = ['CLUBS', 'DIAMONDS', 'HEARTS', 'SPADES']
    deck = [] # deck to store all cards
    try:
        with open("money.txt") as file:
            money_in_file = file.read()
            print(f"Money: {money_in_file}")
    except FileNotFoundError:
        print("File not found.  Closing program")
        sys.exit(1)
    except Exception as e:
        print("unexpected error ", type(e), e)
        print("Shutting down program")
        sys.exit(1)

    for x in suits: # get all cards and store in deck
        for y in values:
            deck.append(x + ' of ' + y)
    while True:
        try:
            bet_money = int(input("Bet amount: "))      # input to get bet amount from  player
            if bet_money < 5 or bet_money > 1000:
                print("Minimum bet is 5 and Maximum bet should be 1000")
                continue
            else:
                break
        except ValueError:
            print("Bet amount must be an integer")
            continue



    player_hand = []
    dealer_hand = []
# to get player 3 first cards
    card_one = take_card(deck)
    remove_card(deck, card_one)
    card_two = take_card(deck)
    remove_card(deck, card_two)
    player_hand.append(card_one)
    player_hand.append(card_two)

    print("YOUR CARDS: ")
    print(card_one + "\n" + card_two)
    player_value_one = card_value(card_one)
    player_value_two = card_value(card_two)
    player_hand_total = player_value_one + player_value_two

    print("DEALER CARDS: ") # to get dealer's card, hide the other
    print(card_one + "\n" + card_two)
    dealer_hand_one = take_card(deck)
    remove_card(deck, dealer_hand_one)
    dealer_hand_two = take_card(deck)
    remove_card(deck, dealer_hand_two)

    dealer_value_one = card_value(dealer_hand_one)
    dealer_value_two = card_value(dealer_hand_two)
    dealer_hand_total = dealer_value_one + dealer_value_two
    print(dealer_hand_one)
    dealer_hand.append(dealer_hand_one)
    dealer_hand.append(dealer_hand_two)

    if player_hand_total == 21:
        print("You win!")
        total_money = round(total_money + bet_money * 1.5)
        print(f"Money: {bet_money}")
        play_again = input("Play again (y/n")
    else:
        while player_hand_total < 21 and play_again != "n":
            player_selection = input("Hit or Stand? (hit/stand) : ")
            if player_selection == "hit":

                new_card_player = take_card(deck) # obtain card from deck and kep adding to player's value
                remove_card(deck, new_card_player)
                new_card_value = card_value(new_card_player)
                player_hand_total += int(new_card_value)
                player_hand.append(new_card_player)

                print("Your cards: ")
                for x in range(len(player_hand)):
                    print(player_hand[x])
                if player_hand_total > 21:
                    print("You busted")
                    print("Sorry. you lose")
                    total_money = total_money - bet_money
                    print(f"Money: {total_money}")
                    play_again = input("Play again (y/n")
                else:
                    continue
            elif player_selection == "stand":
                if dealer_hand_total < 17: # obtain card from deck and kep adding to dealer's value
                    new_card_dealer = take_card(deck)
                    dealer_card_value = take_card(new_card_dealer)
                    print(f"This card is a {new_card_dealer}")
                    dealer_hand_total += int(dealer_card_value)
                    dealer_hand.append(new_card_dealer)

                    print("DEALER's CARDS:")
                    for i in range(len(dealer_hand)):
                        print(dealer_hand[i])
                    if dealer_hand_total > 21 and player_hand_total <= 21:
                        print("Dealer busted! You win.")
                        total_money = round(total_money + bet_money)
                        print(f"Money: {total_money}")
                    elif dealer_hand_total < 21 and dealer_hand_total > player_hand_total:
                        print(f"YOUR POINTS: {player_hand_total}")
                        print(f"DEALER'S POINTS: {dealer_hand_total}")
                        total_money = total_money - bet_money
                        print("Sorry. you lose")
                        print(F"MONEY: {total_money}")
                    else:
                        continue
                elif dealer_hand_total == player_hand_total: # if dealer and player has equal value
                    print("It's a tie!")
                elif dealer_hand_total < player_hand_total:      #if dealer hand is less value than player hand
                    print(f"YOUR POINTS: {player_hand_total}")
                    print(f"DEALER'S POINTS: {dealer_hand_total}")
                    total_money = total_money + bet_money
                    print("You win!")
                    print(f"MONEY: {total_money}")
                else:                                           # if value of card in dealer's hand is more than value in player's hand
                    print(f"YOUR POINTS: {player_hand_total}")
                    print(f"DEALER'S POINTS {dealer_hand_total}")
                    total_money = total_money - bet_money
                    print("Sorry. you lose")
                    play_again = input("Play again? (y/n):  ")
                    if play_again.lower() != "y":                  # if a player wants to play again
                        print("come back soon")
                        break








