

def display_message():
    print("Blackjack Project")


def Display_Card(card):
    print(card[0])
    print(card[1])
    print(card[2])

def main():
    display_message()
    card = ["Hearts", "Ace", 11];
    Display_Card(card)


if __name__ == '__main__':
    main()


