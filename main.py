# Import random module.
import random
import os

# Dictionary representing 4 possible suits of cards in a deck.
# Where the key is the suit name and the value is the UNICODE symbol.
SUITS = {
    "club": '\u2663',
    "diamond": '\u2666',
    "heart": '\u2665',
    "spade": '\u2660',
}
# Dictionary representing the 13 possible card ranks and values in a deck.
# Where the key is the card rank and the value is the numerical value of the card.
VALUES = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 11,
}


# Classes.
class Card:
    """
    Card class that represents a standard playing card.
    """
    def __init__(self, rank, suit):
        """
        Upon instantiation, a card object is assigned with a display attribute and a value attribute.
        Where display equals a concatenation of the card's rank and suit.
        Where value equals the cards corresponding numerical value.
        """
        self.rank = rank
        self.display = rank + suit
        self.value = VALUES[rank]

    def __str__(self):
        """
        Method that returns the display attribute to the print statement.
        """
        return f"{self.display}"


class Deck:
    """
    Deck class that represents a standard 52 card deck.
    """
    def __init__(self):
        """
        Upon instantiation, a deck object is assigned with an all_cards attribute.
        Where all_cards consists of 52 card objects.
        The 52 card objects are the result of a nested for loop of VALUES and SUITS.
        """
        self.all_cards = []
        for rank in VALUES:
            for suit in SUITS:
                card = Card(rank, SUITS[suit])
                self.all_cards.append(card)

    def shuffle_cards(self):
        """
        Method that shuffles the card objects inside all_cards attribute.
        """
        random.shuffle(self.all_cards)

    def deal_card(self):
        """
        Method that removes a single card object from the deck by popping a card from the all_cards attribute.
        Returns the popped card.
        """
        return self.all_cards.pop()


# Player class.
class Player:
    """
    Player class that represents a player in the game.
    """
    def __init__(self, player_name, player_bankroll):
        """
        Upon instantiation a player object is assigned a name, a bankroll, and a hand attribute.
        Where name equals a user defined parameter.
        Where bankroll equals a user defined value.
        Where hand equals and empty list.
        """
        self.name = player_name
        self.bankroll = player_bankroll
        self.hand = []

    def receive_card(self, card):
        """
        Method that enables a player object to add cards to their hand.
        It does so by appending to the player's hand attribute.
        Returns player's hand attribute with appended card.
        Where card is the card dealt from the deck by deck.deal_card()
        """
        return self.hand.append(card)

    def display_full_hand(self):
        """
        Method that displays a visual representation of the card objects in a player's hand.
        It does so by appending the display attribute of a card object to full_hand.
        Returns full_hand.
        """
        full_hand = []
        for card in self.hand:
            full_hand.append(card.display)
        return full_hand

    def display_partial_hand(self):
        """
        Method that displays a partial visual representation of the card objects in a player's hand.
        It does so by appending the display attribute of the card object's in 'self.hand' from index 1 onwards.
        Returns partial_hand.
        """
        partial_hand = []
        for index in range(1, len(self.hand)):
            partial_hand.append(self.hand[index].display)
        return partial_hand

    def hand_value(self):
        """
        Method that calculates the value of a player's hand.
        It does so by adding up the value attributes of the card objects in a player's hand.
        If player's hand value is over 21, and they have aces in their hand.
        The player's hand value is reduced by 10 for every ace in their hand.
        Returns total hand value.
        """
        aces = 0
        hand_value = 0
        for card in self.hand:
            hand_value += card.value
        if hand_value > 21:
            for card in self.hand:
                if card.rank == "A":
                    aces += 1
            while aces > 0:
                hand_value -= 10
                aces -= 1
            return hand_value
        else:
            return hand_value

    def clear_hand(self):
        """
        Method that clears a player object's hand attribute and removes the cards from the game.
        """
        self.hand = []

    def wager(self, bet):
        """
        Method that lets a player object make a bet.
        It does so by removing the bet from the player's bankroll attribute.
        Returns bet.
        Where bet equals bet_value set in game.
        """
        self.bankroll -= bet
        return bet

    def collect(self, winnings):
        """
        Method that collect a player's winnings after winning a round and updates their bankroll attribute.
        Where winnings equals winning_pot in game.
        """
        self.bankroll += winnings

    def __str__(self):
        """
        Method that returns a custom print string for the print function.
        """
        return f"{self.name} has {len(self.hand)} cards in hand.\n" \
               f"{self.name} has a bankroll of {self.bankroll} available."


# Functions
def hit_or_stick():
    """
    Function that asks for an input of 'Hit' or 'Stick'.
    If input is not what requested loops and asks again for a valid input.
    Where 'Hit' equals True.
    Where 'Stick' equals False.
    """
    while True:
        play = input("Would you like a 'Hit' or do you want to 'Stick': ").lower()
        if play == 'hit':
            return True
        elif play == 'stick':
            return False
        else:
            print("You did not type 'Hit' or 'Stick'. Try again.")


def yes_or_no():
    """
    Function that asks for an input of 'Yes' or 'No'.
    If input is not what requested loops and asks again for a valid input.
    Where 'Yes' equals True.
    Where 'No' equals False.
    """
    while True:
        answer = input("Type 'Yes' or 'No': ").lower()
        if answer == 'yes':
            return True
        elif answer == 'no':
            return False
        else:
            print("You did not type 'Yes' or 'No'. Try again.")


def clear_screen():
    """
    Function that clears windows the Python terminal.
    """
    os.system('cls')


# Game introduction.
print("\nWelcome to Black Jack\n")
# Instantiate a deck and shuffle it.
deck = Deck()
deck.shuffle_cards()
# Set betting round counter.
betting_rounds = 0
# Set game length.
game_length = 5
print(f"\nEach game consists of {game_length} rounds of betting.")
# Set betting amount
bet_value = 100
print(f"The buy in to play is: ${bet_value}\n")
# Ask player for their name.
name = input("What is your name: ")
bankroll = int(input("How large a bankroll do you want: $"))
# Instantiate a dealer and player using player 'name' and 'bankroll'.
dealer = Player("Dealer", bankroll)
p1 = Player(name, bankroll)
# Print question asking player if they want to play.
print("\nWould you like to play?")
# Create game replay flag.
replay = True
# Start replay while loop.
while replay:
    # Whenever betting_rounds are evenly divisible by game_length.
    if betting_rounds % game_length == 0:
        # Set replay flag using play_again() function.
        replay = yes_or_no()
        # If play_again() returns False.
        if not replay:
            # Break from loop and game over.
            break
    # Add round to betting_rounds counter.
    betting_rounds += 1
    # Provide round starting feedback:
    print(f"\nRound {betting_rounds}\n")
    print(f"{p1.name}'s current bankroll is ${p1.bankroll}.")
    print(f"{dealer.name}'s current bankroll is ${dealer.bankroll}.")
    # Create winning_pot.
    winning_pot = 0
    # Have dealer and player place a bet.
    winning_pot += p1.wager(bet_value)
    winning_pot += dealer.wager(bet_value)
    print(f"\nBets placed.\nThe game pot is: ${winning_pot}\n")
    # Deal two cards to dealer and player respectively.
    for _ in range(2):
        p1.receive_card(deck.deal_card())
        dealer.receive_card((deck.deal_card()))
    # Display partial dealer and full player hands.
    print(f"\n{dealer.name} has: {dealer.display_partial_hand()}")
    print(f"{p1.name} has: {p1.display_full_hand()}\n")
    # Create game_over flag.
    game_over = False
    # If player has Black Jack.
    if p1.hand_value() == 21:
        # Give player winner and game over feedback.
        print(f"\n{p1.name} has Black Jack.")
        print(f"{dealer.name} has: {dealer.display_full_hand()}.")
        print(f"{p1.name} wins.\n")
        # Have player collect winning_pot.
        p1.collect(winning_pot)
        # Set game over flag to True and end game.
        game_over = True
    # If player does not have Black Jack start game_over while loop to control game flow.
    while not game_over:
        # If player wants to 'Hit'.
        if hit_or_stick():
            # Deal extra card to player.
            p1.receive_card(deck.deal_card())
            # If player hand value over 21.
            if p1.hand_value() > 21:
                # Give dealer winner and game over feedback.
                print(f"\n{p1.name} has: {p1.display_full_hand()}")
                print(f"{p1.name} is BUST.")
                print(f"{dealer.name} WINS.\n")
                # Dealer collects winning_pot.
                dealer.collect(winning_pot)
                # Break loop.
                game_over = True
            # Else player hand value less than 21.
            else:
                # Give hand feedback.
                print(f"\n{p1.name} has: {p1.display_full_hand()}")
                print(f"{dealer.name} has: {dealer.display_partial_hand()}\n")
                # Continue to top of loop.
                continue
        # Else player wants to 'Stick'.
        else:
            # Give hand feedback.
            print(f"\n{p1.name} has: {p1.display_full_hand()}")
            print(f"{dealer.name} has: {dealer.display_full_hand()}\n")
            # While dealer hand value less than 17.
            while dealer.hand_value() < 17:
                # Give value less than 17 feedback.
                print(f"{dealer.name} has a hand value of less than 17.  Extra card issued.")
                # Deal extra card to dealer.
                dealer.receive_card(deck.deal_card())
                # Show updated hand.
                print(f"{dealer.name} has: {dealer.display_full_hand()}.\n")
            # If dealer hand value is greater than 21.
            if dealer.hand_value() > 21:
                # Give game over feedback
                print(f"\n{dealer.name} is BUST.")
                print(f"{p1.name} WINS.\n")
                # Have player collect winning_pot.
                p1.collect(winning_pot)
                # Break loop.
                game_over = True
            # Else if dealer hand value and player hand value are equal.
            elif dealer.hand_value() == p1.hand_value():
                # Give hand feedback.
                print(f"\n{p1.name} has: {p1.display_full_hand()}")
                print(f"{dealer.name} has: {dealer.display_full_hand()}\n")
                # Print game is a draw.
                print("Game is a DRAW.")
                # Have player collect their stake only.
                p1.collect(int(winning_pot/2))
                # Have dealer collect their stake only.
                dealer.collect(int(winning_pot/2))
                # Break loop.
                game_over = True
            # Else if dealer hand value further away from 21 than player.
            elif abs(21 - dealer.hand_value()) > abs(21 - p1.hand_value()):
                # Give hand feedback.
                print(f"\n{p1.name} has: {p1.display_full_hand()}")
                print(f"{dealer.name} has: {dealer.display_full_hand()}\n")
                # Print dealer scores less than Player 1
                print(f"{dealer.name} has lowest score.")
                print(f"{p1.name} WINS.")
                # Player 1 collects winning_pot.
                p1.collect(winning_pot)
                # Break loop.
                break
            # Else if dealer is closer to 21 than player.
            elif abs(21 - dealer.hand_value()) < abs(21 - p1.hand_value()):
                # Give hand feedback.
                print(f"\n{p1.name} has: {p1.display_full_hand()}")
                print(f"{dealer.name} has: {dealer.display_full_hand()}\n")
                # Print Player 1 scores less than dealer.
                print(f"{p1.name} has lowest score.")
                print(f"{dealer.name} WINS.")
                # Player 1 collects winning_pot.
                dealer.collect(winning_pot)
                # Break loop.
                break
    # Clear dealer and player hands.
    p1.clear_hand()
    dealer.clear_hand()
    # If less than 1/4 of the deck is remaining in the game.
    if len(deck.all_cards) < 14:
        # Give feedback.
        print("Less than 1/4 deck remaining adding new deck.")
        # Instantiate and shuffle extra_deck.
        extra_deck = Deck()
        extra_deck.shuffle_cards()
        # Add extra_deck to remaining cards from deck.
        for card_object in extra_deck.all_cards:
            deck.all_cards.append(card_object)
    # Print new total cards remaining for the game.
    print(f"\nCards remaining in game: {len(deck.all_cards)}")
    # If player does not have enough bankroll to place minimum bet.
    if p1.bankroll < bet_value:
        # Give feedback.
        print(f"\n{p1.name} does not have enough bankroll to place another bet.")
        # End game.
        break
    # If dealer does not have enough bankroll to place minimum bet.
    if dealer.bankroll < bet_value:
        # Give feedback.
        print(f"\n{p1.name} does not have enough bankroll to place another bet.")
        # End game.
        break
    # If betting rounds can be evenly divisible by game_length.
    if betting_rounds % game_length == 0:
        # Print replay feedback.
        print("\nWant to play another round?")
    else:
        # Clear screen for new round.
        input("\nPress enter to continue...")
        clear_screen()
# End of Game
print("\nGame Over.")
print(f"You leave with a bankroll of ${p1.bankroll}")
