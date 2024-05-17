import nltk
from nltk.corpus import state_union 
from nltk.tokenize import PunktSentenceTokenizer
from Tokenizing_Words import Tokenizer
from StopWords import RemoveStopWords
from Stemming import Stemmer

class PosTagger:
    def __init__(self, text, train_text):
        if not isinstance(text, str) or not isinstance(train_text, str):
            raise ValueError("Expected a string for text and train_text, but received: %s and %s" % (type(text), type(train_text)))
        if not text or not train_text:
            raise ValueError("Received an empty string for text or train_text")
        self.text = text
        self.train_text = train_texta
        self.sent_tokenizer = PunktSentenceTokenizer(train_text)
        
    def pos_tag(self):
        try:
            tokenized = self.sent_tokenizer.tokenize(self.text)
            return [nltk.pos_tag(nltk.word_tokenize(i)) for i in tokenized]
        except Exception as e:
            print("An error occurred while POS tagging: %s" % str(e))
            return []
               
    

    

        
        
