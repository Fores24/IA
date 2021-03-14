import math
from reversi import Reversi
import reversi
from heuristic import *
from game import (
    TwoPlayerGameState,
)
from tournament import (
    StudentHeuristic,
)


class Solution1(StudentHeuristic):
  def get_name(self) -> str:
    return "solution1"
  def evaluation_function(self, state: TwoPlayerGameState) -> float:
    return simple_evaluation_function(state)


class Solution2(StudentHeuristic):
  def get_name(self) -> str:
    return "solution2"
  def evaluation_function(self, state: TwoPlayerGameState) -> float:
    return complex_evaluation_function(state)

class Solution3(StudentHeuristic):
  def get_name(self) -> str:
    return "solucion3"

  def evaluation_function(self, state: TwoPlayerGameState) -> float:
    if not isinstance(state.game, Reversi):
      return 0
    if isinstance(state.board, dict):
      board = state.board
    else:
      board = reversi.from_array_to_dictionary_board(state.board)
    if state.end_of_game:
      scores = state.scores
      result = scores[0] - scores[1]
    else:
      game = state.game
      corners = [board.get((1, 1)), board.get((1, game.height)), board.get((game.width, 1)),
                 board.get((game.width, game.height))]
      x_squares = [board.get((2, 2)), board.get((2, game.height - 1)), board.get((game.width - 1, 2)),
                   board.get((game.width - 1, game.height - 1))]
      corner_diff = 0
      for i in range(4):
        if corners[i] == game.player1.label:
          corner_diff += 4
        elif corners[i] == game.player2.label:
          corner_diff -= 4
        else:
          if x_squares[i] == game.player1.label:
            corner_diff -= 1
          elif x_squares[i] == game.player2.label:
            corner_diff += 1

      mobility = len(game.generate_successors(state))

      result = 4 * corner_diff - mobility

    if state.is_player_max(state.player1):
      return result
    elif state.is_player_max(state.player2):
      return - result
    else:
      raise ValueError('Player MAX not defined')





