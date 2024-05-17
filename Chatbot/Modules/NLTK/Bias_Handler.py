from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score
from Naive_Bayes_Classifier import NaiveBayesTextClassification

class BiasHandler:
    def __init__(self, documents, num_features=3000):
        self.documents = documents
        self.classifier = NaiveBayesTextClassification(documents, num_features)

    def split_data(self, test_size=0.2):
        try:
            X, y = zip(*self.documents)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)
            return (X_train, y_train), (X_test, y_test)
        except Exception as e:
            print(f"An error occurred while splitting the data: {e}")
            return None, None

    def train_and_evaluate(self, num_train=0.8):
        (X_train, y_train), (X_test, y_test) = self.split_data(test_size=1-num_train)
        if X_train and X_test and y_train and y_test:
            try:
                # Convert tuples to dictionaries
                train_documents = [{'text': x, 'label': y} for x, y in zip(X_train, y_train)]
                test_documents = [{'text': x, 'label': y} for x, y in zip(X_test, y_test)]
                
                # Train the classifier on each individual document
                for doc in train_documents:
                    self.classifier.train(doc)
                
                # Predict the labels of the test documents
                y_pred = [self.classifier.classify(doc['text']) for doc in test_documents]
                
                # Ensure y_test and y_pred only contain 'pos' and 'neg'
                y_test = [y if y in ['pos', 'neg'] else 'neg' for y in y_test]
                y_pred = [y if y in ['pos', 'neg'] else 'neg' for y in y_pred]
                
                precision = precision_score(y_test, y_pred, pos_label='pos')
                recall = recall_score(y_test, y_pred, pos_label='pos')
                f1 = f1_score(y_test, y_pred, pos_label='pos')
                return precision, recall, f1
            except Exception as e:
                print(f"An error occurred while training the model: {e}")
                return None, None, None
        else:
            print("Data splitting failed.")
            return None, None, None
    
# # example of usage
# if __name__ == "__main__":
#     documents = [("I love this movie", "pos"), ("I hate this movie", "neg"), ("I like this movie", "pos")]
#     bias_handler = BiasHandler(documents)
#     precision, recall, f1 = bias_handler.train_and_evaluate()
#     print("Precision:", precision)
#     print("Recall:", recall)
#     print("F1 Score:", f1)
