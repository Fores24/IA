"""Strategies for two player games.

   Authors:
        Fabiano Baroni <fabiano.baroni@uam.es>,
        Alejandro Bellogin <alejandro.bellogin@uam.es>
        Alberto Suárez <alberto.suarez@uam.es>
"""

from __future__ import annotations  # For Python 3.7

from abc import ABC, abstractmethod
from typing import List

import numpy as np

from game import TwoPlayerGame, TwoPlayerGameState
from heuristic import Heuristic


class Strategy(ABC):
    """Abstract base class for player's strategy."""

    def __init__(self, verbose: int = 0) -> None:
        """Initialize common attributes for all derived classes."""
        self.verbose = verbose

    @abstractmethod
    def next_move(
        self,
        state: TwoPlayerGameState,
        gui: bool = False,
    ) -> TwoPlayerGameState:
        """Compute next move."""

    def generate_successors(
        self,
        state: TwoPlayerGameState,
    ) -> List[TwoPlayerGameState]:
        """Generate state successors."""
        assert isinstance(state.game, TwoPlayerGame)
        successors = state.game.generate_successors(state)
        assert successors  # Error if list is empty
        return successors


class RandomStrategy(Strategy):
    """Strategy in which moves are selected uniformly at random."""

    def next_move(
        self,
        state: TwoPlayerGameState,
        gui: bool = False,
    ) -> TwoPlayerGameState:
        """Compute next move."""
        successors = self.generate_successors(state)
        return np.random.choice(successors)


class ManualStrategy(Strategy):
    """Strategy in which the player inputs a move."""

    def next_move(
        self,
        state: TwoPlayerGameState,
        gui: bool = False,
    ) -> TwoPlayerGameState:
        """Compute next move."""
        successors = self.generate_successors(state)

        assert isinstance(state.game, TwoPlayerGame)
        if gui:
            index_successor = state.game.graphical_input(state, successors)
        else:
            index_successor = state.game.manual_input(successors)

        next_state = successors[index_successor]

        if self.verbose > 0:
            print('My move is: {:s}'.format(str(next_state.move_code)))

        return next_state


class MinimaxStrategy(Strategy):
    """Minimax strategy."""

    def __init__(
        self,
        heuristic: Heuristic,
        max_depth_minimax: int,
        verbose: int = 0,
    ) -> None:
        """Initialize depth of the search & heuristic."""
        super().__init__(verbose)
        self.heuristic = heuristic
        self.max_depth_minimax = max_depth_minimax

    def next_move(
        self,
        state: TwoPlayerGameState,
        gui: bool = False,
    ) -> TwoPlayerGameState:
        """Compute next state in the game."""

        successors = self.generate_successors(state)

        minimax_value = -np.inf

        for successor in successors:
            if self.verbose > 1:
                print('{}: {}'.format(state.board, minimax_value))

            successor_minimax_value = self._min_value(
                successor,
                self.max_depth_minimax,
            )
            if (successor_minimax_value > minimax_value):
                minimax_value = successor_minimax_value
                next_state = successor

        if self.verbose > 0:
            if self.verbose > 1:
                print('\nGame state before move:\n')
                print(state.board)
                print()
            print('Minimax value = {:.2g}'.format(minimax_value))

        return next_state

    def _min_value(
        self,
        state: TwoPlayerGameState,
        depth: int,
    ) -> float:
        """Min step of the minimax algorithm."""
        if state.end_of_game or depth == 0:
            minimax_value = self.heuristic.evaluate(state)

        else:
            minimax_value = np.inf

            successors = self.generate_successors(state)
            for successor in successors:
                if self.verbose > 1:
                    print('{}: {}'.format(state.board, minimax_value))

                successor_minimax_value = self._max_value(
                    successor, depth - 1,
                )
                if (successor_minimax_value < minimax_value):
                    minimax_value = successor_minimax_value

        if self.verbose > 1:
            print('{}: {}'.format(state.board, minimax_value))

        return minimax_value

    def _max_value(
        self,
        state: TwoPlayerGameState,
        depth: int,
    ) -> float:
        """Max step of the minimax algorithm."""
        if state.end_of_game or depth == 0:
            minimax_value = self.heuristic.evaluate(state)

        else:
            minimax_value = -np.inf

            successors = self.generate_successors(state)
            for successor in successors:
                if self.verbose > 1:
                    print('{}: {}'.format(state.board, minimax_value))

                successor_minimax_value = self._min_value(
                    successor, depth - 1,
                )
                if (successor_minimax_value > minimax_value):
                    minimax_value = successor_minimax_value

        if self.verbose > 1:
            print('{}: {}'.format(state.board, minimax_value))

        return minimax_value


class MinimaxAlphaBetaStrategy(Strategy):
    """Minimax alpha-beta strategy."""

    def __init__(
        self,
        heuristic: Heuristic,
        max_depth_minimax: int,
        verbose: int = 0,
    ) -> None:
        super().__init__(verbose)
        self.heuristic = heuristic
        self.max_depth_minimax = max_depth_minimax

    def next_move(
        self,
        state: TwoPlayerGameState,
        gui: bool = False,
    ) -> TwoPlayerGameState:
        """Compute next state in the game."""

        # NOTE <YOUR CODE HERE>
        #inicializamos las variables a infitito y menos infinito
        alfa = -np.inf
        beta = np.inf
        minmax = -np.inf
        next_state = None
        sucesores = self.generate_successors(state)

        for sucesor in sucesores:
            minimax_value_successor, alfa_s, beta_s = self._min_value(sucesor, self.max_depth_minimax, alfa, beta)
            if minimax_value_successor > minmax:
                minmax = minimax_value_successor
                next_state = sucesor

            if beta_s > alfa:
                alfa = beta_s

            if alfa >= beta:
                break

        return next_state

    def min_value(
        self,
        state: TwoPlayerGameState,
        depht: int,
        alfa = int,
        beta = int,
    ) -> (float, float, float):
        if state.end_of_game or depht ==0:
            minmax = self.heuristic.evaluate(state)
            alfa = minmax
            beta = minmax
        else :
            minmax = np.inf
            sucesores = self.generate_successors(state)
            for sucesor in sucesores:
                minmax_sucesores, alfa_s, beta_s = self._max_value(sucesor, self.max_depth_minimax, alfa, beta)

                if alfa_s < beta:
                    beta = alfa_s

                if minmax_sucesores <= minmax:
                    minmax = minmax_sucesores

                if alfa >= beta:
                    break
        return minmax, alfa, beta

    def max_value(
            self,
            state: TwoPlayerGameState,
            depht: int,
            alfa=int,
            beta=int,
    ) -> (float, float, float):
        if state.end_of_game or depht == 0:
            minmax = self.heuristic.evaluate(state)
            alfa = minmax
            beta = minmax
        else:
            minmax = np.inf
            sucesores = self.generate_successors(state)
            for sucesor in sucesores:
                minmax_sucesores, alfa_s, beta_s = self._min_value(sucesor, self.max_depth_minimax, alfa, beta)

                if alfa_s > beta:
                    beta = alfa_s

                if minmax_sucesores > minmax:
                    minmax = minmax_sucesores

                if alfa >= beta:
                    break
        return minmax, alfa, beta




