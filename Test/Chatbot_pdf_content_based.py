import speech_recognition as sr
from PyPDF2 import PdfReader
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

stopwords = set(stopwords.words('english'))
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

with open('D:\\Roba da autodidatta\\Musica\\Teoria e Armonia Musicale\\Hollywood Chord Progressions.pdf', 'rb') as f:
    reader = PdfReader(f)
    raw = ''
    for i in range(len(reader.pages)):
        raw += reader.pages[i].extract_text()
        
tokens = nltk.word_tokenize(raw)
tokens = [token for token in tokens if token not in stopwords]
tokens = [stemmer.stem(token) for token in tokens]
tokens = [lemmatizer.lemmatize(token) for token in tokens]

text = nltk.Text(tokens)

r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        
    try:
        question = r.recognize_google(audio)
        print("You said: " + question)
        
        if question.lower() == "stop":
            break
        
        keywords = nltk.word_tokenize(question)
        keywords = [stemmer.stem(keyword) for keyword in keywords if keyword not in stopwords]
        
        for keyword in keywords:
            text.concordance(keyword)
            
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
           
