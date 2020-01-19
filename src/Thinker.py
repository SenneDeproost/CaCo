from PolicyTree import *
from PolicyMatrix import *
import random
from debug import *
import json

class Thinker:
    def __init__(self, name):
        self.name = name
        self.tree = PolicyTree(name)
        self.state = 0
        self.epsilon = 0.1
        self.states = [0]
        self.counter = -1
        self.chosen_actions = []
        self.policy = PolicyMatrix(name, 99, 42)

    def think(self, i):
        state = self.state
        best_action = self.policy.best(state)
        random_action = self.policy.random()
        if random.random() < self.epsilon:
            action_indx = best_action
            log("Chosing best action: " + str(action_indx), self.name)
        else:
            action_indx = random_action
            log("Chosing random action: " + str(action_indx), self.name)
        #action = self.actions[action_indx]
        self.chosen_actions.append(action_indx)
        self.state += 1  # State represent the number of sentences thought by the thinker
        return action_indx

    def feedback(self, reward):
        self.policy.update(self.state - 1, self.chosen_actions[-1], self.state, reward)

    def last_feedback(self, old_state, new_state, action, reward):
        self.policy.update(old_state, action, new_state, reward)

    def newest(self):
        return self.chosen_actions[-1]







