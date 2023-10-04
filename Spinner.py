import random
# Jordan Reynolds
# Assignment 4

class Spinner:
    def __init__(self, synonym_file):
        self.synonyms = self.load_synonyms(synonym_file)

    def load_synonyms(self, file_path):
        synonyms = {}
        with open(file_path, 'r') as file:
            for line in file:
                word, synonym_str = line.strip().split(':')
                synonyms[word] = synonym_str.split(',')
        return synonyms

    def spin_word(self, word):
        if word.lower() in self.synonyms and random.randint(1, 100) > 50:
            synonyms = self.synonyms[word.lower()]
            return random.choice(synonyms)
        else:
            return word

    def spin_text(self, text):
        words = text.split()
        spun_words = [self.spin_word(word) for word in words]
        return ' '.join(spun_words)
