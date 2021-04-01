import ast
import math
from typing import Union

from reversi import Reversi
import reversi
from heuristic import *
from game import (
    TwoPlayerGameState,
)
from tournament import (
    StudentHeuristic,
)

alpha_to_num = {
  'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8
}

str_num = {
  '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8
}

def letra_a_num(str) -> int:
  for letra in alpha_to_num:
    if letra == str:
      return alpha_to_num[letra]

  return -1

def str_to_num(str) -> int:
  for letra in str_num:
    if letra == str:
      return str_num[letra]

  return -1

"""class Solution1(StudentHeuristic):
  def get_name(self) -> str:
    return "2301_15_sol1"
  def evaluation_function(self, state: TwoPlayerGameState) -> float:

    game = state.game
    moves = game.generate_successors(state)
    return len(moves)
    #devuelve el numero de sucesores (coge el sucesor que de el máximo numero de sucesores)
"""

class Solution2(StudentHeuristic):
  def get_name(self) -> str:
    return "2301_15_sol2"

  def evaluation_function(self, state: TwoPlayerGameState) -> float:
    if not isinstance(state.game, Reversi):
      return 0

    max = 1
    moves = state.generate_successor()
    for move in moves:
      if len(move.generate_successor()) > max:
        max = len(move.generate_successor())

    return max

def not_corner(L) -> bool:
  vecino_esquina = [[1, 2], [2, 1], [1, 7], [2, 8], [7, 1], [8, 2], [7, 8], [8, 7]]

  if (L in vecino_esquina):
    return True

  return False

class Solution3(StudentHeuristic):
  def get_name(self) -> str:
    return "2301_15_sol3"

  def evaluation_function(self, state: TwoPlayerGameState) -> float:
    if not isinstance(state.game, Reversi):
      return 0

    game = state.game
    moves = game.generate_successors(state)

    cuatro = 10
    min_DB = 10
    min_DA = 10
    min_IB = 10
    min_IA = 10

    while moves:
      move = moves.pop().move_code

      if (move):
        y = letra_a_num(move[4])
        x = str_to_num(move[1])

        L = [x, y]

        if (not_corner(L) == True):
          return 20

        if (y == 1 and x == 1) or (y == 8 and x == 8) or (y == 1 and x == 8) or (y == 8 and x == 1):
          return 1

        if y > 4 and x > 4:
          D_B = min(8 - x, 8 - y)
          if min_DB > D_B:
            min_DB = D_B

        if y < 4 and x > 4:
          D_A = min(8 - x, y)
          if min_DA > D_A:
            min_DA = D_A

        if y > 4 and x < 4:
          I_B = min(x, 8 - y)
          if min_IB > I_B:
            min_IB = I_B

        if y < 4 and x < 4:
          I_A = min(x, y)
          if min_IA > I_A:
            min_IA = I_A

        if y == 4 or x == 4:
          cuatro = min(x, y)

    return min(min_DA, min_IA, min_IB, min_DB, cuatro)

class Solution4(StudentHeuristic):
  def get_name(self) -> str:
    return "2301_15_sol4"

  def evaluation_function(self, state: TwoPlayerGameState) -> float:
    if not isinstance(state.game, Reversi):
      return 0

    corners = [[1, 'a'], [1, 'h'], [8, 'a'], [8, 'h']]
    minDist = 10
    game = state.game
    moves = game.generate_successors(state)

    while moves:
      move = moves.pop().move_code

      if(move):
        y = letra_a_num(move[4])
        x = str_to_num(move[1])

        L = [x, y]

        if (not_corner(L) == True):
          return 20

        for corner in corners:
          distX = abs(corner[0] - x)
          distY = abs(letra_a_num(corner[1]) - y)
          dist = math.sqrt(distX * distX + distY * distY)
          if dist < minDist:
            minDist = dist

    return minDist


    """
class Solution8(StudentHeuristic):  
  def get_name(self) -> str:
    return "solution8"
  def evaluation_function(self, state: TwoPlayerGameState) -> float:
    return simple_evaluation_function(state)
    """
