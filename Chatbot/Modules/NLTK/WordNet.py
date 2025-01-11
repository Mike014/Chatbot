import nltk
from Lemmatizing import Lemmatizer
from nltk.corpus import wordnet


class WordNet:
    def __init__(self, word):
        if not isinstance(word, str):
            raise ValueError("Expected a string, but received: %s" % type(word))
        self.lemmatizer = Lemmatizer(word)

    def get_synonyms(self):
        try:
            lemmatized_word = self.lemmatizer.lemmatize()
            if isinstance(lemmatized_word, list):
                lemmatized_word = lemmatized_word[0]
            synonyms = []
            for syn in wordnet.synsets(lemmatized_word):
                for lemma in syn.lemmas():
                    synonyms.append(lemma.name())
            return synonyms
        except Exception as e:
            print("An error occurred while retrieving synonyms: %s" % str(e))
            return []
