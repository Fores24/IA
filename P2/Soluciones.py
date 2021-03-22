import math
from reversi import Reversi
from heuristic import *
from game import TwoPlayerGameState
from tournament import StudentHeuristic


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
    print("hola")
    corners = [[1, 1], [1, 8], [8, 1], [8, 8]]
    minDist = 10
    game = state.game
    moves = game.generate_successors(state)
    print(moves)
    for move in moves:
      for corner in corners:
        distX = abs(corner[0] - move.x)
        distY = abs(corner[1] - move.y)
        dist = math.sqrt(distX * distX + distY * distY)
        if dist < minDist:
          minDist = dist

    return minDist



