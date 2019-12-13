import speech_recognition as sr
import warnings
from debug import *



class Microphone:
    def __init__(self, owner):
        self.owner = owner
        self.recorder = sr.Recognizer()
        self.mic = sr.Microphone()

    def observe(self):
        with self.mic as source:
            log("Listening...", self.owner)
            audio = self.recorder.listen()
            input = self.recorder.recognize_google(audio)
            log("Heard: " + input, self.owner)
        return input





