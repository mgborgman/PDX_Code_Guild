values = ['Ace', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']


class Deck():
    pass


class Card():
    def __init__(self, suit, color, value):
        self.suit = suit
        self.color = color
        self.value = value


def create_deck():
    for item in values:
        item = Card('spades', 'black', item)


create_deck()


