from Deck import Stack
from Card import Card
from enumns import Suit, Rank
class Hand(Stack):
    
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.number_of_cards = 4 # number of real cards

    def remove(self, pos):
        # should not remove the card from list but replace with another blank card
        # None of None
        c = self.deck[pos]
        self.deck[pos] = Card(Suit.NONE, Rank.NONE)
        self.number_of_cards -= 1
        return c
    

    def add(self, card):
        self.number_of_cards += 1
        self.deck.append(card)

    # card to replace with
    # position in hand 
    # returns the card from the hand 
    def replace(self, card, pos):
        c = self.reveal(pos)
        self.deck[pos] = card
        return c

    def reveal(self, position: int):
        if position < len(self.deck):
            return self.deck[position]
        print("error - position does not exisit")
        return -1

    def print_hand(self):
        pass
        # number_of_cards = self.number_of_cards()

        # for x in range(number_of_cards):

    # return true if valid position
    # return false if invalid position
    def is_valid_position(self, pos):
        c:Card = self.reveal(pos)
        if c != -1 and c.get_rank() != Rank.NONE and c.get_suit() != Suit.NONE:
            return True
        return False
    
    def score(self):
        my_score = 0
        for card in self.deck:
            print(card.get_value())
            my_score += card.get_value()

        return my_score


    


            

