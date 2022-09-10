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
class Agent:
    def __init__(self, stateHistory):
        self.stateHistory = None

    def updateStateHistory(self):
        pass

    def chooseAction(self):
        pass

    def learn(self):
        pass
