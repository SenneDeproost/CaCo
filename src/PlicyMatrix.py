import numpy as np
import random

class TransMatrix:
    def __init__(self):
        self.transitions = np.ones([20, 20])
        self.transitions[:,0] = 0



class PolicyMatrix:
    def __init__(self, n_states, n_actions):
        self.n_action = n_actions
        self.n_states = n_states
        self.policy = np.zeroes([n_states, n_actions])

    def best(self, state_indx):
        return np.argmax(self.policy[state_indx])

    def random(self):
        return random.randint(0, self.n_actions)

    def update(self, old_state, action, new_state, reward):
        self.policy[old_state][action] += 0.9*(reward + 0.9*np.max(self.policy[new_state, :]) - self.policy[old_state, action])
