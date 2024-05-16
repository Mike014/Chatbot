import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize, sent_tokenize

# Text to be pre-processed
raw = "The quick brown foxes jumped over the lazy dogs. The dogs were not amused."

# Tokenize the text
tokens = word_tokenize(raw)

# Initialize the stemmer and lemmatizer
porter = PorterStemmer()

# Stem the tokens
stemmed = [porter.stem(t) for t in tokens]
print('Stemmed:', stemmed)

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Lemmatize the tokens
lemmatized = [lemmatizer.lemmatize(t) for t in tokens]
print('Lemmatized:', lemmatized)




