import random

import pytest

from blackjack import Deck, Human, NoCardsException, Croupier, Player


@pytest.fixture()
def deck():
    deck = Deck()
    return deck


def test_deck_no_of_cards(deck):
    assert len(deck.cards) == 52
    assert len(deck.cards) != 53


def test_deck_colours_values(deck):
    assert ('Hearts', '3', 3) in deck.cards
    assert ('Diamonds', '3', 3) in deck.cards
    assert ('Diamonds', 'Ace', 11) in deck.cards
    assert ('Diamonds', '4', 3) not in deck.cards



def test_pop_deck(deck):
    popped_card = deck.deal_card()
    assert len(deck) != 52  # len(deck) can be used because def __len__(self) is defined in Deck
    assert popped_card not in deck.cards


def test_shuffle_deck(deck):
    random_index = random.randint(0, len(deck))
    random_pick = deck.cards[random_index]
    deck.shuffle()
    assert random_pick != deck.cards[random_index]


def test_human_creation():
    human = Human()
    assert human.cards == []
    assert human.name == ""
    assert human.name != " "
    assert len(human.cards) == 0
    with pytest.raises(NoCardsException) as exc_info:
        human.total_value_counter()
    assert str(exc_info.value.args[0]) == "Player has no cards in hand"


def test_croupier():
    croupier = Croupier()
    assert croupier.name != ""
    assert croupier.cards == []


def test_player():
    player = Player()
    assert player.name != ""
    assert player.cards == []
    assert player.balance == 100
    assert player.bet == 0
    assert len(player.create_random_players()) in range(2, 8)
    assert len(player.create_random_players(3, 10)) in range(3, 11)








