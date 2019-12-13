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


class Robot:
    def __init__(self, name, remotes=None):
        self.name = name
        self.remotes = remotes
        self.state = 0
        log("Initializing robot", self.name)
        self.observer = Observer(self.name)
        self.thinker = Thinker(self.name)
        self.actor = Actor(self.name)
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

    def observe(self):
        self.observer.observe()
        pass

    def await_name(self):
        while True:
            result = self.observer.devices['microphone']

    def think(self, i):
        i['state'] = self.state
        action = self.thinker.think(i)
        return action

    def act(self, action):
        self.actor.output_space['speaker'].append(action)
        self.actor.act()
        self.state = self.thinker.newest()
        #reward = int(input("Feedback score: "))
        #self.thinker.feedback(reward, action, self.state)

    def ota(self):
        self.observe()
        observations = self.observer.newest()
        self.think(observations)
        actions = self.thinker.newest()
        self.act(actions)

    def done(self):
        loop = True
        while loop:
            self.observe()
            obs = self.observer.newest()
            if any(word in obs['microphone'] for word in ["satisfied", "finish", "finished"]):
                self.ask_feedback()
            elif any(word in obs['microphone'] for word in ["done", "ok", "okay", "ready"]):
                loop = False



    def ask_feedback(self):
        self.actor.devices['speaker'].act("Are you satisfied with the " + self.name + " experience?")
        self.observe()
        if self.observer.newest()['microphone'] == "yes":
            self.thinker.feedback(1, 1, 1, 1)
        else:
            self.thinker.feedback(1, 1, 0, 1)
        self.actor.devices['speaker'].act("Thank you, come again!")