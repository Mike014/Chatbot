import nltk
from Chunking import Chunker
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
from Pos_Tagger import PosTagger
from Stemming import Stemmer
from StopWords import RemoveStopWords
from Tokenizing_Words import Tokenizer


class Chinker:
    def __init__(self, chunker):
        if not isinstance(chunker, Chunker):
            raise ValueError(
                "Expected a Chunker instance, but received: %s" % type(chunker)
            )
        self.chunker = chunker

    def chinking(self, chunkGram):
        try:
            pos_tagged = self.chunker.pos_tagger.pos_tag()
            return [nltk.RegexpParser(chunkGram).parse(tagged) for tagged in pos_tagged]
        except Exception as e:
            print("An error occurred while chinking: %s" % str(e))
            return []
