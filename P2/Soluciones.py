import math
import reversi
from reversi import Reversi
from heuristic import *
from game import TwoPlayerGameState
from tournament import StudentHeuristic

def sa(str )-> float:
  return 'b'



class Solution1(StudentHeuristic):
  def get_name(self) -> str:
    return "solution1"
  def evaluation_function(self, state: TwoPlayerGameState) -> float:
    return simple_evaluation_function(state)


class Solution2(StudentHeuristic):
  def get_name(self) -> str:
    return "solution2"
  def evaluation_function(self, state: TwoPlayerGameState) -> float:
    tabler = reversi.from_array_to_dictionary_board(state.board)

    return complex_evaluation_function(state)

class Solution3(StudentHeuristic):
  def get_name(self) -> str:
    return "solucion3"

  def evaluation_function(self, state: TwoPlayerGameState) -> float:
    if not isinstance(state.game, Reversi):
      return 0
    print("hola")
    corners = [[1, 1], [1, 8], [8, 1], [8, 8]]

    print(corners[0][0])

    incio = [[4,4],[4,5],[5,4],[5,5]]
    game = state.game
    moves = game.generate_successors(state)
    print (moves.pop().move_code)

    return len(moves)





