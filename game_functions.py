def take_bet(chips):
    while True:
        
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except:
            print("Sorry, please provide an integer")
        else:
            if chips.bet > chips.total:
                print("Sorry, you do not have enough chips! You have: {}".format(chips.total))
            else:
                break

def hit(deck,hand):
    
    pass

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    pass

def show_some(player,dealer):
    
    pass
    
def show_all(player,dealer):
    
    pass

def player_busts():
    pass

def player_wins():
    pass

def dealer_busts():
    pass
    
def dealer_wins():
    pass
    
def push():
    pass

while True:
    # Print an opening statement

    
    # Create & shuffle the deck, deal two cards to each player

    
        
    # Set up the Player's chips
    
    
    # Prompt the Player for their bet

    
    # Show cards (but keep one dealer card hidden)

    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        
        
        # Show cards (but keep one dealer card hidden)
 
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        

            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    
    
        # Show all cards
    
        # Run different winning scenarios
        
    
    # Inform Player of their chips total 
    
    # Ask to play again

        break