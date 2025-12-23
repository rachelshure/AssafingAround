from Deck import Stack
class Hand(Stack):
    
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.cards = []

    def remove(self, card):
        self.cards.remove(card)

    def add(self, card):
        self.deck.append(card)

