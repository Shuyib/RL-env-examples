"""
A module to handle an RL agent that finds what's the exit of the maze using numpy and the standard python library.
"""

import numpy as np

# define the action space: Dictionary tuple
# U means Up, D means down, L means left and R means right
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
        self.randomFactor = randomFactor  # spends 20% of time exploring/ 80 % exploiting (hyperparameter)
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
        self.stateHistory.append((state, reward))

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
            nextMove = np.random.choice(allowedMoves)  # controls the next move
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

        # run at the end of the maze (reduce the random factor)
        self.randomFactor -= 10e-5


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
        self.steps = 0  # setting the state to be zero
        self.constructAllowedStates()

    def printMaze(self):
        """for debugging purposes. Let's you see the current state of the maze.
        R for the robot, X for the wall and empty space ''.
        """
        print("*" * 1000)
        for row in self.maze:
            for col in row:
                if col == 0:
                    print("", end="\t")
                elif col == 1:
                    print("X", end="\t")
                elif col == 2:
                    print("R", end="\t")
            print("\n")
        print("*" * 1000)

    def isAllowedtoMove(self, state, action):
        """Determining if a move is allowed.

        Parameters
        ----------
        state :
            
        action :
            

        Returns
        -------

        
        """
        y, x = state
        y += actionSpace[action][0]
        x += actionSpace[action][1]

        # defining the rules of the maze to prevent issues
        if y < 0 or x < 0 or y > 5 or x > 5:
            return False
        if self.maze[y, x] == 0 or self.maze[y, x] == 2:
            return True
        else:
            return False

    def constructAllowedStates(self):
        """Defining if every state is allowed"""
        allowedStates = {}
        for y, row in enumerate(self.maze):
            for x, col in enumerate(row):
                if self.maze([y, x]) != 1:
                    allowedStates[(y, x)] = []
                    for action in actionSpace:
                        if self.isAllowedtoMove([(y, x)], action):
                            allowedStates([y, x]).append(action)
        self.allowedStates = allowedStates

    def updateMaze(self, action):
        """Updates the maze give the action taken.

        Parameters
        ----------
        action : what the robot did.
            

        Returns
        -------

        
        """
        y, x = self.robotPosition
        self.maze[y, x] = 0
        y += actionSpace[action][0]
        x += actionSpace[action][1]
        self.robotPosition = (y, x)
        self.maze[y, x] = 2
        self.steps += 1

    def isGameOver(self):
        """Allows the game to end at some point."""
        if self.robotPosition == (5, 5):
            return True
        else:
            return False

    def getStateAndReward(self):
        """Figuring out the current state of the system."""
        reward = self.giveReward()
        return self.robotPosition, reward

    def giveReward(self):
        """Issues reward to the agent based on state of the system.

        Parameters
        ----------
        state :
            

        Returns
        -------

        
        """
        if self.robotPosition == (5, 5):
            return 0
        else:
            return -1
