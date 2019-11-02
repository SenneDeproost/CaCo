import Pyro4 as pyro
from debug import *
import threading
@pyro.expose
class Observer:
    def __init__(self, name, hosted=False):
        self.input_space = {}
        self.devices = {}
        self.hosted = hosted
        self.name = name
        self.active = True
        threading.Thread(target=self.observe_loop, args=()).start()

    def register_device(self, name, device):
        self.devices[name] = device
        self.input_space[name] = []
        log("Registered input device " + name, self.name)

    def initialize(self):
        if self.hosted:
            daemon = pyro.Daemon()
            uri = daemon.register(self)
            log("Initializing observer on " + str(uri), self.name)
            daemon.requestLoop()
        else:
            log("Initializing local observer", self.name)

    def observe(self):
        for name, device in self.devices.items():
            observation = device.observe()
            self.input_space[name].append(observation)

    def observe_loop(self):
        while self.active:
            self.observe()


