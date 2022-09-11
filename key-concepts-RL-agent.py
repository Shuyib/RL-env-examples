# Create an agent which can get through a maze
# It should have appropriate functions for learning,choosing actions,and updating its memory.

# Create a class named agent add a function called learn, memory and actions
# hasty first attempt
# class Agent:
#     def __init__(self, name, action, stateHistory):
#         self.name = name
#         self.action = action
#         self.stateHistory = {action}

# formatted with black
import numpy as np


class Agent:
    """ This is entity that learns and takes actions to maximize the reward. 
    Will track its state, make actions and finally make a decision."""

    def __init__(self, stateHistory):
        self.stateHistory = None

    def updateStateHistory(self):
        """ changes the current state of the agent."""
        pass

    def chooseAction(self):
        """controls what action the agent will take."""
        pass

    def learn(self):
        """ decision agent takes"""
        pass


# 6*6 maze, Update moves, check if game over, get the state, get rewards, print maze
# robot position 2
# class Environment:
#     def __init__(self, state):
#         self.state = None

#     def createMaze(self, noofrows=6, noofcolumns=6):
#         maze = np.zeros(shape=(noofrows, noofcolumns))
#         global maze

#     def printMaze(self):
#         return maze

#     def updateMove(self, rowindice, columnindice, maxmoves=[0]):
#         position = np.put(maze, [rowindice, columnindice], 1)
#         maxmoves[0] += 1
#         global maxmoves
#         global rowindice, columnindice
#         return position

#     def gameOver(self):
#         if maxmoves >= 10:
#             print("Game Over")
#         else:
#             print("Still have")
#         return maxmoves

#     def getReward(self):  # can't think of a way to update
#         if position != 1 | maxmoves < 10:
#             continue
#         else:
#             StopIteration()

#     def getState(self):
#         current_state = []
#         return current_state.append(rowindice, columnindice)

#     def getState(self):
#         return self.state

# some similar components to the one above issue contextuatizing the maze and getting ahead of myself.
class Maze:
    """An RL environment for a robot in a 6 row and 6 column matrix trying to find its way to the objective.
    obstacles are labelled 1, robot position identity is 2 at the position 0,0 in a tuple."""

    def __init__(object):
        self.maze = np.zeros(shape=(6, 6))
        self.maze[5, :5] = 1  # np.put(self.maze, [5, :5], 1) wall
        self.maze[:4, 5] = 1  # np.put(self.maze, [:4, 5], 1) wall
        self.maze[2, 2:] = 1  # np.put(self.maze, [2, 2:], 1) wall
        self.maze[3, 2] = 1  # np.put(self.maze, [3, 2], 1) wall
        self.maze[0, 0] = 2  # np.put(self.maze, [0,0], 2) robot
        self.robotPosition = (0, 0)  # actual position at start

    def printMaze(self):
        """ for debugging purposes. Let's you see the current state of the maze """
        pass

    def isAllowedtoMove(self, state, action):
        """Determining if a move is allowed.

        Parameters
        ----------
        state :
            
        action :
            

        Returns
        -------

        """
        pass

    def updateMaze(self, action):
        """Updates the maze give the action taken.

        Parameters
        ----------
        action :
            

        Returns
        -------

        """
        pass

    def isGameOver(self):
        """ Allows the game to end at some point."""
        pass

    def getState(self):
        """Figuring out the current state of the system."""
        pass

    def giveReward(self, state):
        """Issues reward to the agent based on state of the system.

        Parameters
        ----------
        state :
            

        Returns
        -------

        """
        pass
