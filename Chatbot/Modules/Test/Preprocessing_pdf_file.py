import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from PyPDF2 import PdfReader

stopwords = set(stopwords.words('english'))
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

with open('D:\\Roba da autodidatta\\Videogames\\C++\\Visual Studio\\Shortcut utili.pdf', 'rb') as f:
    reader = PdfReader(f)
    raw = ''
    for i in range(len(reader.pages)):
        raw += reader.pages[i].extract_text()
        
tokens = nltk.word_tokenize(raw)
tokens = [token for token in tokens if token not in stopwords]
tokens = [stemmer.stem(token) for token in tokens]
tokens = [lemmatizer.lemmatize(token) for token in tokens]

print(tokens)

                
             
