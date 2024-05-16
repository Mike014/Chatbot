from nltk.corpus import movie_reviews
from nltk import FreqDist
from Text_Classification import TextClassification

class FeatureExtractor:
    def __init__(self, num_features=3000):
        self.num_features = num_features
        self.word_features = self.get_word_features()

    def get_word_features(self):
        all_words = []
        for w in movie_reviews.words():
            all_words.append(w.lower())
        all_words = FreqDist(all_words)
        return list(all_words.keys())[:self.num_features]

    def find_features(self, document):
        words = set(document)
        features = {}
        for w in self.word_features:
            features[w] = (w in words)
        return features

    def get_featuresets(self, documents):
        try:
            return [(self.find_features(rev), category) for (rev, category) in documents]
        except ValueError:
            print("Each document should be a tuple of two elements: (rev, category)")
            return []


