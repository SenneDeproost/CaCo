from Robot import *
from Observer import *
from devices.Microphone import *

#observer = Observer(hosted=True, name="Jos")

robot = Robot(name="Maya")
m = Microphone()
m.listen()


""" source = self.mic
 audio = self.recorder.listen(source)
 input = self.recorder.recognize_google(audio)
 return input"""