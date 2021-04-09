# Haithem's version of the war card game

"""
The deck is divided evenly, with each player receving 26 cards, dealt one at a time,face down.
Anyone may deal first. Each player places his stack of cards face down, in front of him/her.
The Play:
Each player turns up a card at the same time and the player with the higher card takes both cards and puts them,
face down, on the bottom of his stack.
If the cards are the sam rank, it is WAR. Each player turns up three cards face down and one card face up.
The player with the higher cards takes both piles(six cards). If the turned-up cards are again the same rank, 
each player places another card face down and turns another card face up. 
The player with the hihger card takes all 10 cards and so on...
"""
from random import shuffle
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A '.split()
class Deck:
    """
    This is the Deck class. This object will create a deck of cards to intiate play.
    You can then use this Deck list of cards to split in half and give to the players. 
    It will use SUITE and RANKS to create the deck. It should also have a method for splitting/cutting the deck in half,
    and shuffle the deck.
    """
    def __init__(self):
        print("Creating new ordered deck")
        self.allcards = [(s,r) for s in SUITE for r in RANKS]
    
    def shuffle(self):
        print("Shuffling Deck")
        shuffle(self.allcards)
        
    def split_in_half(self):
        return(self.allcards[:26],self.allcards[26:])
class Hand:
    """
    Each player has a Hand, and can add or remove cards from that hand. 
    There should be an add and remove card method here.
    """
    def __init__(self, cards):
        self.cards = cards
        
    def __str__(self):
        return "Contains {} cards".format(len(self.cards))
    
    def add(self, added_cards):
        self.cards.extend(added_cards)
        
    def remove_card(self):
        return self.cards.pop()
        
        
        
        
class Player:
    """
    The Player class takes in a name and an instance of a Hand class objekt. 
    The player can then play cards and check if they still have cards.
    """
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
        
    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed: {}".format(self.name, drawn_card))
        print("\n")
        return drawn_card
    
    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return war_cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop(0))
            return war_cards
    def still_has_cards(self):
        #Return True if player still has cards
        return len(self.hand.cards) != 0
#GAME PLAY
print("Welcome to War, lets begin...")
#Create New Deck and split in half
d = Deck()
d.shuffle()
half1,half2 = d.split_in_half()
#Create both players
comp = Player("computer", Hand(half1))
name = input("What is your name player?")
user = Player(name,Hand(half2))
total_rounds = 0
war_count = 0
while user.still_has_cards() and comp.still_has_cards():
    total_rounds += 1
    
    print("It is time for a new round!")
    print("Here are the current standings: ")
    print(user.name + "count: " + str(len(user.hand.cards)))
    print(comp.name + "count: " + str(len(comp.hand.cards)))
    print("Both player play a card!")
    print("\n")
    
    #Cards on table represented by list
    table_cards = []
    
    #Play cards
    c_card = comp.play_card()
    p_card = user.play_card()
    
    #Add to table_cards
    table_cards.append(c_card)
    table_cards.append(p_card)
    
    #Check for war!
    
    if c_card[1] == p_card[1]:
        war_count += 1
        print("We have a match, time for war!")
        print("Each player removes 3 cards 'face down' andthen one card face up")
        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())
        
        #Play cards
        c_card = comp.play_card()
        p_card = user.play_card()
        
        #Add to table_cards
        table_cards.append(c_card)
        table_cards.append(p_card)
        
        #Check to see who had higher rank
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            print(user.name +" has the higher card, adding to hand")
            user.hand.add(table_cards)  
        else:
            print(comp.name+ " has the higher card, adding to hand")
    else:
        #Check to see who had higher rank
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            print(user.name+ " has the higher card, adding to hand")
            user.hand.add(table_cards)
        else:
            print(comp.name + " has the higher card, adding to hand")
            comp.hand.add(table_cards)
print("Great game! it lasted:"+ str(total_rounds) + " rounds!")
print("A war occured " +str(war_count)+ " times")