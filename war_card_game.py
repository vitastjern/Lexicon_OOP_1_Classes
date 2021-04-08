# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time, face down.
# Anyone may deal first. Each player places his stack of cards face down, in front of him/her.

# The play:

# Each player turns up a card at the same time and the player with the higher card takes both cards 
# and puts them, face down, in the bottom of his/her stack.
# If the cards are of the same rank, it is WAR! Each player turns up three cards face down and one card
# face up. The player with the higher card takes both piles (six cards). If the turned-up cards are
# again the same rank, each player places another card face down and turns another card face up.
# The player with the higher card takes all 10 cards and so on...

from random import shuffle

SUITE = "H D S C".split()
RANKS = "2 3 4 5 6 7 8 9 10 J D K A".split()

class Deck:
    # This is the Deck class. This object will create a deck of cards to initiate play.
    # You can then use this Deck list of cards to split in half and give to the players.
    # It will use SUIT and RANKS to create the deck. It should also have a method for splitting/cutting
    # and shuffle the deck.
    the_deck = []
    left = []
    right = []

    def __init__(self):
        print("Init the deck")
        for x in RANKS:
            for y in SUITE:
                self.the_deck.append(x+y) # 2H 3H 
        shuffle(self.the_deck)
        #print(self.the_deck)  # [ '5D', 'AS', .. ]
        #shuffle(self.the_deck)
        #print(self.the_deck)
    
    def split(self):  # split the deck in 2 equal halves
        self.left = self.the_deck[:len(self.the_deck)//2]
        self.right = self.the_deck[len(self.the_deck)//2:]
        #print("Left:", self.left)
        #print("Right:", self.right)


class Hand(Deck):
    # Each player has a Hand, and can add or remove cards from that hand.
    # There should be an add and a remove card method here.
    hand = []
    def __init__(self, hand):
        #print("Init the user's hand")
        self.hand = hand
        #print(hand)
        #print("This is the user's hand", self.hand)

    def add_card(self, cards):  # <desk> <put new cards here> AD 5S ... <top of pile>
        self.hand = cards + self.hand

    def remove_card(self):
        self.hand.pop()   # cards are removed from the top (but added to the bottom)

    def print_hand(self):
        print(self.hand)


class Player(Hand):
    # The Player class takes in a name and an instance of a Hand class object.
    # The player can then play cards and check if they still have cards.
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
        self.table = []
        #print(self.hand)

    def play_cards(self, nr_of_cards):
        # when you play cards, you remove them from the hand and put them on the table
        # you need to know which cards you removed and save to your "table"-position
        # take the card from the top of the hand, put it at the bottom of the table stack
        for _ in range(nr_of_cards):
            #print(self.name)
            self.table.append(self.hand[-1])   # add the last card in hand to the table stack
            self.remove_card()                 # remove the card from the hand

    def cards_left(self):   # return True if cards left to play, else False
        if self.hand == [] and self.table == []:
            return False
        return True

    def rank_top_table(self):
        # return the rank of the player's top card on the table
        card_rank = self.table[-1][0:len(self.table[-1])-1]
        return RANKS.index(card_rank)

    def empty_table(self):
        self.table = []



# GAME PLAY
# Use the 3 classes along with some logic to play a game of War!
# https://en.wikipedia.org/wiki/War_(card_game)

print("Welcome to War! Lets begin...")

# our shuffled deck
deck = Deck()
# our player's hands, one get the left part of the shuffled deck, the other the right
deck.split()

player1 = Player("Ryan", deck.left)
player2 = Player("Stina", deck.right)

print("Player1 hand: ", player1.hand)
print("\n")
print("Player2 hand: ", player2.hand)
print("\n")

# Play the first set of cards
player1.play_cards(1)
player2.play_cards(1)

print(player1.table)
print(player2.table)

#print(player1.rank_top_table(), player2.rank_top_table())
'''player1.table = ["AD"]
player2.table = ["AS"]'''

while True: 

    if player1.rank_top_table() == player2.rank_top_table():
        print("WAR!")           # when we go to war, we play 3 cards from each hand
        if player1.cards_left() and player2.cards_left():
            player1.play_cards(3)
            player2.play_cards(3)
        print("Player 1 table:", player1.table, "\nPlayer2 table:", player2.table)
    else:
        if player1.rank_top_table() > player2.rank_top_table():
            print("Player1 gets player 2's cards")
            # Add player2's cards from the table to the hand of player1
            player1.add_card(player1.table)
            player1.add_card(player2.table)
            player1.empty_table()
            player2.empty_table()
            print(player1.hand)
            print(player2.hand)
        else:
            print("Player 2 gets the cards")
            player2.add_card(player1.table)
            player2.add_card(player2.table)
            player1.empty_table()
            player2.empty_table()
            print(player1.hand)
            print(player2.hand)
        if player1.cards_left() and player2.cards_left():
            player1.play_cards(1)
            player2.play_cards(1)
        else:
            break
if player1.cards_left():
    print(player1.name, "won!")
else:
    print(player2.name, "won!")

