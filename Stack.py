from Card import Card
class Stack():
    def __init__(self):
        self.deck = []

    def is_empty(self):
        if len(self.deck) == 0:
            return True
        return False

    def print_deck(self):
        for card in self.deck:
            print(repr(card))

    def add(self, card):
        self.deck.append(card)

    
    
    def number_of_cards(self):
        return len(self.deck)

    