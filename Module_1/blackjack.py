import random
from faker import Faker


# po inicjalizacji deck trzeba bedzie aktualziwoac deck po rozdaniu kart
class Game:
    def __init__(self, croupier, players, deck):
        self.croupier = croupier
        self.players = players
        self.deck = deck

    def start_game(self):
        """
        Shuffles the deck and deals two cards to each player in the game.
        """
        self.deck.shuffle()
        for _ in range(2):
            for player in self.players:
                    card = self.deck.deal_card()
                    player.cards.append(card)
            card = self.deck.deal_card()
            self.croupier.cards.append(card)

    def show_current_status(self):
        for index, player in enumerate(self.players):
            print(f"Player {index + 1} {player.name}")
            player.total_value_counter()
            print("*" * 20)

        print(f"Croupier {self.croupier.name}")
        print(self.croupier.cards[0][0:2]) # only the first card is visible for the players until check



class NoCardsException(Exception):
    """
    Exception raised when a player has no cards in their hand.
    """
    pass


class Human:
    def __init__(self):
        self.cards = []
        self.name = ""

    def total_value_counter(self):
        total_value = 0
        if not self.cards:
            raise NoCardsException("Player has no cards in hand")
        for i, (suit, rank_name, value) in enumerate(self.cards):
            # if 10 < rank < 14:
            #     rank = 10
            # elif rank == 14:
            #     while True:
            #         try:
            #             chosen_value = int(input(f"You got ace ({suit}-{rank}). Please choose your value 1 or 11"))
            #             if chosen_value not in (1, 11):
            #                 raise ValueError("Invalid value, please enter 1 or 11")
            #             break
            #         except ValueError as e:
            #             print(e)
            #     rank = chosen_value
            if self.cards[0][1] == "Ace" and rank_name == "Ace":
                value = 1

            total_value += value
            print(f"Card no. {i + 1} is {suit}-{rank_name}")
        print(f"Total value is {total_value}")
        return total_value






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
            players.append(player)
        return players



class Croupier(Human):
    def __init__(self):
        super().__init__()
        fake = Faker()
        self.name = fake.name()


class Deck:
    RANKS = {
        2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
        10: '10', 11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'
    }

    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        """create all possible card combinations"""
        for suit in self.SUITS:
            for rank, rank_name in self.RANKS.items():
                value = rank if rank < 11 else 10
                if rank == 14:
                    value = 11

                self.cards.append((suit, rank_name, value))


    def shuffle(self):
        """ shuffle the deck"""
        random.shuffle(self.cards)

    def deal_card(self):
        """remove and return the last card"""
        return self.cards.pop()



deck = Deck()
random_players = Player.create_random_players(min_players=2, max_players=7)
game = Game(croupier=Croupier(), players=random_players, deck=deck)
game.start_game()
game.show_current_status()





