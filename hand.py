class Hand:
    def __init__(self):
        self.cards = []  # List to store card objects
        self.value = 0   # Value of the hand
        self.aces = 0    # Number of aces in the hand

    def add_card(self, card):
        # Add a card to the hand and adjust the value
        self.cards.append(card)
        self.value += card.values[card.rank]
        
        # Track aces
        if card.rank == 'Ace':
            self.aces += 1
        self.adjust_for_ace()

    def adjust_for_ace(self):
        # If total value is over 21 and there is an ace, adjust the ace's value from 11 to 1
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
