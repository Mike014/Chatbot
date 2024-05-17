# -*- coding: utf-8 -*-
from Text_Classification import TextClassification
from Tokenizing_Words import Tokenizer
from StopWords import RemoveStopWords
from Lemmatizing import Lemmatizer
from Converting_words_to_Features import FeatureExtractor

class NaiveBayesTextClassification:
    def __init__(self, documents, num_features=3000):
        if not all(isinstance(doc, tuple) and len(doc) == 2 for doc in documents):
            raise ValueError("Each document should be a tuple of two elements: (rev, category)")
        self.documents = documents
        self.extractor = FeatureExtractor(num_features)
        self.classifier = TextClassification()

    def preprocess(self, document):
        text, category = document
        tokenizer = Tokenizer(text)
        remover = RemoveStopWords(text)
        lemmatizer = Lemmatizer(text)
        tokenized_text = tokenizer.tokenize_word()
        no_stopwords_text = remover.remove()
        lemmatized_text = lemmatizer.lemmatize()
        return lemmatized_text, category

    def train(self, num_train=0.8):
        preprocessed_documents = [self.preprocess(doc) for doc in self.documents]
        featuresets = self.extractor.get_featuresets(preprocessed_documents)
        if not featuresets:
            raise ValueError("No features could be extracted from the documents")
        self.classifier.train_model(featuresets, num_train)
        
    def classify(self, new_text):
        preprocessed_text = self.preprocess((new_text, ""))[0]
        features = self.extractor.find_features(preprocessed_text)
        if not features:
            raise ValueError("No features could be extracted from the new text")
        return self.classifier.classify(features)





