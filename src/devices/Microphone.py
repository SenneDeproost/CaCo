import speech_recognition as sr
import warnings
from debug import *



class Microphone:
    def __init__(self, owner):
        self.owner = owner
        self.recorder = sr.Recognizer()
        self.mic = sr.Microphone()

    def observe(self):
        input = ""
        with self.mic as source:
            log("Listening...", self.owner)
            audio = self.recorder.record(source, duration=4) #### !!!!!!! change to listen afterwards
            #audio = self.recorder.listen(source)
            log("Recognizing speech...", self.owner)
            input = self.recorder.recognize_google(audio)
            log("Heard: " + input, self.owner)
        return input





