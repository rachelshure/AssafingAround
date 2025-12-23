from Deck import Deck
from Hand import Hand

NUMBER_OF_PLAYERS = 2

# create a deck of cards
deck = Deck()

# create 2 hands
hand1 = Hand("rachel")
hand2 = Hand("sophie")


# game play works by dealing 4 cards to each player initially
for x in range (4):
    hand1.add(deck.get_top_card())
    hand2.add(deck.get_top_card())


hand1.print_deck()
hand2.print_deck()