from hand import Hand
from deck import Deck
from chips import Chips

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
    
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        x = input('Hit or Stand? Enter h or s ')
        
        if x[0].lower() == 'h':
            hit(deck,hand)
            
        elif x[0].lower() == 's':
            print("Player Stands, Dealer's Turn")
            playing = False
            
        else:
            print("Sorry, wrong input, Please enter h or s only!")
            continue
        
        break
    

def show_some(player,dealer):
    
   # Show only ONE of the dealer's cards
   print("\n Dealer's Hand: ")
   print("First card hidden!")
   print(dealer.cards[1])
   
   # Show all (2 cards) of the player's hand/cards 
   print("\n Player's hand: ")
   for card in player.cards:
       print(card)
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

def player_busts(player,dealer,chips):
    print("BUST PLAYER!")
    chips.lose_bet

def player_wins(player,dealer,chips):
    print('PLAYER WINS!')
    chips.win_bet

def dealer_busts(player,dealer,chips):
    print('PLAYER WIN! DEALER BUSTED!')
    chips.win_bet
    
def dealer_wins(player,dealer,chips):
    print('DEALER WINS!')
    chips.lose_bet
    
def push():
    print('Dealer and player tie! PUSH')
    
while True:
    # Print an opening statement

    print("WELCOME TO BLACKJACK")
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
        
    # Set up the Player's chips
    player_chips = Chips()
    
    # Prompt the Player for their bet
    take_bet(player_chips)

    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)

    playing = True
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)
 
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
    
        # Show all cards
        show_all(player_hand,dealer_hand)
    
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)
        
    
    # Inform Player of their chips total 
    print('\n Player total chips are at: {}'.format(player_chips.total))
    # Ask to play again
    while True:
        new_game = input("Would you like to play another hand? (y/n): ")
        if new_game.lower() == 'y':
            playing = True
            break
        elif new_game.lower() == 'n':
            print("Thank you for playing!")
            break
        else:
            print("Sorry, wrong input. Please enter 'y' to play another hand or 'n' to quit.")
        