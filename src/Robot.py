##############################################################
#                    CIR PROJECT CORE                        #
##############################################################
import Pyro4
from Actor import *
from Observer import *
from Thinker import *
from debug import *


class Robot:
    def __init__(self, name, remotes=None):
        self.name = name
        self.remotes = remotes
        log("Initializing robot " + self.name)
        self.observer = Observer(self.name)
        self.thinker = Thinker(self.name)
        self.actor = Actor(self.name)
        if self.remotes:
            # Observer
            if self.remotes['observer']:
                self.observer = Pyro4.Proxy(self.remotes['observer'])
            # Thinker
            if self.remotes['thinker']:
                self.thinker = Pyro4.Proxy(self.remotes['thinker'])
            # Actor
            if self.remotes['actor']:
                self.actor = Pyro4.Proxy(self.remotes['actor'])
        self.observer.initialize()

    def observe(self):
        pass

    def think(self):
        pass

    def act(self):
        pass
