from Card import Card
from enumns import Rank, Suit
from Stack import Stack
from Discard import Discard
import random

class Deck(Stack):
    def __init__(self, discard: Discard):
        super().__init__()
        self.create_deck()
        self.shuffle()
        self.discard = discard

    def create_deck(self):
        suits = [Suit.CLUB, Suit.DIAMOND, Suit.SPADE, Suit.HEART]
        for suit in suits:
            self.deck.append(Card(suit, Rank.ACE))
            for number in range(2, 11):
                card = Card(suit, number)
                self.deck.append(card)
            self.deck.append(Card(suit, Rank.JACK))
            self.deck.append(Card(suit, Rank.QUEEN))
            self.deck.append(Card(suit, Rank.KING))

        self.add_jokers()

    def add_jokers(self):
        self.deck.append(Card(Suit.NONE, Rank.JOKER))
        self.deck.append(Card(Suit.NONE, Rank.JOKER))

    def shuffle(self):
        random.shuffle(self.deck)

    def get_top_card(self):
        if self.is_empty():
            self.reshuffle()

        return self.deck.pop()
    
    def reshuffle(self):
        # Shuffle 3 times
        self.discard.shuffle()
        self.discard.shuffle()
        self.discard.shuffle()
        # add all cards from discard pile to the deck
        for card in self.discard:
            self.deck.append(card)
    
    def show_top_card(self):
        return self.deck[-1]
    
