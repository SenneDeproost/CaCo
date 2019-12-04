from PolicyTree import *
import random

class Thinker:
    def __init__(self, name):
        self.name = name
        self.tree = PolicyTree(name)
        self.state = None
        self.epsilon = 0.8

    def think(self, input):
        best_action = self.tree.best_action(input, self.state)
        random_action = self.tree.(input, self.state)
        action = None
        if random.random() < self.epsilon:
            action = best_action
        else:
            action = random_action
        return action

    def feedback(self, score, input, action, new_state):

        self.state = new_state




