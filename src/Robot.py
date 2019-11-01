##############################################################
#                    CIR PROJECT CORE                        #
##############################################################
import Pyro4

from Actor import *
from Observer import *
from Thinker import *


class Robot:
    def __init__(self, name="Maya", remotes=None):
        self.name = name
        self.observer = None
        self.thinker = None
        self.actor = None
        self.remotes = remotes
        self.initialize()

    def initialize(self):
        if self.remotes:
            # Observer
            if self.remotes['observer']:
                self.observer = Pyro4.Proxy(self.remotes['observer'])
            else:
                self.observer = Observer()

            # Thinker
            if self.remotes['thinker']:
                self.thinker = Pyro4.Proxy(self.remotes['thinker'])
            else:
                self.thinker = Thinker()

            # Actor
            if self.remotes['actor']:
                self.actor = Pyro4.Proxy(self.remotes['actor'])
            else:
                self.actor = Actor()

    def observe(self):
        pass

    def think(self):
        pass

    def act(self):
        pass
