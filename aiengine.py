import deck
import logging


# Functions designed to determine what the computer player should do
def chooseCribCards(hand: [deck.Card], crib: bool) -> [deck.Card]:

    # Look at the 6 cards in the hand and assign values
    cards_throw = []
    cards_throw.append(hand[0], hand[1])

    # Update later with real logic
    return cards_throw


# Function to take a hand of cards, also the stack of cards played, then determine what to play
def choosePegCard(hand: [deck.Card], stack: [deck.Card]) -> deck.Card:
    return hand[0]


# Count a cribbage hand - given hand and a cut card, calculate total and explanation
def countHand(hand: [deck.Card], cut_card: deck.Card) -> (int, str):
    total = 0
    explanation = "Nada"
    # Look for 15s
    logging.info("Count 15s")
    for card in hand:
        logging.info(f"Counting 15: {card}")
    # Look for pairs

    # Look for runs

    # Look for flush

    # Look for nobs

    # Return value
    return (total, explanation)
