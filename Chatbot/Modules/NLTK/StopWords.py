import nltk
from nltk.corpus import stopwords
from Tokenizing_Words import Tokenizer

class RemoveStopWords:
    def __init__(self, text, language='english'):
        if not isinstance(text, str):
            raise ValueError("Expected a string, but received: %s" % type(text))
        if not text:
            raise ValueError("Received an empty string")
        self.text = text
        self.tokenizer = Tokenizer(text)
        try:
            self.stop_words = set(stopwords.words(language))
        except Exception as e:
            raise ValueError("An error occurred while loading stop words: %s" % str(e))
        
    def remove(self):
        try:
            word_tokens = self.tokenizer.tokenize_word()
            return [word for word in word_tokens if word not in self.stop_words]
        except Exception as e:
            print("An error occurred while removing stop words: %s" % str(e))
            return []

