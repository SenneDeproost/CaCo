import Pyro4 as pyro
from debug import *

class Actor:
    def __init__(self, name, hosted=False):
        self.output_space = {}
        self.devices = {}
        self.hosted = hosted
        self.name = name

    def register_device(self, name, device):
        self.devices[name] = device
        self.output_space[name] = []
        log("Registered output device " + name, self.name)

    def act(self):
        for name, device in self.devices.items():
            output = self.output_space[name][-1]
            log("Acting on output device " + name + ": " + str(output), self.name)
            device.act(output)

