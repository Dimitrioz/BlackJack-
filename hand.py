class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
        
    def add_card(self,card):
        if type(card) == type([]):
            # List of multiple Card objects
            self.cards.extend(card)
        else:
            # Single Card object
            self.cards.append(card)
    
    def adjust_for_ace(self):
        pass