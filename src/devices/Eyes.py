import warnings
from debug import *
import os
import shutil



class Eyes:
    def __init__(self, owner):
        self.owner = owner
        self.files = {
            "neutral": "eyes/neutral.txt",
            "closed": "eyes/closed.txt",
            "amused": "eyes/amused.txt",
            "notamused": "eyes/notamused.txt",
            "vagueleft": "eyes/vagueleft.txt",
            "vagueright": "eyes/vagueright.txt",
        }

    def act(self, state):
        file_name = self.files[state]
        f = open(file_name)
        lines = f.read()
        columns = shutil.get_terminal_size().columns
        print(lines.center(columns))




