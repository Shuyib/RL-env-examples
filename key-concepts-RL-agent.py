"""
A module to handle an RL agent that finds what's the exit of the maze using numpy and the standard python library.
"""

import numpy as np

# define the action space: Dictionary tuple
actionSpace = {"U": (-1.0), "D": (1.0), "L": (0, -1), "R": (0, 1)}


class Agent(object):
    """This is entity that learns and takes actions to maximize the reward.
    Will track its state, make actions and finally make a decision.

    Parameters
    ----------

    Returns
    -------

    
    """

    def __init__(self, states, alpha=0.15, randomFactor=0.2):
        self.stateHistory = [((0, 0), 0)]  # will be list of states and rewards
        self.alpha = alpha
        self.randomFactor = (
            randomFactor  # spends 20% of time exploring/ 80 % exploiting
        )
        self.G = (
            {}
        )  # keys will be the states and values estimates of the future rewards.
        self.initReward(states)

    def initReward(self, states):
        """Initialize the state of rewards: Goes through each state in a dict.
        Uses a uniform/binomial distribution

        Parameters
        ----------
        states : what has changed that is, the robot position. It ranges
            
        between -0.1 and -1.0. :
            

        Returns
        -------

        
        """
        for state in states:
            self.G[state] = np.random.uniform(low=-1.0, high=-0.1)

    def updateStateHistory(self):
        """changes the current state of the agent."""
        pass

    def chooseAction(self, state, allowedMoves):
        """controls what action the agent will take.

        Parameters
        ----------
        state :
            
        allowedMoves :
            

        Returns
        -------

        """
        maxG = -10e15
        nextMove = None
        randomN = np.random.random()
        if randomN < self.randomFactor:
            nextMove = np.ranom.choice(allowedMoves)
        else:
            for action in allowedMoves:
                newState = tuple([sum(x) for x in zip(state, actionSpace[action])])
                if self.G[newState] >= maxG:
                    nextMove = action
                    maxG = self.G[newState]
        return nextMove

    def learn(self):
        """decision agent takes"""
        target = 0  # we only learn when we beat the maze

        # iterate over reversed state and reward pairs starting from that state
        # increment target with the reward
        for prev, reward in reversed(self.stateHistory):
            self.G[prev] = self.G[prev] + self.alpha * (target - self.G[prev])
            target += reward

        # zero out agents memory for the next episode
        self.stateHistory = []


class Maze:
    """An RL environment for a robot in a 6 row and 6 column matrix trying to find its way to the objective.
    obstacles are labelled 1, robot position identity is 2 at the position 0,0 in a tuple.

    Parameters
    ----------

    Returns
    -------

    
    """

    def __init__(object):
        self.maze = np.zeros(shape=(6, 6))
        self.maze[5, :5] = 1  # np.put(self.maze, [5, :5], 1) wall
        self.maze[:4, 5] = 1  # np.put(self.maze, [:4, 5], 1) wall
        self.maze[2, 2:] = 1  # np.put(self.maze, [2, 2:], 1) wall
        self.maze[3, 2] = 1  # np.put(self.maze, [3, 2], 1) wall
        self.maze[0, 0] = 2  # np.put(self.maze, [0,0], 2) robot
        self.robotPosition = (0, 0)  # actual position at start

    def printMaze(self):
        """for debugging purposes. Let's you see the current state of the maze"""
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
        """Allows the game to end at some point."""
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
