import Pyro4 as pyro
from debug import *
from devices.Microphone import *
@pyro.expose
class Observer:
    def __init__(self, name, hosted=False):
        self.input_space = {}
        self.devices = {}
        self.hosted = hosted
        self.name = name

    def register_devices(self):
        # Microphone
        self.devices['microphone'] = Microphone()
        log("Registered microphone", self.name)

    def initialize(self):
        if self.hosted:
            daemon = pyro.Daemon()
            uri = daemon.register(self)
            log("Initializing observer on " + str(uri), self.name)
            daemon.requestLoop()
        else:
            log("Initializing local observer", self.name)

    def observe(self):
        pass
