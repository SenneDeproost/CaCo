from PolicyTree import *

class Thinker:
    def __init__(self, name):
        self.name = name
        self.tree = PolicyTree(name)

