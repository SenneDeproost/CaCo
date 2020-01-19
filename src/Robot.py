##############################################################
#                    CIR PROJECT CORE                        #
##############################################################
import Pyro4
from Actor import *
from Observer import *
from Thinker import *
from debug import *
from devices.Microphone import *
from devices.Speaker import *
from devices.Camera import *
from devices.Eyes import *
import time


class Robot:
    def __init__(self, name, remotes=None):
        self.name = name
        self.remotes = remotes
        self.state = 0
        self.status = "running"
        log("Initializing robot", self.name)
        self.observer = Observer(self.name)
        self.thinker = Thinker(self.name)
        self.actor = Actor(self.name)
        self.session_done = False
        self.vague = False
        self.actions = []
        self.rewards = []
        self.cont_reward = []

        if self.remotes:
            # Observer
            try:
                self.remotes['observer']
            except:
                self.observer = Pyro4.Proxy(self.remotes['observer'])
            # Thinker
            try:
                self.remotes['thinker']
            except:
                self.thinker = Pyro4.Proxy(self.remotes['thinker'])
            # Actor
            try:
                self.remotes['actor']
            except:
                self.actor = Pyro4.Proxy(self.remotes['actor'])

        self.observer.initialize()
        self.observer.register_device('microphone', Microphone(self.name))
        self.observer.register_device('camera', Camera(self.name))
        self.actor.register_device('speaker', Speaker(self.name))
        self.actor.register_device('eyes', Eyes(self.name))

    def observe(self):
        self.observer.observe()
        pass

    def think(self, i):
        action = self.thinker.think(i)
        self.actions.append(action)
        return action

    def act(self, action):
        self.actor.output_space['speaker'].append(action)
        self.actor.output_space['eyes'].append(action)
        #self.actor.output_space['eyes'].append
        self.actor.act()
        self.state = self.thinker.newest()
        #reward = int(input("Feedback score: "))
        #self.thinker.feedback(reward, action, self.state)

    def check_status(self):
        obs = self.observer.newest()
        if any(word in obs['microphone'] for word in ["stop", "kill", "nine nine", "satisfied"]):
            os.system("mpg123 -q understood.mp3")
            self.status = "session done"
            self.session_done = True
        elif any(word in obs['microphone'] for word in ["thanks", "ok", "okay", "ready",  "ha", "haha", "hahaha"]):
            os.system("mpg123 -q understood.mp3")
            self.status = "step done"
        elif not self.vague:
            os.system("mpg123 -q not_understood.mp3")
            self.actor.devices['eyes'].act('vagueleft')
            self.vague = True

    def ta(self):
        #self.observe()
        observations = self.observer.newest()
        self.actor.devices['eyes'].act('closed')
        time.sleep(2)
        self.think(observations)
        actions = self.thinker.newest()
        self.actor.devices['eyes'].act('amused')
        self.act(actions)
        self.actor.devices['eyes'].act('neutral')

    def tao(self):
        self.actor.devices['eyes'].act('neutral')
        self.ta()
        done = False
        while not done:
            self.observe()
            self.check_status()
            if self.status in ["step done", "session done"]:
                feedback = self.observer.newest()['camera']
                #self.cont_reward += feedback
                self.thinker.feedback(feedback)
                self.rewards.append(feedback)
                done = True
                self.status = "running"     # Reset the robot status

    def ask_feedback(self):
        self.actor.devices['speaker'].act("Are you satisfied with the " + self.name + " experience?")
        self.observe()
        if self.observer.newest()['microphone'] == "yes":
            old_state = 0
            new_state = 1
            for index in range(0, len(self.actions)):
                self.thinker.last_feedback(old_state, new_state, self.actions[index], self.rewards[index])
                old_state += 1
                new_state += 1
            #self.thinker.feedback(1, 1, 1, 1)
        else:
            pass
            #self.thinker.feedback(1, 1, 0, 1)
        self.actor.devices['eyes'].act('amused')
        self.actor.devices['speaker'].act("Thank you, come again!")

