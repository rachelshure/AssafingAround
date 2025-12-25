from Deck import Deck
from Hand import Hand
from Discard import Discard
from Card import Card
from enumns import Suit, Rank
NUMBER_OF_PLAYERS = 2

controls = '''
******************************** 
* P: pick up card from deck    * 
* D: pick up card from discard * 
* S: to snap                   *
* U: use power                 *
* A: call assaf                *
* Q: quit                      *
********************************
'''
class Game:
    def __init__(self):
        # create a deck of cards
        self.discard = Discard()
        self.deck = Deck(self.discard)
        
        self.turn = 1

        self.assaf_called = False
        self.player_called_assaf = -1


        # create 2 hands
        hand1 = Hand("rachel")
        hand2 = Hand("sophie")
        self.hands = ["",hand1, hand2]

        

        self.deal(self.deck, self.hands)
        
        # testing printing handds
        self.print_table_initial()
        

        while self.assaf_called is False:
            
            hand = self.hands[self.turn]
            
            print(controls)
            self.print_table() 
            print(f"Player {self.turn}'s turn")
            print(f"Top card on deck: {self.discard.show_top_card()}")
    
            choice = input("select option P or D or U or S or A or Q : ")
            while self.valid_option(choice) is False:
                choice = input("select option P or D or U or S or A or Q : ")
            self.choose_option(hand, choice)
        
        # now assaf is called and everyone else get one more turn
        for x in range(NUMBER_OF_PLAYERS - 1):
            
            hand = self.hands[self.turn]

            print(controls)
            self.print_table() 
            print(f"Player {self.turn}'s turn")
            print(f"Top card on deck: {self.discard.show_top_card()}")

            
    
            choice = input("select option P or D or U or S or A or Q : ")
            while self.valid_option(choice) is False:
                choice = input("select option P or D or U or S or A or Q : ")
            self.choose_option(hand, choice)

        winner, result = self.results()
        print(f"Player {winner} has won with a score of {result}")
    
    def valid_option(self, option):
        match option:
            case "P":
                return True
            case "R":
                return True
            case "D":
                return True
            case "S":
                if self.discard.is_empty():
                    print("You can't snap as theres no card in the discard pile yet")
                    return False
                return True
            case "A":
                if self.assaf_called:
                    print("you can't call assaf it has already been called")
                    return False
                else:
                    return True
            case "Q":
                return True

        return False

    # return -1 for incorrect option
    # return -2 for quit
    def choose_option(self, hand: Hand, choice):
        match choice:
            case "P":
                # remove card from deck
                deck_card = self.deck.get_top_card()

                print(f"card picked up: {deck_card}")
                placing = True
                while placing:
                    option = input("P to place down, R to replace ")
                    match option:
                        case "P":
                            self.use_power(deck_card, hand)
                            placing = False
                        
                        case "R":
                            replacing = True
                            while replacing:
                                try:
                                    index = int(input("which card to replace with? "))

                                    # should check this is valid
                                    if hand.is_valid_position(index):
                                        self.replace_card(hand, deck_card, index)
                                        placing = False
                                        replacing = False
                                    else:
                                        print("not valid card option!")
                                except ValueError:
                                    print("Not an integer")
                            
                        case _:
                            print("invalid option")

                
                
            case "D":
                # should check here there is actually a card
                deck_card = self.discard.get_top_card()
                replacing = True
                while replacing:
                    index = int(input("Which card to replace with?"))
                    if hand.is_valid_position(index):
                        self.replace_card(hand, deck_card, index)
                        replacing = False
                    else:
                        print("not a valid card option!")

            case "S":
                top_discard_card = self.discard.show_top_card()
                snapping = True
                while snapping:
                    try:
                        player = int(input("Which players card do you want to snap with? "))
                        if self.is_a_player(player):
                            try:
                                index = int(input("Which do you want to snap "))
                                if hand.is_valid_position(index):
                                    card = hand.reveal(index)
                                    if self.can_snap(top_discard_card, card):
                                        print("they can be snapped!")
                                        snapping = False
                                        self.snap(hand, index)
                                    else:
                                        print("wrong those cards are not the same!")
                                        snapping = False
                                        self.penality(hand)
                                else:
                                    print("invalid card")
                            except ValueError:
                                print("Not an integer!")
                        else:
                            print("not valid player")
                    except ValueError:
                        print("not an integer!")

            case "A":
                self.call_assaf(self.turn)
                
            case "Q":
                print("goodbye ;(")
                return -2
            case _:
                print("\nINVALID OPTION\n")
                return -1
        self.next_player()

    def deal(self, deck, hands):
        # game play works by dealing 4 cards to each player initially
        for x in range (4):
            for y in range(NUMBER_OF_PLAYERS):
                hand = hands[y+1]
                hand.add(deck.get_top_card())

    def next_player(self):
        self.turn = (self.turn % NUMBER_OF_PLAYERS) + 1

    def print_table_initial(self):
        for x in range(1, NUMBER_OF_PLAYERS+1):
            print(f"Player {x}")
            self.hands[x].print_hand_initial()
            print("\n")
    
    def print_table(self):
        for x in range(1, NUMBER_OF_PLAYERS+1):
            print(f"Player {x}")
            self.hands[x].print_hand_blank()
            print("\n")
           


    def use_power(self, card: Card, hand: Hand):
        if card.is_power_card():          
            # 7 or an 8
            if card.is_78():
                # reveal one card
                self.look_at_own(hand)

            # 9 or 10 : look at someone else
            
            elif card.is_910():
                self.look_at_someone_else(hand)
            # J or Q
            elif card.is_JQ():
                self.swap_two_cards()
            # K
            elif card.is_K():
                self.look_at_two_and_swap()
        else:
            print("this is not a power card")
        self.discard.add(card)

    # replace the card with one in the hand
    def replace_card(self, hand: Hand, card_from_deck: Card, pos_in_hand: int):
        # remove card from hand 
        # removed_card = hand.remove(pos_in_hand)
        removed_card = hand.replace(card_from_deck, pos_in_hand)
        # add removed card to the deck
        self.discard.add(removed_card)


    def snap(self, hand: Hand, position):
        # should remove from hand
        c = hand.remove(position)
        # then add to the discard pile
        self.discard.add(c)

    # returns True if the top card of the discard is the same as card wanting to snap 
    def can_snap(self, discard: Card, hand: Card):
        if hand.same_rank(discard):
            return True
        return False
    
    def penality(self, hand: Hand):
        print("oops you made a mistake heres another card :)")
        c = self.deck.get_top_card()
        hand.add(c)

    def look_at_own(self, hand: Hand):
        revealing = True
        while revealing:
            try:
                index = int(input("What card to reveal? "))
                if hand.is_valid_position(index):
                    print(f"that card is: {hand.reveal(index)}")
                    revealing = False
                else:
                    print("not a correct index")
            except ValueError:
                print("Not an integer")

    def look_at_someone_else(self, hand: Hand):
        # make sure not youre own hand
        revealing = True
        while revealing:
            try:
                player = int(input("Which player would you like to look at? "))
                if self.is_a_player(player) or self.is_another_player(player):
                    other_hand: Hand = self.hands[player]
                    get_index = True
                    while get_index:
                        index = int(input("Which card would you like to look at? "))
                        if other_hand.is_valid_position(index):
                            card1 = other_hand.reveal(index)
                            print(f"that card is: {card1}")
                            get_index = False
                            revealing = False
                        else:
                            print("invalid position, try again")
                    
                else:
                    print("incorrect player!")

            except ValueError:
                print("Not an integer!")

        
    def swap_two_cards(self):
        swapping = True
        while swapping:
            try:
                player1_index = int(input("CARD 1: Which player to swap with? "))
                if self.is_a_player(player1_index):
                    if self.assaf_called and player1_index == self.player_called_assaf:
                        print("you cant swap with someone who called assaf")
                    else:
                        try:
                            card1_position = int(input(f"CARD 1: Which card from player {player1_index}? "))
                            player1: Hand = self.hands[player1_index]
                            if player1.is_valid_position(card1_position):
                                card1 = player1.reveal(card1_position)
                                try:
                                    player2_index = int(input("CARD 2: Which player to swap with? "))
                                    if self.is_a_player(player2_index):
                                        if self.assaf_called and player2_index == self.player_called_assaf:
                                            print("you can't swap with someone who called assaf")
                                        else:
                                            try:
                                                card2_position = int(input(f"CARD 2: Which card from player {player2_index}? "))
                                                player2: Hand = self.hands[player2_index]
                                                if player2.is_valid_position(card2_position):
                                                    card2 = player2.reveal(card2_position)
                                                    self.swap(card1, card2, player1, player2, card1_position, card2_position)
                                                    swapping = False
                                            except ValueError:
                                                print("Not an integer")
                                except ValueError:
                                    print("Not an integer")

                            else:
                                print("Not a valid card")
                        except ValueError:
                            print("Not an integer!")
                    

                else:
                    print("not a valid player")
            except ValueError:
                print("Not an integer!")

    def look_at_two_and_swap(self):
        swapping = True
        while swapping:
            try:
                player1_index = int(input("CARD 1: Which player to look at? "))
                if self.is_a_player(player1_index):
                    try:
                        card1_position = int(input(f"CARD 1: Which card from player {player1_index}? "))
                        player1: Hand = self.hands[player1_index]
                        if player1.is_valid_position(card1_position):
                            card1 = player1.reveal(card1_position)
                            print(f"CARD 1 is {card1}")
                            try:
                                player2_index = int(input("CARD 2: Which player to look at? "))
                                if self.is_a_player(player2_index):
                                    try:
                                        card2_position = int(input(f"CARD 2: Which card from player {player2_index}? "))
                                        player2: Hand = self.hands[player2_index]
                                        if player2.is_valid_position(card2_position):
                                            card2 = player2.reveal(card2_position)
                                            print(f"CARD 2 is {card2}")
                                            y_or_n = True
                                            while y_or_n:
                                                to_swap = input("Do you want to swap these cards? (y or n)")
                                                if to_swap == "y":
                                                    self.swap(card1, card2, player1, player2, card1_position, card2_position)
                                                    y_or_n = False
                                                elif to_swap == "n":
                                                    y_or_n = False
                                                else:
                                                    print("not correct option ")
                                            swapping = False
                                    except ValueError:
                                        print("Not an integer")
                            except ValueError:
                                print("Not an integer")

                        else:
                            print("Not a valid card")
                    except ValueError:
                        print("Not an integer!")
                else:
                    print("not a valid player")
            except ValueError:
                print("Not an integer!")

            

    def swap(self, c1: Card, c2: Card, hand1: Hand, hand2: Hand, p1, p2):
        hand1.replace(c2, p1)
        hand2.replace(c1, p2)
        # hope this is correct ngl probs not


    def is_a_player(self, player):
        if player <= NUMBER_OF_PLAYERS and player != 0:
            return True
        return False

    def is_another_player(self, other_player):
        if other_player != self.turn:
            return True
        return False
    
    def call_assaf(self, player):
        self.assaf_called = True
        self.player_called_assaf = player


    def results(self):
        top_score = 1000000000
        top_player = -1
        for h in range(1, NUMBER_OF_PLAYERS + 1):
            hand: Hand = self.hands[h]
            score = hand.score()
            if score < top_score:
                top_score = score
                top_player = h

        return top_player, top_score




my_game = Game()

# need to add if deck is empty to reshuffle
# when should this be?


"""
Player 1
c2 c3 c5
c0 c1 c4

two rows?

Blank
x x 
x x 




"""