from abc import ABC, abstractmethod

from lib.classes.model.game import BaseGame, HangmanGame, SnakeGame
from lib.classes.model.game_type import GameType
from lib.classes.view.gui import SnakeGui, HangmanGui


class Factory(ABC):

    @staticmethod
    @abstractmethod
    def build(g_type: GameType):
        pass


class GameFactory(Factory):

    @staticmethod
    def build(g_type: GameType):
        if g_type == GameType.HANGMAN:
            return HangmanGame(g_type)
        elif g_type == GameType.SNAKE:
            return SnakeGame(g_type)
        else:
            raise ValueError(f'Unknown game type: {g_type}')


class GuiFactory(Factory):

    @staticmethod
    def build(g: BaseGame):
        if isinstance(g, HangmanGame):
            return HangmanGui(g)
        elif isinstance(g, SnakeGame):
            return SnakeGui(g)
        else:
            raise ValueError(f'Unknown game type: {g}')
