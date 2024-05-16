import nltk
import pickle
from Text_Classification import TextClassification
from Tokenizing_Words import Tokenizer
from StopWords import RemoveStopWords
from Lemmatizing import Lemmatizer
from Converting_words_to_Features import FeatureExtractor
from Naive_Bayes_Classifier import NaiveBayesTextClassification

nltk.download('movie_reviews')

class NaiveBayesTextClassification:
    def __init__(self, documents, num_features=3000): 
        if not all(isinstance(doc, tuple) and len(doc) == 2 for doc in documents):
            raise ValueError("Each document should be a tuple of two elements: (rev, category)")
        self.documents = documents
        self.extractor = FeatureExtractor(num_features)
        self.classifier = TextClassification()

    def preprocess(self, text): 
        tokenizer = Tokenizer(text)
        remover = RemoveStopWords(text)
        lemmatizer = Lemmatizer(text)
        tokenized_text = tokenizer.tokenize_word()
        no_stopwords_text = remover.remove()
        lemmatized_text = lemmatizer.lemmatize()
        return lemmatized_text

    def train(self, num_train=0.8):
        preprocessed_documents = [(self.preprocess(text), category) for text, category in self.documents]  
        featuresets = self.extractor.get_featuresets(preprocessed_documents)
        if not featuresets:
            raise ValueError("No features could be extracted from the documents")
        self.classifier.train_model(featuresets, num_train)

        with open("naive_bayes_classifier.pickle", "wb") as f:
            pickle.dump(self.classifier, f)

    def load_classifier(self):
        with open("naive_bayes_classifier.pickle", "rb") as f:
            self.classifier = pickle.load(f)

    def classify(self, new_text):
        self.load_classifier()
        preprocessed_text = self.preprocess(new_text)  
        features = self.extractor.find_features(preprocessed_text)
        if not features:
            raise ValueError("No features could be extracted from the new text")
        return self.classifier.classify(features)



