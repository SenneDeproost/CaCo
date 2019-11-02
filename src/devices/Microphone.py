import speech_recognition as sr
import warnings
from debug import *



class Microphone:
    def __init__(self, owner):
        self.owner = owner
        try:
            self.recorder = sr.Recognizer()
            self.mic = sr.Microphone()
        except:
            pass

    def observe(self):
        input = ""
        try:
            with self.mic as source:
                log("Listening...", self.owner)
                audio = self.recorder.listen(source)
                input = self.recorder.recognize_google(audio)
                log("Heard: " + input, self.owner)
        except:
            pass
        return input





