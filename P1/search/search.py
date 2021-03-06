# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""
from typing import List, Any

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    acciones = []
    aux = []
    Nodos = util.Stack()
    Nodos.push((problem.getStartState(),[],[]))
    while not Nodos.isEmpty():
        nodo, accion , visitado = Nodos.pop()
        if problem.isGoalState(nodo):
            return acciones
        for hijo , direcciones , pasos in problem.getSuccessors(nodo):
            if not hijo in visitado:
                Nodos.push((hijo,accion+[direcciones],visitado+[nodo]))
                acciones = accion+[direcciones]
    return  None

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    aux = []
    Nodos = util.Queue()
    Nodos.push((problem.getStartState(), [], []))
    while not Nodos.isEmpty():
        nodo, accion, coste = Nodos.pop()
        if not nodo in aux:
            aux.append(nodo)
            if problem.isGoalState(nodo):
                return accion
            for hijo, direcciones, pasos in problem.getSuccessors(nodo):
                Nodos.push((hijo, accion + [direcciones], coste + [pasos]))

    return None


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    aux = []
    Nodos = util.PriorityQueue()
    Nodos.push((problem.getStartState(), [], 0),0)
    while not Nodos.isEmpty():
        nodo, accion, coste = Nodos.pop()
        if not nodo in aux:
            aux.append(nodo)
            if problem.isGoalState(nodo):
                return accion
            for hijo, direcciones, pasos in problem.getSuccessors(nodo):
                    Nodos.push((hijo, accion + [direcciones],  coste + pasos),coste+pasos)

    return None

def nullHeuristic(state, problem=None):
     """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
     return None

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    Abiertos = util.PriorityQueue()
    Cerrados = []
    """Nodo Origen en lista abiertos"""
    Abiertos.push((problem.getStartState(), [], 0), heuristic(problem.getStartState(), problem))
    while not Abiertos.isEmpty():
        nodo, accion, coste = Abiertos.pop()
        if not nodo in Cerrados:
            Cerrados.append(nodo)
            if problem.isGoalState(nodo):
                return accion

            for hijo, direcciones, pasos in problem.getSuccessors(nodo):
                g = coste + pasos
                Abiertos.push((hijo, accion + [direcciones], coste + pasos), g + heuristic(hijo, problem))
    return None
"*** YOUR CODE HERE ***"


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

""" Condiciones de Esquina
      - 1 PUNTO en cada esquina (¿como se sabe si la casilla tiene PUNTO?)
      - Heuristica:
          (- Elegir Dirección X: Ver que nodo hijo cuesta menos para priorizar dirección.)
          - Elegir Dirección X = DERECHA por ejemplo:

          - Bucle mientras que nªEsquinas != 4
              - Comprobar si se puede mover en X
                  - Si : Mover en X 
                  - No :
                      - Elegir nueva Dirección Y (perpendicular): Ir abajo (o arriba)
                      - Comproabr si se puede mover en Y
                          - Si : Mover en Y
                          - No:
                              - COmprobar si es Esquina / Existe PUNTO en Casilla (Función??)
                              - Si:

          FUNCION ESQUINA{    
                                  - nºEsquinas ++
                                  - Si n1Esquinas = 1 or 3
                                  - Cambiar Dirección Y
                                      - Volver arriba del bucle

                                  - Si nº Esquinas = 2 
                                  - Cambiar dirección X
                                  - Volver arriba del bucle

                                  - Si nºEsquinas = 4 
                                  - Return (FIN).
                          }

                              - No:
                                  - Bucle Mientras no se pueda mover en X o Y
                                      - Comprobar movernos en dirección Y contraria = !Y
                                          - Si: 
                                              - Mover en !Y
                                              - Comproabr si podemos mover en X   
                                                  - Si:                           
                                                      - Mover en X                
                                                      - Comprobar si ESQUINA      
                                                          - Si:                   
                                                              - FUNCIÓN ESQUINA   

                                                  # Sube al principio del bucle y comprueba y mueve en X, si no puede, mueve en Y, pierde el progreso
                                                  - No: 
                                                      - Mover en !X

                                          - No:
                                              - Comprobar movimiento en Dirección X Contraria = !X
                                                  - Si:
                                                      - Mover en !X
                                                  - No:
                                                      - RETURN ERROR!!!.          #Estas encerrado en un bucle sin fin ni sentido.                     
  """

