# CaCo: the calming companion
Project developed for the course _Cognitive Interactions with Robotics_ at the **Universitat Politechnica de Catalunya** 
(UPC), Barcelona Spain. Final project score: 9.5/10, first of the class.

![The CaCo robot.](https://i.imgur.com/xRdZVqk.jpg)

## Motivation
Stress in today's society is present in everyone. Whether returning from an exhaustive day working with more to do at home 
or before an upcoming exam, many reasons can induce this unpleasant feeling. To combat this, we made a robotic experience
that can help to calm you down by interacting with it in a relaxing conversation. It has pre-build exercises that the user
can do to reduce its stress level. The more the user interacts with the robot, the smarter it becomes thanks to a built-in
reinforcement learning algorithm based on classical Q-learning. It uses a pretrained deep neural network to recognize the 
current emotions reflected in the user's face. This form of feedback is incorporated in the learning part of the robot, 
adapting it to only say the sentences that makes the user most comfortable.

## Usage
The robot is programmed to be run in a SSH session on a mobile screen. It is optimised for usage on a 6-inch 1080p phone 
using the Termux terminal emulator app. When used on a computer screen, select a font size for the terminal so that the 
displayed eyes are aligned in the middle. The device that will handle all logic, most often the computer, needs to have a 
clear sight on the face of the user so its facial expressions can be read from.

To initialize the project, run the following commands in an open terminal:

1. `git clone https://github.com/SenneDeproost/CaCo.git` 
2. `cd CaCo`
3. `bash install.sh`

To run the robot, insert following commands in the terminal:

1. `source venv/bin/activate`
2. `python src/test.py`




## Interaction
![Facial expression recognition](https://i.imgur.com/D5icOdB.png)
The robot will indicate with two short bleeps when the user can say something. Laughing, saying "ok" en "thanks" make it
progress in the conversation. When the user wants to quit, he or she has to say "statisfied" to end the experience. Afterwards
the robot will ask one final question how the interaction was. The user can reply with "yes" or "no" wheter the robot has 
helped in reducing the stress of the user.


## Inner workings
![UML diagram](https://i.imgur.com/BQ2WHsI.png)
## Future work
There are several extensions possible to the project. One of them is the integration of user profiles with automatic which 
person is interacting with the robot. With this, the robot can learn a global behaviour that can be further 
individualised for a more personal experience.

Another improvement is the usage of the on-board systems of the smartphone instead of using the camera and computational
resources of the computer the application runs on. However, this aks for better access to the device's hardware by integrating
it into a fully functional Android or iOS app or by using a PWA framework. Due to the scope of the project within the course
most of these considerations were left untouched, leaving room for improvement.

## Credits
All credits for the emotional recognition part goes to [Octavio Arriaga](https://github.com/oarriaga/face_classification):
[code](https://github.com/oarriaga/face_classification)