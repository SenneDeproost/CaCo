from Robot import *
from Observer import *


import warnings
warnings.filterwarnings("ignore")

#observer = Observer(hosted=True, name="Jos")
name = "Caco"
robot = Robot(name)
robot.actor.devices['speaker'].act("Hi! I am " + robot.name + ".")
while (True):
    robot.observe()
    robot.think(robot.observer.newest())
    robot.act(robot.thinker.newest())





""" source = self.mic
 audio = self.recorder.listen(source)
 input = self.recorder.recognize_google(audio)
 return input"""