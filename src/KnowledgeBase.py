import json

class KnowledgeBase:
    def __int__(self, input_file):
        self.input_file = input_file
        self.kb = []

    def add_entry(self, score, content, parent="root"):
        entry = {}
        entry['content'] = content
        entry['score'] = score
        entry['parent'] = parent
        self.kb.append(entry)

    def find_entry(self, score=None, content=None, parent=None):
        result = []
        if score:
            result.extend(list(filter(lambda entry: entry['score'] == score, self.kb)))
        if content:
            result.extend(list(filter(lambda entry: content in entry['content'], self.kb)))
        if parent:
            result.extend(list(filter(lambda entry: entry['parent'] == parent, self.kb)))
        return list(set(result))

    def update_entry(self, content, parent):
        
        pass

    def save_kb(self):
        with open(self.input_file, 'w') as f:
            json.dump(self.kb, f)

    def load_kb(self):
        with open(self.input_file, 'r') as f:
            self.kb = json.load(f)

