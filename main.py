import pygame, sys
import logging
import deck, gamestate

from pygame.locals import QUIT

# Setup Code


def setup_custom_logger(name):
    formatter = logging.Formatter(
        fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    return logger


logger = setup_custom_logger('root')
logger.debug("Main Code")

pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Hello World!')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_n:
            # Start New Game
            g = gamestate.GameState()
            logger.info(f"Game state: {g}")
            d = deck.Deck()
            d.shuffle()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            # deal card
            c = d.topCard()
            logger.info(f"Card: {c}")
    DISPLAYSURF.fill((255, 255, 255))
    pygame.display.update()
