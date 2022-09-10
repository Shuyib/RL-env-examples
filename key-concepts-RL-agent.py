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
    def __init__(self, stateHistory):
        self.stateHistory = None

    def updateStateHistory(self):
        pass

    def chooseAction(self):
        pass

    def learn(self):
        pass


# 6*6 maze, Update moves, check if game over, get the state, get rewards, print maze
# robot position 2
class Environment:
    def __init__(self, state):
        self.state = None

    def createMaze(self, noofrows=6, noofcolumns=6):
        maze = np.zeros(shape=(noofrows, noofcolumns))
        global maze

    def printMaze(self):
        return maze

    def updateMove(self, rowindice, columnindice, maxmoves=[0]):
        position = np.put(maze, [rowindice, columnindice], 2)
        maxmoves[0] += 1
        global maxmoves
        global rowindice, columnindice
        return position

    def gameOver(self):
        if maxmoves >= 10:
            print("Game Over")
        else:
            print("Still have")
        return maxmoves

    def getReward(self):  # can't think of a way to update
        if position != 1 | maxmoves < 10:
            continue
        else:
            StopIteration()

    def getState(self):
        current_state = []
        return current_state.append(rowindice, columnindice)

    def getState(self):
        return self.state
