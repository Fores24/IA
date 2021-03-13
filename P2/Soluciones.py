import time
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
    # let's use an auxiliary function
    aux = self.dummy(123)
    return aux

  def dummy(self, n: int) -> int:
    return n + 1

class Solution2(StudentHeuristic):
  def get_name(self) -> str:
    return "solution2"
  def evaluation_function(self, state: TwoPlayerGameState) -> float:
    print("sleeping")
    time.sleep(3)
    print("awake")
    return 2

class Solution3(StudentHeuristic):
  def get_name(self) -> str:
    return "solucion3"

  def evaluation_function(self, state: TwoPlayerGameState) -> float:
    print(TwoPlayerGameState.generate_successor())
    return 1


class CornerPlayer:
  def __init__(self, color):
    self.color = color

  def play(self, board):
    return self.getNearestCorner(board.valid_moves(self.color))

  def getNearestCorner(self, moves):
    import math
    corners = [[1,1],[1,8], [8,1], [8,8]]
    minDist = 8
    retMove = None
    for move in moves:
      for corner in corners:
        distX = abs(corner[0] - move.x)
        distY = abs(corner[1] - move.y)
        dist  = math.sqrt(distX*distX + distY*distY)
        if dist < minDist:
          minDist = dist
          retMove = move

    return retMove