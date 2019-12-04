import numpy as np

class TransMatrix:
    def __init__(self):
        self.transitions = np.ones([20, 20])
        self.transitions[:,0] = 0



class PolicyMatrix:
    def __init__(self, n_states, n_actions):
        self.n_action = n_actions
        self.n_states = n_states
