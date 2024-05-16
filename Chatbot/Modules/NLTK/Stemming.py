import nltk
from nltk.stem import PorterStemmer
from Tokenizing_Words import Tokenizer
from StopWords import RemoveStopWords

class Stemmer:
    def __init__(self, text):
        if not isinstance(text, str):
            raise ValueError("Expected a string, but received: %s" % type(text))
        if not text:
            raise ValueError("Received an empty string")
        self.text = text
        self.tokenizer = Tokenizer(text)
        try:
            self.stop_words = RemoveStopWords(text)
        except Exception as e:
            raise ValueError("An error occurred while removing stop words: %s" % str(e))
        self.stemmer = PorterStemmer()
        
    def stem(self):
        try:
            word_tokens = self.stop_words.remove()
            return [self.stemmer.stem(word) for word in word_tokens]
        except Exception as e:
            print("An error occurred while stemming words: %s" % str(e))
            return []
    

    

