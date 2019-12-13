from PolicyTree import *
from PolicyMatrix import *
import random
from debug import *

class Thinker:
    def __init__(self, name):
        self.name = name
        self.tree = PolicyTree(name)
        self.policy = PolicyMatrix(name, 21, 21)
        self.state = None
        self.epsilon = 0.9
        self.states = [0]
        self.actions = [0]

    def think(self, i):
        state = i['state']
        best_action = self.policy.best(state)
        random_action = self.policy.random()
        if random.random() < self.epsilon:
            action = best_action
            log("Chosing best action: " + str(action), self.name)
        else:
            action = random_action
            log("Chosing random action: " + str(action), self.name)
        self.actions.append(action)
        return action

    def feedback(self, reward, action, new_state):
        self.policy.update(self.state, action, new_state, reward)







