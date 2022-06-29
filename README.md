# Hero To Zero

## Project 4: 21 Black Jack

Black Jack (also known as 21) is a very popular casino game played with one or multiple decks of cards.
The aim of the game is to try and beat the dealer by getting a hand value as close to 21 as possible without going over 21.
The rules vary but for this particular implementation they are as follows.

### Rules

#### Scoring
A card's value is equal to its pip value unless the cards are face cards or aces.
A face card's value is equal to 10.
It is for the player to decide an ace's value.  It can be equal to 1 or 11.

#### Betting
Before a betting round begins, the player must make a bet in order to take part.

#### The Deal
Once a player has placed their bet, the deck is shuffled and one card is dealt to the player and the dealer.
The player takes this card face up whilst the dealer takes the card face down.
Another card is then dealt to the player and the dealer.
Both of whom take the dealt card face up.

#### The Play 
If upon receiving his hand the player has an ace card and a face or 10 card.  
That player has "Black Jack" and wins the round recovering his bet amount plus an equal stake from the dealer.
If the player does not have a "Black Jack" the player must decide whether to _Stick_ or _Hit_.
To _Stick_ is not to receive any further cards whereas to _Hit_ is to receive extra cards one by one until the player either chooses to _Stick_ or their hand value goes above 21.
If a player's hand value goes above 21 then that player is considered "Bust" and loses the betting round thereby forfeiting their bet amount to the dealer.
0n the other hand, if a player's hand value after sticking is under 21 then the dealer proceeds to reveal their face-down card.
If upon revealing their hand, the dealer has a score of 16 or less, the dealer must take an additional card. 
If the ensuing dealer's hand value after receiving their additional card goes over 21 then the dealer is bust and the player wins the round recovering his bet plus an equal stake from the dealer.
Otherwise, if the dealer's hand value remains under 21 then the player and dealer compare their totals.
If the player's total is closest to 21 then the player wins the round and collects their bet amount plus an equal stake from the dealer. 
If the dealer's total is closest to 21 then the dealer wins the round and takes the bet from the player.
If both the player and dealer have an equal score then it is considered a draw and the player is returned his bet amount.
The game concludes once X number of betting rounds are played, at which point the player can continue or end the game.
