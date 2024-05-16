import nltk
from nltk.corpus import gutenberg
from Tokenizing_Words import Tokenizer

class CorpusHandler:
    def __init__(self, corpus):
        if not isinstance(corpus, str):
            raise ValueError("Expected a string, but received: %s" % type(corpus))
        if not corpus:
            raise ValueError("Received an empty string")
        self.corpus = corpus 
        self.tokenizer = Tokenizer(corpus)
            
    def load_corpus(self):
        try: 
            return gutenberg.raw(self.corpus)
        except Exception as e:
            print("An error occurred while loading the corpus: %s" % str(e))
            return ""
        
    def tokenize_corpus(self):
        try: 
            self.tokenizer.text = self.load_corpus()
            return self.tokenizer.tokenize_word()
        except Exception as e:
            print("An error occurred while tokenizing the corpus: %s" % str(e))
            return []
        

    

    
