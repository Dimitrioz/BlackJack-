from cards import Card,suits,ranks
import random

class Deck:
    
    def __innit__(self):
        # This only happens once upon creation of a new Deck
        self.deck = [] # start with an empty list
        for suit in suits:
            for rank in ranks:
                # This assumes the Card class has already been defined!
                self.deck.append(Card(suit, rank))
                
    def __str__(self):
        return self.deck 
    
    def shuffle(self):
        # This doesn't return anything
        random.shuffle(self.deck)
        
    def deal(self):
        # We remove one card from the list of all_cards
        return self.deck.pop()
    
