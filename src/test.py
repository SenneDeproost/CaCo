from Robot import *
from Observer import *


import warnings
warnings.filterwarnings("ignore")

#observer = Observer(hosted=True, name="Jos")

robot = Robot(name="Lana")
robot.observe()




""" source = self.mic
 audio = self.recorder.listen(source)
 input = self.recorder.recognize_google(audio)
 return input"""