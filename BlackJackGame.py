
import csv
import db
from random import randint
import random



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
while True:
    values = ['2', '3', '4', '5', '6', '7', '8', '9', 'JACK', 'KING', 'QUEEN', 'ACE']
    suits = ['CLUBS', 'DIAMONDS', 'HEARTS', 'SPADES']
    deck = []
    with open("money.txt") as file:
        money_in_file = file.read()
        print(f"Money: {money_in_file}")

    for x in suits: # get all cards and store in deck
        for y in values:
            deck.append(x + ' of ' + y)

    bet_money = int(input("Bet amount: "))      # get bet amount from  player
    print()

    player_hand = []
    dealer_hand = []

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

    print("DEALER CARDS: ")
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
                new_card_player = take_card(deck)
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
                if dealer_hand_total < 17:
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
                elif dealer_hand_total == player_hand_total:
                    print("It's a tie!")
                elif dealer_hand_total < player_hand_total:
                    print(f"YOUR POINTS: {player_hand_total}")
                    print(f"DEALER'S POINTS: {dealer_hand_total}")
                    total_money = total_money + bet_money
                    print("You win!")
                    print(f"MONEY: {total_money}")
                else:
                    print(f"YOUR POINTS: {player_hand_total}")
                    print(f"DEALER'S POINTS {dealer_hand_total}")
                    total_money = total_money - bet_money
                    print("Sorry. you lose")
                    play_again = input("Play again? (y/n):  ")
                    if play_again.lower() != "y":
                        print("come back soon")
                    else:

                        break








