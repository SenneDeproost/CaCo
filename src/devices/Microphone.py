import speech_recognition as sr
from debug import *

class Microphone:
    def __init__(self):
        self.recorder = sr.Recognizer()
        self.mic = sr.Microphone()

    def listen(self):
        with self.mic as source:
            log("Listening...")
            audio = self.recorder.listen(source)
            input = self.recorder.recognize_google(audio)
            log("Heard: " + input)
            return input







