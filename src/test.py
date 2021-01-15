from Robot import *
from Observer import *
import shutil
import time
import os



import warnings
warnings.filterwarnings("ignore")

#import distutils
#if distutils.distutils_path.endswith('__init__.py'):
#    distutils.distutils_path = os.path.dirname(distutils.distutils_path)



#observer = Observer(hosted=True, name="Jos")
name = "Caco"
os.system("mpg123 -q open.mp3")
robot = Robot(name)
robot.actor.devices['eyes'].act('neutral')
time.sleep(5)
robot.actor.devices['eyes'].act('amused')
robot.actor.devices['speaker'].act("Hi! I am " + robot.name + ".")
robot.thinker.policy.load(name + ".json")
robot.actor.devices['eyes'].act('neutral')
done = False
while not done:
    robot.tao()
    robot.actor.devices['eyes'].act('neutral')
    robot.vague = False
    if robot.session_done:
        done = True
robot.ask_feedback()
robot.actor.devices['eyes'].act('closed')
os.system("mpg123 -q exit.mp3")
robot.thinker.policy.save(name + ".json")
print(robot.actions)
print(robot.rewards)







""" source = self.mic
 audio = self.recorder.listen(source)
 input = self.recorder.recognize_google(audio)
 return input"""