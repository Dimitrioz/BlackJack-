from cards import Card,suits,ranks
import random

class Deck:
    
    def __init__(self):
        # This only happens once upon creation of a new Deck
        self.deck = [] # start with an empty list
        for suit in suits:
            for rank in ranks:
                # This assumes the Card class has already been defined!
                self.deck.append(Card(suit, rank))
                
    def __str__(self):
       # Create a string representing the deck
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()
        return 'The deck has:' + deck_comp 
    
    def shuffle(self):
        # This doesn't return anything
        random.shuffle(self.deck)
        
    def deal(self):
        # We remove one card from the list of all_cards
        single_card = self.deck.pop()
        return single_card
    