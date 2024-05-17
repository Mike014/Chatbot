import nltk 
from nltk.tokenize import word_tokenize, sent_tokenize
from PyPDF2 import PdfReader

with open('D:\\Roba da autodidatta\\Musica\\Teoria e Armonia Musicale\\Hollywood Chord Progressions.pdf', 'rb') as file:
    reader = PdfReader(file)
    raw = ''
    for page in reader.pages:
        raw += page.extract_text()

tokens = nltk.word_tokenize(raw)
print(tokens)
words = [w.lower() for w in tokens]
print(words)
vocab = sorted(set(words))
print(vocab)







