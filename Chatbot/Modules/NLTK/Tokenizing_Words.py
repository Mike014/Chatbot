import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

class Tokenizer:
    def __init__(self):
        self.text = None

    def set_text(self, text):
        if not isinstance(text, str):
            raise ValueError("Expected a string, but received: %s" % type(text))
        if not text:
            raise ValueError("Received an empty string")
        self.text = text

    def tokenize_sentence(self):
        if self.text is None:
            raise ValueError("No text set for tokenization")
        try:
            return sent_tokenize(self.text)
        except Exception as e:
            print("An error occurred while tokenizing sentences: %s" % str(e))
            return []
    
    def tokenize_word(self):
        if self.text is None:
            raise ValueError("No text set for tokenization")
        try:
            return word_tokenize(self.text)
        except Exception as e:
            print("An error occurred while tokenizing words: %s" % str(e))
            return []

