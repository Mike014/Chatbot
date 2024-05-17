import nltk
import random
from nltk.corpus import movie_reviews
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy as nltk_accuracy

class TextClassification:
    def __init__(self):
        self.train_set = None
        self.test_set = None
        self.classifier = None

    def extract_features(self, words):
        return dict([(word, True) for word in words])
    
    def split_data(self, num_train=0.8):
        try:
            documents = [(list(movie_reviews.words(fileid)), category)
                         for category in movie_reviews.categories()
                         for fileid in movie_reviews.fileids(category)]
            random.shuffle(documents)
            
            featuresets = [(self.extract_features(words), category) for words, category in documents]
            num_train = int(len(featuresets) * num_train)
            train_set, test_set = featuresets[num_train:], featuresets[:num_train]
            return train_set, test_set
        except Exception as e:
            print("An error occurred while splitting data: %s" % str(e))
            return [], []
    
    def train_model(self, featuresets, num_train=0.8):
        try:
            num_train = int(len(featuresets) * num_train)
            self.train_set, self.test_set = featuresets[num_train:], featuresets[:num_train]
            self.classifier = NaiveBayesClassifier.train(self.train_set)
            train_accuracy = nltk_accuracy(self.classifier, self.train_set)
            test_accuracy = nltk_accuracy(self.classifier, self.test_set)
            return train_accuracy, test_accuracy
        except Exception as e:
            print("An error occurred while training the model: %s" % str(e))
            return 0, 0
    
    def classify_text(self, text):
        try:
            return self.classifier.classify(self.extract_features(text))
        except Exception as e:
            print("An error occurred while classifying text: %s" % str(e))
            return None
    
    def classify(self, text):
        return self.classify_text(text)
    
    def classify_many(self, texts):
        return [self.classify_text(text) for text in texts]


    

    



