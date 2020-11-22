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
#iterating through suits and ranks tuples
    	for suit in suits:
    		for rank in ranks:
#creating instance of each card using Card class
#and then appending each instance to deck list
    			self.deck.append(Card(suit, rank))

#function below prints current deck composition
#meaning the cards currently in deck

    def __str__(self):
    	deck_comp = ""
    	for card in self.deck:
    		deck_comp = deck_comp + "\n" + card.__str__()
    	return "The deck has:" + deck_comp

#shuffle() method, using random module and shuffle method,
#shuffles cards in the deck, before dealing    
    def shuffle(self):
    	random.shuffle(self.deck)

#deal() method deals card, using pop() method
#which picks an item in the deck and deletes from the list
    def deal(self):
    	single_card = self.deck.pop()
    	return single_card

#creating class Hand to hold dealt cards. It's basically player's hand
class Hand:
	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0

#add_card() method adds a card into player's hand and calculates
#current value on hand. If it's Ace, self.aces value increments
	def add_card(self, card):
		self.cards.append(card)
		self.value = self.value + values[card.rank]
		if card.rank == "Ace":
			self.aces += 1
#if the value is more than 21, below method will adjust
#Ace's value from 11 to 1
	def adjust_for_ace(self):
		while self.value > 21 and self.aces:
			self.value = self.value - 10
			self.aces -= 1

class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0


    def win_bet(self):                           #method will increment total number of chips
        self.total = self.total + self.bet       #if player wins the bet


    def lose_bet(self):                          #method below will decrement total number of chips
        self.total = self.total - self.bet       #if player loses the bet


def take_bet(chips):
    
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed", chips.total)
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing #to control an upcoming while loop
    while True:
        x = input("Would you like to hit or stand? Enter 'h' or 's' ")
        if x[0].lower() == "h":
            hit(deck, hand) #hit() function defined above
        elif x[0].lower() == "s":
            print("Player stands. Dealer is playing")
            playing = False
        else:
            print("Sorry, please try again")
            continue
        break


def show_some(player, dealer):
	print("\nDealer's Hand: ")
	print("<card hidden>")
	print(dealer.cards[1])
	print("\nPlayer's hand:", *player.cards, sep = "\n")

def show_all(player, dealer):
	print("\nDealer's Hand: ", *dealer.cards, sep = "\n")
	print("Dealer's Hand = ", dealer.value)
	print("\nPlayer's Hand: ", *player.cards, sep = "\n")
	print("Player's Hand = ", player.value)


def player_busts(player, dealer, chips):
	print("Bust! Player lost")
	chips.lose_bet()

def player_wins(player, dealer, chips):
	print("Player wins!")
	chips.win_bet()

def dealer_busts(player, dealer, chips):
	print("Dealer busts!")
	chips.win_bet()

def dealer_wins(player, dealer, chips):
	print("Dealer wins!")
	chips.lose_bet()

def push(player, dealer):
	print("Dealer and Player tie. It's a push.")




while True:
	# Print an opening statement
	print("Welcome To BlackJack!")
	# Create and shuffle the deck. Deal two cards to each player
	deck = Deck()
	deck.shuffle()

	# Create a player and a dealer. Deal two cards to each of them
	player_hand = Hand()
	player_hand.add_card(deck.deal())
	player_hand.add_card(deck.deal())

	dealer_hand = Hand()
	dealer_hand.add_card(deck.deal())
	dealer_hand.add_card(deck.deal())

	# Player's chips setup
	player_chips = Chips()     # Remember, default value is 100
	# Prompt the player for their bet
	take_bet(player_chips)
	# Show cards (but keep one dealer's card hidden)
	show_some(player_hand, dealer_hand)

	while playing:  # recall this variable from our hit_or_stand() function
	    # Prompt for Player to hit or stand
	    hit_or_stand(deck, player_hand)
	    # Show cards (but keep one dealer's card hidden)
	    show_some(player_hand, dealer_hand)
	    # If player's hand exceeds 21, run player_busts() and break out of loop
	    if player_hand.value > 21:
	        player_busts(player_hand, dealer_hand, player_chips)
	        break
	# If Player hasn't busted, play Dealer's hand until Dealer reaches 17
	if player_hand.value < 21:
	    while dealer_hand.value >= 17:
	        hit(deck, dealer_hand)
	    # Show All cards
	    show_all(player_hand, dealer_hand)
	    # Run different winning scenarios
	    if dealer_hand.value > 21:
	    	dealer_busts(player_hand, dealer_hand, player_chips)
	    elif player_hand.value > dealer_hand.value:
	        player_wins(player_hand, dealer_hand, player_chips)
	    elif player_hand.value < dealer_hand.value:
	        dealer_wins(player_hand, dealer_hand, player_chips)
	    else:
	        push(player_hand, dealer_hand)
	# Inform player about their chips total
	print("\nPlayer's winnings stand at",player_chips.total)
	# Ask to play again
	new_game = input("Would you like to play again? Enter 'y' or 'n' ")
	if new_game[0].lower() == "y":
	    playing = True
	    continue
	else:
	    print("Thanks for playing!")
	    break























