from blackjack import Deck


def test_deck_no_of_cards():
    deck = Deck()
    assert len(deck.cards) == 52

