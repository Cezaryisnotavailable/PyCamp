import random

import pytest
from pytest_mock import mocker


from blackjack import Deck, Human, NoCardsException, Croupier, Player, Game


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


def test_game(mocker, deck):
    croupier = Croupier()
    player1 = Player()
    player2 = Player()
    player3 = Player()
    mocker.patch("builtins.input", side_effect=[50, 75, 100])
    game = Game(croupier=croupier, players=[player1, player2, player3], deck=deck)
    game.start_game()

    assert player1.bet == 50
    assert player2.bet == 75
    assert player3.bet == 100


def test_game_show_current_status(deck, capsys):
    # Create a test game with a croupier and players
    croupier = Croupier()
    player1 = Player()
    player2 = Player()
    game = Game(croupier=croupier, players=[player1, player2], deck=deck)

    # Set up player cards and bets for testing
    player1.cards = [('Hearts', 'Ace', 11), ('Spades', 'King', 10)]
    player1.bet = 50
    player1.balance = 100

    player2.cards = [('Diamonds', '8', 8), ('Clubs', '7', 7)]
    player2.bet = 75
    player2.balance = 100

    croupier.cards = [('Diamonds', '6', 6), ('Clubs', '6', 6)]

    # Call the method to be tested
    game.show_current_status()

    # Assert that the total value is correctly calculated and displayed
    expected_output = "Player 1 " + player1.name + "\n"
    expected_output += "Card no. 1 is Hearts-Ace\n"
    expected_output += "Card no. 2 is Spades-King\n"
    expected_output += "Total value is 21\n"
    expected_output += "********************\n"
    expected_output += "Player 2 " + player2.name + "\n"
    expected_output += "Card no. 1 is Diamonds-8\n"
    expected_output += "Card no. 2 is Clubs-7\n"
    expected_output += "Total value is 15\n"
    expected_output += "********************\n"

    assert capsys.readouterr().out == expected_output


def test_no_cards_exception():
    croupier = Croupier()
    player1 = Player()
    with pytest.raises(NoCardsException) as exc_info:
        croupier.total_value_counter()
    assert str(exc_info.value.args[0]) == "Player has no cards in hand"

    with pytest.raises(NoCardsException) as exc_info:
        player1.total_value_counter()
    assert str(exc_info.value.args[0]) == "Player has no cards in hand"













