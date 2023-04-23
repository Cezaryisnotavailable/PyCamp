import random


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        """create all possible card combinations"""
        for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
            for rank in range(1, 14):
                self.cards.append((suit, rank))

    def shuffle(self):
        """ shuffle the deck"""
        random.shuffle(self.cards)

    def deal_card(self):
        """remove and return the last card"""
        return self.cards.pop()


deck = Deck()
print(deck.cards)

