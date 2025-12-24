from Deck import Stack

class Discard(Stack):
    def __init__(self):
        super().__init__()

    

    def get_top_card(self):
        
        if (self.is_empty()):
            return -1
        return self.deck.pop()
    
    def show_top_card(self):
        if (self.is_empty()):
            return -1
        return self.deck[-1]