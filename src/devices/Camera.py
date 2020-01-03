import speech_recognition as sr
import warnings
from debug import *
from devices.reco.exp_reco import *



class Camera:
    def __init__(self, owner):
        self.owner = owner 
        try:
            pass
        except:
            pass

    def observe(self):
        input = ""
        try:
            log("Seeing...", self.owner)
            for i in range(50):
                recoRun()
            input = score
            log("Saw: " + str(input), self.owner)
        except Exception as e:
            print(e)
        return input





