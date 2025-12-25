from enumns import Suit, Rank
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        if self.rank is Rank.JOKER:  
            return "Joker" 
        elif self.rank == Rank.ACE:
            return f"A of {self.suit}"

        elif self.rank == Rank.JACK:
            return f"J of {self.suit}"
        
        elif self.rank == Rank.QUEEN:
            return f"Q of {self.suit}"
        
        elif self.rank == Rank.KING:
            return f"K of {self.suit}"
        
        else:
            return f"{self.rank} of {self.suit}"

        

    def __repr__(self):
        return f"{str(self)}"
    
    # If the current card is the same as other card
    def same_rank(self, other_card: Card):
        if (self.rank == other_card.rank):
            return True
        return False
    
    def is_78(self):
        if self.rank == 7 or self.rank == 8:
            return True
        return False
    
    def is_910(self):
        if self.rank == 9 or self.rank == 10:
            return True
        return False
    
    def is_JQ(self):
        if self.rank == Rank.JACK or self.rank == Rank.QUEEN:
            return True
        return False
    #NOTES 4 thinks its a JQ??
    def is_K(self):
        if self.rank == Rank.KING:
            return True
        return False
    
    def is_A(self):
        if self.rank == Rank.ACE:
            return True
        return False
    
    def is_Joker(self):
        if self.rank == Rank.JOKER:
            return True
        return False
    
    def is_blank(self):
        if self.rank == Rank.NONE and self.suit == Suit.NONE:
            return True
        return False
    
    
    def get_suit(self):
        return self.get_suit
    
    def get_rank(self):
        return self.rank
    
    def is_power_card(self):
        if self.is_78() or self.is_910() or self.is_K() or self.is_JQ():
            return True
        return False
    
    def get_value(self):
        if self.is_JQ():
            return 10
        
        elif self.is_Joker():
            return 0
        
        elif self.is_K():
            if self.suit == Suit.DIAMOND or self.suit == Suit.HEART:
                return -1
            
            else:
                return 10
            
        elif self.is_A():
            return 1

        elif self.rank == Rank.NONE and self.rank == Suit.NONE:
            return 0
        
        return self.rank
    