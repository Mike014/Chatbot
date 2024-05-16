import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
from Tokenizing_Words import Tokenizer
from StopWords import RemoveStopWords
from Stemming import Stemmer
from Pos_Tagger import PosTagger
from Chunking import Chunker

class Chinker:
    def __init__(self, chunker):
        if not isinstance(chunker, Chunker):
            raise ValueError("Expected a Chunker instance, but received: %s" % type(chunker))
        self.chunker = chunker

    def chinking(self, chunkGram):
        try:
            pos_tagged = self.chunker.pos_tagger.pos_tag()
            return [nltk.RegexpParser(chunkGram).parse(tagged) for tagged in pos_tagged]
        except Exception as e:
            print("An error occurred while chinking: %s" % str(e))
            return []



                
    
