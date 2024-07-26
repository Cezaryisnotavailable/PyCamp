import random
from faker import Faker


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
        for player in self.players:
            while True:
                try:
                    bet = int(input(f"{player.name}, place your bet "))
                    if bet <= 0:
                        raise ValueError("Bet must be greater than zero")
                    if bet > 100:
                        raise ValueError("Maximum bet is 100")
                    if bet > player.balance:
                        raise ValueError("Not enough funds")
                    player.bet = bet
                    break
                except ValueError as e:
                    print(e)

        for _ in range(2):
            for player in self.players:
                card = self.deck.deal_card()
                player.cards.append(card)
            card = self.deck.deal_card()
            self.croupier.cards.append(card)

    def show_current_status(self):
        for index, player in enumerate(self.players):
            print(f"Player {index + 1} {player.name}")
            total_value = player.total_value_counter()
            if total_value == 21:
                player.balance += player.bet * 1.5
                self.players.remove(player)
            print("*" * 20)
        print(f"Croupier {self.croupier.name}")
        print(self.croupier.cards[0][0:2])  # only the first card is visible for the players until check


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
        self.balance = 100
        self.bet = 0

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

    def __len__(self):
        return len(self.cards)

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


game_deck = Deck()
random_players = Player.create_random_players(min_players=2, max_players=7)
game = Game(croupier=Croupier(), players=random_players, deck=game_deck)
game.start_game()
game.show_current_status()
