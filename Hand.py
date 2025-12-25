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

    def print_hand_blank(self):
        row0 = ""
        row1 = ""
        for x in range(0, 2):
            card: Card = self.deck[x]
            if card.is_blank() is False:
                row0 += "X "
            else:
                row0 += "  "

        for y in range(2, 4):
            card: Card = self.deck[y]
            if card.is_blank() is False:
                row1 += "X "
            else:
                row1 += "  "

        for z in range(4, len(self.deck), 2):
            card: Card = self.deck[z]
            if card.is_blank() is False:
                row0 += "X "
            else:
                row0 += "  "
            try:
                card: Card = self.deck[z+1]
                if card.is_blank() is False:
                    row1 += "X "
                else:
                    row1 += "  "
            except:
                row1 += "  "

        
        print(row1)
        print(row0)


    def print_hand_initial(self):
        row0 = ""
        row1 = ""
        for x in range(0, 2):
            card: Card = self.deck[x]
            if card.is_blank() is False:
                row0 += str(card) + ", "
            else:
                row0 += "  "

        for y in range(2, 4):
            card: Card = self.deck[y]
            if card.is_blank() is False:
                row1 += "X "
            else:
                row1 += "  "

        for z in range(4, len(self.deck), 2):
            card: Card = self.deck[z]
            if card.is_blank() is False:
                row0 += "X "
            else:
                row0 += "  "
            try:
                card: Card = self.deck[z+1]
                if card.is_blank() is False:
                    row1 += "X "
                else:
                    row1 += "  "
            except:
                row1 += "  "

        
        print(row1)
        print(row0)


       

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
            my_score += card.get_value()

        return my_score


    


            

