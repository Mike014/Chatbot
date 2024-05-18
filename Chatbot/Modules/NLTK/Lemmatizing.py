import nltk
from nltk.stem import WordNetLemmatizer
from Tokenizing_Words import Tokenizer
from StopWords import RemoveStopWords

class Lemmatizer:
    def __init__(self, text):
        if not isinstance(text, str):
            raise ValueError("Expected a string, but received: %s" % type(text))
        if not text:
            raise ValueError("Received an empty string")
        self.text = text
        self.tokenizer = Tokenizer(text)
        self.stop_words = RemoveStopWords(text)
        self.lemmatizer = WordNetLemmatizer()
        
    def lemmatize(self, pos=nltk.corpus.reader.wordnet.VERB):
        try:
            word_tokens = self.stop_words.remove()
            return [self.lemmatizer.lemmatize(word, pos) for word in word_tokens]
        except Exception as e:
            print("An error occurred while lemmatizing words: %s" % str(e))
            return []

def lemmatize(text):
    lemmatizer = Lemmatizer(text)
    return lemmatizer.lemmatize()

                    
        
        


    

