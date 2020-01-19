import numpy as np
import random
import json

#class TransMatrix:
#    def __init__(self):
#        self.transitions = np.ones([20, 20])
#        self.transitions[:,0] = 0



class PolicyMatrix:
    def __init__(self, name, n_states, n_actions):
        self.n_actions = n_actions
        self.n_states = n_states
        self.policy = np.zeros([n_states, n_actions])

    def best(self, state_indx):
        return np.argmax(self.policy[0:15][state_indx])

    def random(self):
        #return random.randint(0, self.n_actions - 1)
        return random.randint(0, 16 - 1)

    def update(self, old_state, action, new_state, reward):
        print(old_state, action, new_state, reward)
        self.policy[old_state][action] += 0.9*(reward + 0.9*np.max(self.policy[new_state, :]) - self.policy[old_state, action])
        print(self.policy[old_state][action])

    def load(self, file_name):
        f = open("../data/policies/matrix/" + file_name)
        self.policy = np.array(json.load(f))

    def save(self, file_name):
        f = open("../data/policies/matrix/" + file_name, 'w')
        json.dump(self.policy.tolist(), f)
