import nltk
from nltk.corpus import state_union
from Pos_Tagger import PosTagger
from Chunking import Chunker

nltk.download('maxent_ne_chunker')
nltk.download('words')

class NER:
    def __init__(self, text, train_text):
        self.text = text
        self.train_text = train_text
        self.pos_tagger = PosTagger(text, train_text)
        self.chunker = Chunker(text, train_text)

    def ner(self, chunk_gram=r"""Chunk: {<.*>+}
                                    }<VB.?|IN|DT>+{""", draw_trees=False):
        try:
            chunked = self.chunker.chunk(chunk_gram)
            named_entities = [nltk.ne_chunk(chunk.leaves()) for chunk in chunked]
            if draw_trees:
                for entity in named_entities:
                    entity.draw()
            return named_entities
        except Exception as e:
            print(f"An error occurred: {e}")
            return []
        


        

