from Deck import Stack

class Discard(Stack):
    def __init__(self):
        super().__init__()

    def add(self, card):
        self.deck.append(card)