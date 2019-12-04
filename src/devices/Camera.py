import speech_recognition as sr
import warnings
from debug import *



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
            input = "darkness"
            log("Saw: " + input, self.owner)
        except:
            pass
        return input





