import nltk
import random
import os 

from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
from sklearn.svm import LinearSVC, NuSVC
from Tokenizing_Words import word_tokenize
from Classifier_Training import SklearnClassifiers
from Bias_Handler import BiasHandler
from Converting_words_to_Features import FeatureExtractor
from StopWords import RemoveStopWords
from Lemmatizing import Lemmatizer
from Stemming import Stemmer
from statistics import mode

class Classifier(SklearnClassifiers):
    def __init__(self, *classifiers):
        self._classifiers = classifiers
        
    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)
    
    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
            
        choice_votes = votes.count(mode(votes))
        conf = choice_votes / len(votes)

        return conf
    
    @staticmethod
    def sentiment_analysis():
        print("Starting sentiment analysis...") 
        
        # nested function to read files from directory
        def read_files_from_directory(path):
            file_contents = []
            for filename in os.listdir(path):
                print(f"Processing file: {filename}")
                with open(os.path.join(path, filename), 'r', encoding='utf-8') as file:
                    file_contents.append(file.read())
            print("Files processed.")
            return '\n'.join(file_contents)
    
        # pos_path = "D:\\Roba da autodidatta\\Videogames\\Code Academy\\Chatbots in Python\\aclImdb\\test\\pos"
        pos_path = "D:\\Roba da autodidatta\\Videogames\\Code Academy\\Chatbots in Python\\Test Sentiment\\Pos"
        neg_path = "D:\\Roba da autodidatta\\Videogames\\Code Academy\\Chatbots in Python\\Test Sentiment\\Neg"
        
        print("Reading positive files...")
        short_pos = read_files_from_directory(pos_path)
        print("Reading negative files...")
        short_neg = read_files_from_directory(neg_path)
        
        documents = []
        
        for r in short_pos.split('\n'):
            documents.append((r, "pos"))
        
        for r in short_neg.split('\n'):
            documents.append((r, "neg"))
            
        all_words = []
       
        print("Tokenizing, removing stop words, lemmatizing and stemming positive words...")
        short_pos_words = word_tokenize(short_pos)
        for w in short_pos_words:
            print(w)
        stop_words_remover = RemoveStopWords(' '.join(short_pos_words))
        short_pos_words = stop_words_remover.remove()
        for w in short_pos_words:
            print(w)
        lemmatizer = Lemmatizer(' '.join(short_pos_words))
        short_pos_words = lemmatizer.lemmatize()
        for w in short_pos_words:
            print(w)
        stemmer = Stemmer(' '.join(short_pos_words))
        short_pos_words = stemmer.stem()
        for w in short_pos_words:
            print(w)
        print("Positive words:")

        print("Tokenizing negative words...")
        short_neg_words = word_tokenize(short_neg)
        for w in short_pos_words:
            print(w)
        stop_words_remover = RemoveStopWords(' '.join(short_neg_words))
        short_neg_words = stop_words_remover.remove()
        for w in short_pos_words:
            print(w)
        lemmatizer = Lemmatizer(' '.join(short_neg_words))
        short_neg_words = lemmatizer.lemmatize()
        for w in short_pos_words:
            print(w)
        stemmer = Stemmer(' '.join(short_neg_words))
        short_neg_words = stemmer.stem()
        for w in short_pos_words:
            print(w)
        print("Negative words:")
        
        print("Adding words to all_words list...")
        
        for w in short_pos_words:
            all_words.append(w.lower())
            
        for w in short_neg_words:
            all_words.append(w.lower())
            
        all_words = nltk.FreqDist(all_words)
         
        word_features = list(all_words.keys())[:5000] # 5000 most common words
        
        # Blocco del codice
        find_features = lambda document: {w: (w in word_tokenize(document)) for w in word_features} # lambda function to find features
        
        try:
            print("Finding features...")
            featuresets = [(find_features(rev), category) for (rev, category) in documents]
        except Exception as e:
            print(f"An error occurred while finding features: {str(e)}")
            return
        
        random.shuffle(featuresets)
        
        training_set = featuresets[:10000]
        testing_set = featuresets[10000:]
        
        MNB_classifier = SklearnClassifiers(MultinomialNB())
        MNB_classifier.train(training_set)

        BernoulliNB_classifier = SklearnClassifiers(BernoulliNB())
        BernoulliNB_classifier.train(training_set)

        LogisticRegression_classifier = SklearnClassifiers(LogisticRegression())
        LogisticRegression_classifier.train(training_set)

        SGDClassifier_classifier = SklearnClassifiers(SGDClassifier())
        SGDClassifier_classifier.train(training_set)

        LinearSVC_classifier = SklearnClassifiers(LinearSVC())
        LinearSVC_classifier.train(training_set)

        NuSVC_classifier = SklearnClassifiers(NuSVC())
        NuSVC_classifier.train(training_set)

        # Create a list of the trained classifiers
        classifiers = [MNB_classifier, BernoulliNB_classifier, LogisticRegression_classifier, SGDClassifier_classifier, LinearSVC_classifier, NuSVC_classifier]

        # Use the classifiers for prediction, etc.
        for classifier in classifiers:
            print("Classifier accuracy percent:", (nltk.classify.accuracy(classifier, testing_set)) * 100)

        voted_classifier = Classifier(*classifiers)
        print("voted_classifier accuracy percent:", (nltk.classify.accuracy(voted_classifier, testing_set)) * 100)

        print("Sentiment analysis completed.")

if __name__ == "__main__":
    Classifier.sentiment_analysis()

        
