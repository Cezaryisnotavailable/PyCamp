import random
from faker import Faker


# po inicjalizacji deck trzeba bedzie aktualziwoac deck po rozdaniu kart
class Game:
    def __init__(self, croupier, players, deck):
        self.croupier = croupier
        self.players = players
        self.deck = deck

    def start_game(self):
        self.deck.shuffle()
        for player in self.players:
            for _ in range(2):
                card = self.deck.deal_card()
                player.cards.append(card)



class Human:
    def __init__(self):
        self.cards = []
        self.name = ""


class Player(Human):
    def __init__(self):
        super().__init__()
        fake = Faker()
        self.name = fake.name()

    @classmethod
    def create_random_players(cls, min_players=2, max_players=7):
        num_players = random.randint(min_players, max_players)
        players = []
        for i in range(num_players):
            player = cls()


class Croupier(Human):
    def __init__(self):
        super().__init__()
        fake = Faker()
        self.name = fake.name()


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


random_players = Player.create_random_players(min_players=2, max_players=7)
game = Game(croupier=Croupier(), )
deck = Deck()


