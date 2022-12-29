import pygame, sys
import logging
import deck, gamestate, aiengine

from pygame.locals import QUIT

# Setup Code

# def setup_custom_logger(name):

#     formatter = logging.Formatter(
#         fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')

#     handler = logging.StreamHandler()
#     handler.setFormatter(formatter)

#     logger = logging.getLogger(name)
#     logger.setLevel(logging.DEBUG)
#     logger.addHandler(handler)
#     return logger

# logger = setup_custom_logger('root')
logger = logging.getLogger("root")
logger.setLevel(logging.DEBUG)
logger.debug("Main Code")

pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Hello World!')

# Some globals
deck = deck.Deck()
cut_card = None
player_hand = []
comp_hand = []

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_n:
            # Start New Game
            g = gamestate.GameState()
            logger.info(f"Game state: {g}")
            #deck = deck.Deck()
            deck.shuffle()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            # deal cards

            for i in range(6):
                player_hand.append(deck.topCard())
                comp_hand.append(deck.topCard())
            #Set cut Card
            cut_card = deck.topCard()
            logger.info(f"Dealt Player: {player_hand}")
            logger.info(f"Dealt Comp: {comp_hand}")
            logger.info(f"Cut Card: {cut_card}")
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            # count cards
            p_tot = aiengine.countHand(player_hand, cut_card)
            c_tot = aiengine.countHand(comp_hand, cut_card)
            logger.info(f"Player Score: {p_tot}, Comp Score: {c_tot}")
        DISPLAYSURF.fill((255, 255, 255))
        pygame.display.update()
