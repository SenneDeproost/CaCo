import speech_recognition as sr
import warnings
from debug import *
from gtts import gTTS
import os



class Speaker:
    def __init__(self, owner):
        self.owner = owner

    def act(self, sentence):
        sentence = str(sentence)
        log("Speaking: " + sentence, self.owner)
        file = "speech.mp3"
        tts = gTTS(sentence, 'en')
        tts.save(file)
        os.system("mpg123 " + file)

