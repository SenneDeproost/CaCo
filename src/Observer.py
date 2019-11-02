import Pyro4 as pyro
from debug import *
@pyro.expose
class Observer:
    def __init__(self, name, hosted=False):
        self.input_space = {}
        self.hosted = hosted
        self.name = name

    def register_devices(self):
        pass

    def initialize(self):
        if self.hosted:
            daemon = pyro.Daemon()
            uri = daemon.register(self)
            log("Initializing " + self.name + " observer on " + str(uri))
            daemon.requestLoop()
        else:
            log("Initializing local " + self.name + " observer")

    def observe(self):
        pass
