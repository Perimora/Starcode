from abc import ABC, abstractmethod

from lib.classes.model.game import BaseGame


class BaseGui(ABC):

    game: BaseGame

    def __init__(self, game: BaseGame):
        self.game = game


class HangmanGui(BaseGui):
    def __init__(self, game: BaseGame):
        super().__init__(game)


class SnakeGui(BaseGui):
    def __init__(self, game: BaseGame):
        super().__init__(game)
