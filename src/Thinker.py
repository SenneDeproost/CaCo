from PolicyTree import *
from PolicyMatrix import *
import random
from debug import *

class Thinker:
    def __init__(self, name):
        self.name = name
        self.tree = PolicyTree(name)
        self.policy = PolicyMatrix(name, 99, 21)
        self.state = 0
        self.epsilon = 0.1
        self.states = [0]
        self.actions = [0]
        self.counter = -1

    def think(self, i):
        state = self.state
        best_action = self.policy.best(state)
        random_action = self.policy.random()
        if random.random() < self.epsilon:
            action = best_action
            log("Chosing best action: " + str(action), self.name)
        else:
            action = random_action
            log("Chosing random action: " + str(action), self.name)
        self.actions.append(action)
        self.state += 1  # State represent the number of sentences thought by the thinker
        return action

    def feedback(self, reward):
        self.policy.update(self.state - 1, self.actions[-1], self.state, reward)


    def newest(self):
        return self.actions[-1]







