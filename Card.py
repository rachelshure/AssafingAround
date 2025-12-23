from enumns import Suit, Rank
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        if self.rank is Rank.JOKER:  
            return "Joker" 
        elif self.rank == 1:
            return f"A of {self.suit}"

        elif self.rank == 11:
            return f"J of {self.suit}"
        
        elif self.rank == 12:
            return f"Q of {self.suit}"
        
        elif self.rank == 13:
            return f"K of {self.suit}"
        
        else:
            return f"{self.rank} of {self.suit}"

        

    def __repr__(self):
        return f"{str(self)}"