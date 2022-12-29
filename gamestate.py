import logging


class GameState:

    # locals
    game_points = 121
    player_score = 0
    comp_score = 0
    hand_count = 0

    def __init__(self) -> None:
        logger = logging.getLogger('root')
        logger.debug(f"Init Game State")
        pass

    def __str__(self) -> str:
        return f"Score(P): {self.player_score} Score(C): {self.comp_score}"
        pass

    def newgame(self, options):
        self.game_points = options.game_points


class Options:

    def __init__(self, game_points) -> None:
        self.game_points = game_points
        pass
