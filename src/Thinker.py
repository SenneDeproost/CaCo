from PolicyTree import *
from PolicyMatrix import *
import random
from debug import *

class Thinker:
    def __init__(self, name):
        self.name = name
        self.tree = PolicyTree(name)
        self.policy = PolicyMatrix(name, 21, 21)
        self.state = 0
        self.epsilon = 0.1
        self.states = [0]
        self.actions = [0]

    counter = -1
    def think(self, i):
        l = [“Lets sort through this together”,
        "Visualize yourself in a nice situation during the day",
        “Your worries are not silly”,
        "Make a cup of coffee or tea, slow down and notice the ritual",
        “Take, your time”,
        "Think about 3 things you liked about this week",
        "What is a robot’s favorite type of music? - Heavy metal!",
        "I am proud of you. Good job.",
        "Try to focus on the tense areas in your body and pay attention to how you feel",
        “You are capable, you are wstrong”]
        counter = counter + 1
        return l[counter]

        """
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
        """

    def feedback(self, reward, action, new_state):
        self.policy.update(self.state, action, new_state, reward)


    def newest(self):
        return self.actions[-1]







