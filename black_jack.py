#Importing 'random' module below to be able to 
#shuffle card deck
import random 

#Creating a tuples, dictionary to store
#card suits, ranks, and values

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}

#Declaring boolean value to control while loop and 
#flow of the game

playing = True

#Creating Card class with rank and suit parameters
class Card:
	def __init__(self, suit, rank):
		self.rank = rank
		self.suit = suit
		
#creating a method in case we need to print card rank and suit
	def __str__(self):
		return f"{self.rank} of {self.suit}"

#creating card deck class

class Deck:
    def __init__(self):
#creating an empty list to append each of 52 card objects    	
    	self.deck = []
#iterating through suits list and ranks tuple
    	for suit in suits:
    		for rank in ranks:
#creating instance of each card using Card class
#and then appending each instance to deck list
    			self.deck.append(Card(suit, rank))

    def __str__(self):
    	deck_comp = ""
    	for card in self.deck:
    		deck_comp = deck_comp + "\n" + card.__str__()
    	return "The deck has:" + deck_comp
    
    def shuffle(self):
    	random.shuffle(self.deck)

    def deal(self):
    	single_card = self.deck.pop()
    	return single_card


class Hand:
	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0

	def add_card(self, card):
		self.cards.append(card)
		self.value = self.value + values[card.rank]
		if card.rank == "Ace":
			self.aces += 1

	def adjust_for_ace():
		while self.value > 21 and self.aces:
			self.value = self.value - 10
			self.aces -= 1

class Chips:
	def __init__(self):
		self.total = 100
		self.bet = 0

	def win_bet(self):
		self.total = self.total + self.bet

	def lose_bet(self):
		self.total = self.total - self.bet


def take_bet(chips):
    while True:
    	try:
		    chips.bet = int(input("How many chips would you like to bet? "))

		except: 
			print("Your bet must be a number!S")
			
		else:
			if chips.bet > chips.total:
				print("Sorry, your bet can't exceed", chips.total)
			else:
			    print("Thanks. Bet accepted.")
			    break


my_deck = Deck()
my_deck.shuffle()
player_1 = Hand()
player_1.add_card(my_deck.deal())
player_1.add_card(my_deck.deal())
print(player_1.value)
for card in player_1.cards:
	print(card)














