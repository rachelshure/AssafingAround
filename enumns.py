from enum import Enum

class Suit(Enum):
    HEART = "hearts"
    DIAMOND = "diamonds"
    SPADE = "spades"
    CLUB = "clubs"
    NONE = "none"

    
    def __str__(self):
        return self.value



class Rank(Enum):
    ACE = "ace"
    KING = "king"
    QUEEN = "queen"
    JACK = "jack"
    JOKER = "joker"
    NONE = " "
    
    def __str__(self): 
        return self.value


