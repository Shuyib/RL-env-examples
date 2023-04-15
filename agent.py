import numpy as np


class Agent(object):
    """This is entity that learns and takes actions to maximize the reward.
    Will track its state, make actions and finally make a decision.

    Parameters
    ----------
    object :

    Returns
    -------

    
    """

    def __init__(self, states, alpha=0.15, randomFactor=0.2):
        self.stateHistory = [((0, 0), 0)]  # will be list of states and rewards
        self.alpha = alpha # learning rate (hyperparameter)
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
