#Importing 'random' module below to be able to 
#shuffle card deck
import random 

#Creating a list, tuple, dictionary to store
#card suits, ranks, and values

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": (10, 1)}

#Declaring boolean value to control while loop and 
#flow of the game

playing = True

#Creating Card class with rank and suit parameters
class Card:
	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit
		
#creating a method in case we need to print card rank and suit
	def __str__(self):
		return f"{rank} of {suit}"

#creating card deck class

class Deck
    def __init__(self):
#creating an empty list to append each of 52 card objects    	
    	self.deck = []
#iterating through suits list and ranks tuple
    	for suit in suits:
    		for rank in ranks:
#creating instance of each card using Card class
#and then appending each instance to deck list
    			self.deck.append(Card(rank, suit))

    def __str__(self):
    	deck_comp = ""
    	for card in self.deck:
    		deck_comp = deck_comp "\n" + card.__str__()
    		return "The deck has:" + deck_comp
    
    def shuffle(self):
    	random.shuffle(self, deck)

    def deal(self):
    	single_card = self.deck.pop()
    	return single_card
















