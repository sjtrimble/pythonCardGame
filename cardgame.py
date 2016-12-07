# basic card game for Coding Dojo Python OOP module
# San Jose, CA
# 2016-12-06

import random # to be used below in the Deck class function

# Creating Card Class
class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def show(self):
        print self.value + " " + self.suit

# Creating Deck Class
class Deck(object):
    def __init__(self):
        self.cards = []
        self.get_cards() # running the get_card method defined below to initiate with a full set of cards as your deck

    def get_cards(self):
        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        values = ['Ace', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        for suit in suits: # iterating through the suits
            for value in values: # iterating through each value
                newcard = Card(value, suit) # creating a newcard variable with the class Card and passing the iterations from the for loop
                self.cards.append(newcard) # adding the newly created card of Card class and adding it to the cards variable within the deck class object/instance

    def show(self):
        for card in self.cards:
            card.show() # calling the Card class' show method (see above in Card class section) - this is okay because the item it's iterating through it of the Card class

    def shuffle(self):
        random.shuffle(self.cards) # using random.shuffle method - import random above needs to be set before using

    def deal(self):
        return self.cards.pop() # returning the removed last value (a card of class Card) of the cards variable

# Creating Player Class
class Player(object):
    def __init__(self, name):
        self.hand = []
        self.name = name

    def draw_cards(self, number, deck): # also need to pass through the deck here so that the player can have cards deal to them from that deck of class Deck
        if number < len(deck.cards):# to ensure that the amount of cards dealt do not exceed how many cards remain in a deck
            for i in range (number): # iterating through the cards in the deck
                dealtcard = deck.deal() # calling the Deck class' deal method and assigning it to a new dealtcard variable to be used in the next step
                self.hand.append(dealtcard) # appending it to the player's hand variable set above

    def show(self):
        for card in self.hand:
            card.show() # calling the Card class' show method (see above in Card class section) - this is okay because the item it's iterating through it of the Card class

        print "Show is running!"

# Sample Order of Process

mydeck = Deck() # create a new deck with Deck class
mydeck.shuffle() # shuffle the deck
player1 = Player('Bob') # create a new player
player1.draw_cards(5, mydeck) # draw 5 card from the mydeck deck created
player1.show() # show the player's hand of cards that has been drawn
