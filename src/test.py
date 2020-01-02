from Robot import *
from Observer import *


import warnings
warnings.filterwarnings("ignore")

#observer = Observer(hosted=True, name="Jos")
name = "Lana"
robot = Robot(name)
robot.actor.devices['speaker'].act("Hi! I am " + robot.name + ".")
done = False
while not done:
    robot.otao()
    state = robot.state
    feedback = int(input("> "))
    robot.thinker.feedback(feedback)
    if robot.session_done:
        done = True
robot.ask_feedback()







""" source = self.mic
 audio = self.recorder.listen(source)
 input = self.recorder.recognize_google(audio)
 return input"""