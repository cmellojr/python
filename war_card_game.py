import random

# Constants
SUITS = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
RANKS = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
VALUES = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

CARDS_FOR_WAR = 3  # Number of cards to place face down during a war
CARDS_IN_INITIAL_DEAL = 26


class Card:
    """
    Represents a single playing card with a suit, rank, and value.
    """
    def __init__(self, suit, rank):
        """
        Initializes a Card.

        Args:
            suit (str): The suit of the card (e.g., 'Hearts').
            rank (str): The rank of the card (e.g., 'Ace').
        """
        self.suit = suit
        self.rank = rank
        self.value = VALUES[rank]

    def __str__(self):
        """
        Returns a string representation of the card.
        """
        return f"{self.rank} of {self.suit}"


class Deck:
    """
    Represents a deck of 52 playing cards.
    """
    def __init__(self):
        """
        Initializes a full deck of cards.
        """
        self.all_cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        """
        Shuffles the deck of cards in place.
        """
        random.shuffle(self.all_cards)

    def deal_one(self):
        """
        Deals one card from the top of the deck.

        Returns:
            Card: The card dealt from the deck. Returns None if deck is empty.
        """
        if self.all_cards:
            return self.all_cards.pop()
        return None


class Player:
    """
    Represents a player in the card game.
    """
    def __init__(self, name):
        """
        Initializes a Player.

        Args:
            name (str): The name of the player.
        """
        self.name = name
        self.all_cards = []

    def remove_one(self):
        """
        Removes and returns the top card from the player's hand.

        Returns:
            Card: The card removed from the hand. Returns None if hand is empty.
        """
        if self.all_cards:
            return self.all_cards.pop(0)
        return None

    def add_cards(self, new_cards):
        """
        Adds one or more cards to the player's hand.

        Args:
            new_cards (Card or list): A Card object or a list of Card objects.
        """
        if isinstance(new_cards, list):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        """
        Returns a string representation of the player's status.
        """
        return f'Player {self.name} has {len(self.all_cards)} cards.'


def print_game_over(winner_name, loser_name, reason="out of cards"):
    """Prints the game over message."""
    print(f"Player {loser_name} {reason}! Game Over")
    print(f"Player {winner_name} Wins!")


def play_war_game():
    """
    Manages the main game logic for War.
    """
    player_one = Player("One")
    player_two = Player("Two")

    new_deck = Deck()
    new_deck.shuffle()

    for _ in range(CARDS_IN_INITIAL_DEAL):
        player_one.add_cards(new_deck.deal_one())
        player_two.add_cards(new_deck.deal_one())

    round_num = 0

    while True:
        round_num += 1
        print(f"\nRound {round_num}")

        if not player_one.all_cards:
            print_game_over("Two", "One")
            break

        if not player_two.all_cards:
            print_game_over("One", "Two")
            break

        # Each player plays a card
        p1_played_card = player_one.remove_one()
        p2_played_card = player_two.remove_one()

        if not p1_played_card or not p2_played_card:
            # This case should ideally not be reached if checks above are correct
            # but as a safeguard:
            if not p1_played_card and player_two.all_cards: # P1 ran out mid-round draw
                 print_game_over("Two", "One", reason="ran out of cards unexpectedly")
            elif not p2_played_card and player_one.all_cards: # P2 ran out mid-round draw
                 print_game_over("One", "Two", reason="ran out of cards unexpectedly")
            else: # Both ran out simultaneously or other draw error
                 print("Game ends in a draw due to card exhaustion.")
            break


        print(f"Player One plays: {p1_played_card}")
        print(f"Player Two plays: {p2_played_card}")

        player_one_table_cards = [p1_played_card]
        player_two_table_cards = [p2_played_card]

        at_war = True
        while at_war:
            if player_one_table_cards[-1].value > player_two_table_cards[-1].value:
                print("Player One wins the round!")
                player_one.add_cards(player_one_table_cards)
                player_one.add_cards(player_two_table_cards)
                at_war = False
            elif player_one_table_cards[-1].value < player_two_table_cards[-1].value:
                print("Player Two wins the round!")
                player_two.add_cards(player_one_table_cards)
                player_two.add_cards(player_two_table_cards)
                at_war = False
            else:
                print('WAR!')
                # Check if players have enough cards for war
                # Each player needs CARDS_FOR_WAR face-down cards + 1 face-up card
                if len(player_one.all_cards) < CARDS_FOR_WAR + 1:
                    print_game_over("Two", "One", reason="unable to play war")
                    # Give remaining cards to winner
                    player_two.add_cards(player_one.all_cards)
                    player_one.all_cards = [] # Clear P1's hand
                    player_two.add_cards(player_one_table_cards)
                    player_two.add_cards(player_two_table_cards)
                    at_war = False # Ends the war sub-loop
                    return # Ends the game

                if len(player_two.all_cards) < CARDS_FOR_WAR + 1:
                    print_game_over("One", "Two", reason="unable to play war")
                    # Give remaining cards to winner
                    player_one.add_cards(player_two.all_cards)
                    player_two.all_cards = [] # Clear P2's hand
                    player_one.add_cards(player_one_table_cards)
                    player_one.add_cards(player_two_table_cards)
                    at_war = False # Ends the war sub-loop
                    return # Ends the game

                print("Each player places three cards face down and one face up...")
                for _ in range(CARDS_FOR_WAR):
                    p1_war_card = player_one.remove_one()
                    p2_war_card = player_two.remove_one()
                    if p1_war_card: player_one_table_cards.append(p1_war_card)
                    if p2_war_card: player_two_table_cards.append(p2_war_card)

                # Draw the face-up cards for war
                p1_face_up_war_card = player_one.remove_one()
                p2_face_up_war_card = player_two.remove_one()

                if not p1_face_up_war_card: # Player one ran out drawing their war card
                    print_game_over("Two", "One", reason="ran out of cards during war")
                    player_two.add_cards(player_one_table_cards) # P2 gets P1's table cards
                    player_two.add_cards(player_two_table_cards) # P2 gets their own table cards back
                    if p2_face_up_war_card: player_two.add_cards(p2_face_up_war_card) # P2 gets their drawn card
                    at_war = False
                    return

                if not p2_face_up_war_card: # Player two ran out drawing their war card
                    print_game_over("One", "Two", reason="ran out of cards during war")
                    player_one.add_cards(player_one_table_cards) # P1 gets their own table cards back
                    player_one.add_cards(player_two_table_cards) # P1 gets P2's table cards
                    if p1_face_up_war_card: player_one.add_cards(p1_face_up_war_card) # P1 gets their drawn card
                    at_war = False
                    return

                print(f"Player One's war card: {p1_face_up_war_card}")
                print(f"Player Two's war card: {p2_face_up_war_card}")

                player_one_table_cards.append(p1_face_up_war_card)
                player_two_table_cards.append(p2_face_up_war_card)
                # The loop continues to compare the new face-up cards


if __name__ == '__main__':
    play_war_game()
