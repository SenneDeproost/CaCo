from threading import Thread

import speech_recognition as sr
from debug import *


class Microphone:
    def __init__(self, owner):
        self.owner = owner
        self.recorder = sr.Recognizer()
        self.mic = sr.Microphone()
        self.observation = ""
        self.thread = None

    def observe_(self):
        input = ""
        try:
            with self.mic as source:
                log("Listening...", self.owner)
                try:
                    audio = self.recorder.record(source, duration=4)  #### !!!!!!! change to listen afterwards
                     # audio = self.recorder.listen(source)
                    log("Recognizing speech...", self.owner)
                    input = self.recorder.recognize_google(audio)
                     # input = self.recorder.recognize_sphinx(audio)
                    log("Heard: " + input, self.owner)
                except:
                    pass
        except Exception as e:
            pass
        self.observation = input
        exit()
        #break

    def observe(self):
        self.thread = Thread(target=self.observe_)
        self.thread.start()







