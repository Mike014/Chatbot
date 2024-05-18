# Import your modules
import pandas as pd
from os import remove
from nltk import stem
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from Tokenizing_Words import tokenize
from StopWords import RemoveStopWords
from Stemming import Stemmer
from Lemmatizing import lemmatize
import joblib

def load_data():
    # Read the CSV file
    data = pd.read_csv("D:\\Roba da autodidatta\\Videogames\\Game Audio Programming\\tableConvert.com_xm5dcg.csv", on_bad_lines='skip')
    
    # Print the first few rows of the DataFrame
    print(data.head())
    
    # Convert the data to a list of tuples and return it
    return list(zip(data['Command'], data['Label']))

def prepare_data(data):
    commands = [command for command, label in data]
    labels = [label for command, label in data]
    commands = [' '.join(tokenize(command)) for command in commands]
    commands = [' '.join(RemoveStopWords(command).remove()) for command in commands]
    commands = [' '.join(Stemmer(command).stem()) for command in commands]
    commands = [lemmatize(command) for command in commands if command.strip()]
    return commands, labels

def train_model(commands, labels):
    vectorizer = CountVectorizer()
    # Join each list of words into a single string
    commands = [' '.join(command) for command in commands]
    features = vectorizer.fit_transform(commands)
    features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2)
    model = MultinomialNB()
    model.fit(features_train, labels_train)
    labels_pred = model.predict(features_test)
    print(classification_report(labels_test, labels_pred))
    return model, vectorizer

def save_model(model, vectorizer, model_path, vectorizer_path):
    joblib.dump(model, model_path)
    joblib.dump(vectorizer, vectorizer_path)

def main():
    data = load_data()
    commands, labels = prepare_data(data)
    model, vectorizer = train_model(commands, labels)
    save_model(model, vectorizer, 'model.pkl', 'vectorizer.pkl')

if __name__ == "__main__":
    main()

