class Entry:
    def __int__(self, score, content):
        self.score = score
        self.content = content

    def update_score(self, new_score):
        self.score = new_score

    def update_content(self, new_content):
        self.content = new_content




class KnowledgeBase:
    def __int__(self, input_file):
        self.input_file = input_file
        self.kb = []

    def add_entry(self, score, content):
        entry = Entry(score, content)
        self.kb.append(entry)

    def update_entry(self, score, content):
        pass

    def save_kb(self):
        pass

    def load_kb(self):
        pass
    