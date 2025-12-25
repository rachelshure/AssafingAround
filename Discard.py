from Deck import Stack
import random

class Discard(Stack):
    def __init__(self):
        super().__init__()

    def shuffle(self):
        random.shuffle(self.deck)
    

    def get_top_card(self):
        
        if (self.is_empty()):
            return -1
        return self.deck.pop()
    
    def show_top_card(self):
        if (self.is_empty()):
            return -1
        return self.deck[-1]
    
    # def remove_first_card(self):
    #     self.deck.remove[]