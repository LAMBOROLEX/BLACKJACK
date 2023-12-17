def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    scores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    deck = []
    for suit in suits:
        for score in scores:
            # ('Heart', '2')
            card = (suit, score)
            deck.append(card)
    print(deck)
    return deck




def blackjack():
    deck = create_deck()


# Running blackjack
blackjack()