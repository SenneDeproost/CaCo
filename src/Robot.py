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


class Robot:
    def __init__(self, name, remotes=None):
        self.name = name
        self.remotes = remotes
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
        self.actor.register_device('speaker', Speaker(self.name))
        self.actor.devices['speaker'].act("Hi, I am Maya. I like to dance")

    def observe(self):
        self.observer.observe()
        pass

    def await_name(self):
        while True:
            result = self.observer.devices['microphone']

    def think(self):
        pass

    def act(self):
        pass
