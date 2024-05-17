import nltk
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from sklearn.model_selection import cross_val_score
from sklearn.feature_extraction import DictVectorizer
from Text_Classification import TextClassification
from Converting_words_to_Features import FeatureExtractor

class SklearnClassifiers:
    def __init__(self, documents, num_features=3000):
        self.documents = documents
        self.extractor = FeatureExtractor(num_features)
        self.vectorizer = DictVectorizer()
        self.classifiers = [] 

    def train(self, cv=2):  
        try:
            featuresets = self.extractor.get_featuresets(self.documents)
            X, y = zip(*featuresets) 
            X = self.vectorizer.fit_transform(X)  

            print("Class labels in dataset:", set(y))

            classifier_classes = [MultinomialNB, BernoulliNB, LogisticRegression, SGDClassifier, SVC, LinearSVC, NuSVC]
            classifier_names = ["MNB", "BernoulliNB", "LogisticRegression", "SGDClassifier", "SVC", "LinearSVC", "NuSVC"]

            for clf_class, name in zip(classifier_classes, classifier_names):
                try:
                    if name in ["LinearSVC"]:
                        clf = clf_class(dual=True)
                    else:
                        clf = clf_class()
                    scores = cross_val_score(clf, X, y, cv=cv)
                    print(f"{name}_classifier scores: {scores.mean()}")
                    clf.fit(X, y)
                    self.classifiers.append(clf)
                except ValueError as e:
                    print(f"Error training {name} classifier: {e}")
                except Exception as e:
                    print(f"Error training {name} classifier: {e}")
        except ValueError as e:
            print(f"Error training classifiers: {e}")
        except Exception as e:
            print(f"Error training classifiers: {e}")
                        
                    




    




