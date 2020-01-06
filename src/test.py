from Robot import *
from Observer import *
import shutil
import time



import warnings
warnings.filterwarnings("ignore")

import distutils
if distutils.distutils_path.endswith('__init__.py'):
    distutils.distutils_path = os.path.dirname(distutils.distutils_path)



#observer = Observer(hosted=True, name="Jos")
name = "Caco"

robot = Robot(name)
robot.actor.devices['eyes'].act('neutral')
robot.actor.devices['eyes'].act('amused')
robot.actor.devices['speaker'].act("Hi! I am " + robot.name + ".")
robot.thinker.policy.load(name + ".json")
robot.actor.devices['eyes'].act('neutral')
done = False
while not done:
    robot.otao()
    robot.actor.devices['eyes'].act('neutral')
    state = robot.state
    feedback = robot.observer.newest()['camera']
    robot.thinker.feedback(feedback)
    robot.vague = False
    if robot.session_done:
        done = True
robot.ask_feedback()
robot.thinker.policy.save(name + ".json")







""" source = self.mic
 audio = self.recorder.listen(source)
 input = self.recorder.recognize_google(audio)
 return input"""