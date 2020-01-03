import speech_recognition as sr
import warnings
from debug import *
from devices.reco.exp_reco import *



class Camera:
    def __init__(self, owner):
        self.owner = owner
        self.observation = ""
        try:
            pass
        except:
            pass

    def observe(self):
        input = ""
        try:
            log("Seeing...", self.owner)
            score = 0
            for i in range(30):
                score += recoRun()
            input = score
            log("Saw: " + str(input), self.owner)
        except Exception as e:
            print(e)
        self.observation = input
        return input





