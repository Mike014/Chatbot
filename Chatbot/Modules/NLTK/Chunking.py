import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
from Tokenizing_Words import Tokenizer
from StopWords import RemoveStopWords
from Stemming import Stemmer
from Pos_Tagger import PosTagger

class Chunker:
    def __init__(self, text, train_text=None):
        if not isinstance(text, str) or not isinstance(train_text, str):
            raise ValueError("Expected a string for text and train_text, but received: %s and %s" % (type(text), type(train_text)))
        if not text or not train_text:
            raise ValueError("Received an empty string for text or train_text")
        self.text = text
        self.train_text = train_text
        self.pos_tagger = PosTagger(text, train_text)
        
    def chunk(self, chunk_gram):
        try:
            pos_tagged = self.pos_tagger.pos_tag()
            chunk_parser = nltk.RegexpParser(chunk_gram)
            return [chunk_parser.parse(tagged_sentence) for tagged_sentence in pos_tagged]
        except Exception as e:
            print("An error occurred while chunking: %s" % str(e))
            return []



    
