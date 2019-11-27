# Reinforcement Learning Policy Tree
from anytree import Node, RenderTree
from anytree.exporter import JsonExporter
from anytree.importer import JsonImporter
import json

class PolicyTree:
    def __init__(self, agent_name):
        self.nodes = []
        self.tree = None
        self.agent_name = agent_name

    def save(self):
        extension = ".rpt"
        dir_name = "../data/policies/"
        file_name = dir_name + self.agent_name + extension
        exporter = JsonExporter(indent=2, sort_keys=True)
        with open(file_name, 'w') as f:
            json.dump(exporter.export(self.tree), f)
            f.close()

    def load(self):
        extension = ".rpt"
        dir_name = "../data/policies/"
        file_name = dir_name + self.agent_name + extension
        importer = JsonImporter()
        data = None
        with open(file_name, "r") as f:
            data = json.loads(f)
            f.close()
        self.tree = importer.import_(data)







