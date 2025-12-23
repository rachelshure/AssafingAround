from Card import Card
from enumns import Rank, Suit

class Deck():
    def __init__(self):
        self.deck = []
        self.create_deck()

    def create_deck(self):
        suits = [Suit.CLUB, Suit.DIAMOND, Suit.SPADE, Suit.HEART]
        for suit in suits:
            for number in range(1, 14):
                card = Card(suit, number)
                self.deck.append(card)
        self.add_jokers()

    def add_jokers(self):
        self.deck.append(Card(Suit.NONE, Rank.JOKER))
        self.deck.append(Card(Suit.NONE, Rank.JOKER))

    def shuffle():
        pass

    # returns the top card
    def pop():
        pass

    def isEmpty():
        pass

    def print_deck(self):
        for card in self.deck:
            print(repr(card))
