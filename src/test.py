from Robot import *
from Observer import *


import warnings
warnings.filterwarnings("ignore")

#observer = Observer(hosted=True, name="Jos")
name = "Lana"
robot = Robot(name)
robot.actor.devices['speaker'].act("Hi! I am " + robot.name + ".")
robot.observe()
while (True):
    robot.think(robot.observer.newest())
    robot.act(robot.thinker.newest())
    robot.done()






""" source = self.mic
 audio = self.recorder.listen(source)
 input = self.recorder.recognize_google(audio)
 return input"""