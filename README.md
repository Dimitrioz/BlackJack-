# BlackJack-
Python game
The game will have a computer dealer and a human player.
We start with a normal deck of cards.
Player will place bet.
Player starts with 2 cards face up.
Dealer starts with 1 card face up and 1 card face down.
Player goes first.
Goal is to get closer to a total value of 21 than dealer.
Hit (Receive another card)
Stays (Stop Receiving Cards)

After player turn:
   if player is under 21, dealer the hits until either beat the player 
   or the dealer busts.
   
   elif player keeps hitting goes over 21, they bust and lost the bet
   the game is then over and dealer collects the money.

   else player is under 21, dealer then hits until they either beat the player
   or the dealer busts
   the player gets duble the money


special rules:
  face cards (Jack,Queen,King) count as a value of 10.
  Aces can count as either 1 or 11
  wichever value is preferable to the player.

  ## Game Play
To play a hand of Blackjack the following steps must be followed:
1. Create a deck of 52 cards
2. Shuffle the deck
3. Ask the Player for their bet
4. Make sure that the Player's bet does not exceed their available chips
5. Deal two cards to the Dealer and two cards to the Player
6. Show only one of the Dealer's cards, the other remains hidden
7. Show both of the Player's cards
8. Ask the Player if they wish to Hit, and take another card
9. If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
10. If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
11. Determine the winner and adjust the Player's chips accordingly
12. Ask the Player if they'd like to play again
