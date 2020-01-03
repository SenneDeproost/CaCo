import speech_recognition as sr
import warnings
from debug import *
from threading import Thread
import time



class Microphone:
    def __init__(self, owner):
        self.owner = owner
        self.recorder = sr.Recognizer()
        self.mic = sr.Microphone()
        self.observation = ""
        self.thread = None

    def observe_(self):
        input = ""
        with self.mic as source:
            log("Listening...", self.owner)
            try:
                audio = self.recorder.record(source, duration=4) #### !!!!!!! change to listen afterwards
                #audio = self.recorder.listen(source)
                log("Recognizing speech...", self.owner)
                #input = self.recorder.recognize_google(audio)
                input = self.recorder.recognize_sphinx(audio)
                log("Heard: " + input, self.owner)
            except:
                pass
        self.observation = input
        exit()
        #break

    def observe(self):
        self.thread = Thread(target=self.observe_)
        self.thread.start()







