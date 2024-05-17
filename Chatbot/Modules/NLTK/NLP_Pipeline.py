# -*- coding: utf-8 -*-
import numpy as np  # Add this line
from nltk.classify import ClassifierI
from statistics import mode
from Classifier_Training import SklearnClassifiers
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers

    def classify(self, features):
        votes = []
        for c in self._classifiers:
            try:
                features_array = np.array(list(features.values())).reshape(1, -1)
                v = c.predict(features_array)[0]
                votes.append(v)
            except Exception as e:
                print(f"Error classifying with {c}: {e}")
        return mode(votes) if votes else None
        
    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            try:
                features_array = np.array(list(features.values())).reshape(1, -1)
                v = c.predict(features_array)[0]
                votes.append(v)
            except Exception as e:
                print(f"Error classifying with {c}: {e}")
            
        if not votes:
            return 0

        choice_votes = votes.count(mode(votes))
        conf = choice_votes / len(votes)
        return conf
    




    