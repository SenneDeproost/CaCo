# Reinforcement Learning Policy Tree
from anytree import Node, RenderTree
from anytree.exporter import JsonExporter
from anytree.importer import JsonImporter
from anytree.search import find, findall
import json
import random


class PolicyTree:
    def __init__(self, agent_name):
        self.tree = Node("root")
        self.agent_name = agent_name
        self.grade = 0
        self.wp = self.tree
        self.actions = ["1", "2"]

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

    def add(self, name,  parent_node):
        node = Node(name, parent=parent_node)
        node.score = 0

    def find_(self, name, parent):
        return find(self.tree, lambda node: node.name == name and node.parent == parent)

    def adhere_random(self):
        action = random.choice(self.actions)
        self.add(action, self.wp)

    def adhere_kb_best(self):
        pass

    def update_score(self):
        pass





    def best_action(self):
        possibilities = self.wp.children
        best = None
        if len(possibilities) == 0:
            self.adhere_random()  # Every action has score 0, so do random
        else:
            best = possibilities[0]
        for pos in possibilities[1:]:
            if pos.score > best.score:
                best = pos
        return best


    def random_action(self):
        action = random.choice(self.actions)
        children = self.wp.children
        exist = self.find_(action, self.wp.name)
        if not exist:
            self.add(action, self.wp)
        return action







