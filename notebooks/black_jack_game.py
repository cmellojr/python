"""
A classic Blackjack game implemented with modern Python (2026 best practices).
This module provides a command-line interface to play against a computer dealer.
"""

import random
from enum import Enum, IntEnum
from dataclasses import dataclass


class Suit(Enum):
    """Enumeration for card suits."""
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    SPADES = "Spades"
    CLUBS = "Clubs"


class Rank(IntEnum):
    """Enumeration for card ranks with associated values."""
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 10
    QUEEN = 10
    KING = 10
    ACE = 11

    def __str__(self) -> str:
        return self.name.capitalize()


@dataclass(frozen=True, slots=True)
class Card:
    """Represents a single playing card."""
    suit: Suit
    rank: Rank

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit.value}"


class Deck:
    """Represents a deck of 52 playing cards."""
    def __init__(self) -> None:
        self.cards: list[Card] = [
            Card(suit, rank) for suit in Suit for rank in Rank
        ]

    def shuffle(self) -> None:
        """Shuffles the deck in place."""
        random.shuffle(self.cards)

    def deal(self) -> Card:
        """Deals a single card from the deck."""
        if not self.cards:
            raise ValueError("All cards have been dealt.")
        return self.cards.pop()

    def __str__(self) -> str:
        return f"The deck has {len(self.cards)} cards"


class Hand:
    """Represents a player's or dealer's hand in the game."""
    def __init__(self) -> None:
        self.cards: list[Card] = []
        self.value: int = 0
        self.aces: int = 0

    def add_card(self, card: Card) -> None:
        """Adds a card to the hand and adjusts value."""
        self.cards.append(card)
        self.value += card.rank.value
        if card.rank == Rank.ACE:
            self.aces += 1
        self.adjust_for_aces()

    def adjust_for_aces(self) -> None:
        """Adjusts the value of the hand if it exceeds 21 and contains aces."""
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def __str__(self) -> str:
        return ", ".join(str(card) for card in self.cards)


class Chips:
    """Manages a player's betting chips."""
    def __init__(self, total: int = 100) -> None:
        self.total: int = total
        self.bet: int = 0

    def win_bet(self) -> None:
        """Adds the bet amount to total chips."""
        self.total += self.bet

    def lose_bet(self) -> None:
        """Subtracts the bet amount from total chips."""
        self.total -= self.bet


def take_bet(chips: Chips) -> None:
    """Prompts the user to place a bet."""
    while True:
        try:
            prompt = f"How many chips would you like to bet? (Balance: {chips.total}): "
            chips.bet = int(input(prompt))
        except ValueError:
            print("Sorry, please provide an integer")
        else:
            if chips.bet > chips.total:
                print(f"Sorry, you do not have enough chips! You have {chips.total}")
            elif chips.bet <= 0:
                print("Bet must be a positive integer.")
            else:
                break


def hit(deck: Deck, hand: Hand) -> None:
    """Deals a card from the deck to the hand and adjusts for aces."""
    hand.add_card(deck.deal())


def hit_or_stand(deck: Deck, hand: Hand) -> bool:
    """
    Prompts the player to hit or stand.
    Returns False if the player stands, True if they hit.
    """
    while True:
        choice = input("Hit or Stand? Enter h or s: ").lower()

        if choice.startswith('h'):
            hit(deck, hand)
            return True

        if choice.startswith('s'):
            print("Player stands. Dealer's turn.")
            return False

        print("Sorry, please try again.")


def show_some(player: Hand, dealer: Hand) -> None:
    """Shows all player cards and all but the first dealer card."""
    # Show only ONE of the dealer's cards
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print(f" {dealer.cards[1]}")

    # Show all (2 cards) of the player's hand/cards
    print("\nPlayer's Hand:", player)
    print(f"Player's Value: {player.value}")


def show_all(player: Hand, dealer: Hand) -> None:
    """Shows all cards for both player and dealer."""
    # show all dealer's cards
    print("\nDealer's Hand:", dealer)
    # calculate and display value
    print(f"Dealer's Value: {dealer.value}")

    # show all the player's cards
    print("\nPlayer's Hand:", player)
    print(f"Player's Value: {player.value}")


def player_busts(chips: Chips) -> None:
    """Handles scenario where player busts."""
    print("\n--- BUST PLAYER! ---")
    chips.lose_bet()


def player_wins(chips: Chips) -> None:
    """Handles scenario where player wins."""
    print("\n--- PLAYER WINS! ---")
    chips.win_bet()


def dealer_busts(chips: Chips) -> None:
    """Handles scenario where dealer busts."""
    print("\n--- PLAYER WINS! DEALER BUSTED! ---")
    chips.win_bet()


def dealer_wins(chips: Chips) -> None:
    """Handles scenario where dealer wins."""
    print("\n--- DEALER WINS! ---")
    chips.lose_bet()


def push() -> None:
    """Handles a tie scenario."""
    print("\n--- Dealer and Player tie! PUSH ---")


def play_blackjack() -> None:
    """Main game loop for Blackjack."""
    player_chips = Chips()  # Set up the Player's chips

    while True:
        # Print an opening statement
        print("\nWELCOME TO BLACKJACK!")

        # Create & shuffle the deck, deal two cards to each player
        deck = Deck()
        deck.shuffle()

        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        # Prompt the Player for their bet
        take_bet(player_chips)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        playing = True
        while playing:
            # Prompt for Player to Hit or Stand
            if not hit_or_stand(deck, player_hand):
                playing = False
            else:
                show_some(player_hand, dealer_hand)

            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player_hand.value > 21:
                player_busts(player_chips)
                break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                hit(deck, dealer_hand)

            # Show all cards
            show_all(player_hand, dealer_hand)

            # Run different winning scenarios
            if dealer_hand.value > 21:
                dealer_busts(player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_chips)
            else:
                push()

        # Inform Player of their chips total
        print(f"\nPlayer total chips are at: {player_chips.total}")

        if player_chips.total <= 0:
            print("You're out of chips! Game Over.")
            break

        # Ask to play again
        new_game = input("Would you like to play another hand? y/n: ").lower()
        if not (new_game and new_game.startswith('y')):
            print("Thank you for playing!")
            break


if __name__ == "__main__":
    play_blackjack()
