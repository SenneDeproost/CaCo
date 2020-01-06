import Pyro4 as pyro
from debug import *
import json

class Actor:
    def __init__(self, name, hosted=False):
        self.output_space = {}
        self.devices = {}
        self.hosted = hosted
        self.name = name
        # Possible action space
        self.sentences_file = open("actions.json")
        self.actions = {}
        self.actions['speaker'] = json.load(self.sentences_file)
        self.actions['display'] = []
        self.actions['eyes'] = []

    def register_device(self, name, device):
        self.devices[name] = device
        self.output_space[name] = []
        log("Registered output device " + name, self.name)

    def act(self):
        name = 'speaker'
        device = self.devices[name]
        output = self.actions[name][self.output_space[name][-1]]
        log("Acting on output device " + name + ": " + str(output), self.name)
        device.act(output)
        """
        for name, device in self.devices.items():
            print(self.actions[name][self.output_space[name]])
            output = self.actions[name][self.output_space[name][-1]]
            log("Acting on output device " + name + ": " + str(output), self.name)
            device.act(output)
            """

