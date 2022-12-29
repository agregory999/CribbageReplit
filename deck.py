import random
import logging

HEART = 0
CLUB = 1
DIAMOND = 2
SPADE = 3


class Deck:

    def __init__(self) -> None:
        logging.debug(f"init")
        # create 52 cards in a stack
        self.deck = []
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 14):
                self.deck.append(Card(s, v))
                logging.debug(f"added {s} / {v}")

    def shuffle(self) -> None:
        # randomize card order
        for i in range(1000):
            c = self.deck.pop(random.randint(0, 51))
            self.deck.append(c)
        logging.info("Shuffled..")

    def show(self):
        for i, c in enumerate(self.deck):
            logging.info(f"Card {i} = {c}")

    def topCard(self):
        # pick a card and return it
        if self.deck:
            return self.deck.pop()
        return None


class Card:

    def __init__(self, suit, value) -> None:
        self.suit = suit
        self.value = value

    def __str__(self):
        s = f"A {self.value} of {self.suit}"
        #logging.error(s)
        return s

    def getSuit(self):
        logging.debug(f"Suit: {self.suit}")
        return self.suit

    def getValue(self):
        logging.debug(f"Val: {self.value}")
        return self.value
