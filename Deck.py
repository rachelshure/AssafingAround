from Card import Card
from enumns import Rank, Suit
from Stack import Stack
import random

class Deck(Stack):
    def __init__(self):
        super().__init__()
        self.create_deck()
        self.shuffle()

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

    def shuffle(self):
        random.shuffle(self.deck)

    def get_top_card(self):
        return self.deck.pop()
