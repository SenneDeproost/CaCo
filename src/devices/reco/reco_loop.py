from threading import Thread
from exp_reco import *

def loop():
	recoRun()

t = Thread(target = loop)
