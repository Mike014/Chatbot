import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import re

# Initialize resources for text pre-processing
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# Text to be pre-processed
text = "I my name is Michele"

# Preprocess the text
tokens = nltk.word_tokenize(text)
tokens = [token for token in tokens if token not in stop_words]
tokens = [stemmer.stem(token) for token in tokens]
tokens = [lemmatizer.lemmatize(token) for token in tokens]

# Print the pre-processed text
print(tokens)

# Output: ['I', 'name', 'Michele']
