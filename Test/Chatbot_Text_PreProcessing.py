import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import speech_recognition as sr

# Initialize resources for text pre-processing
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# Initialize speech recognition
r = sr.Recognizer()

# Capture the input from the user
with sr.Microphone() as source:
    while True: 
        print("Listening for command...")
        audio = r.listen(source)
        
        text = "" 
        try:
            text = r.recognize_google(audio)
            print("You said " + text)
            break  
        except:
            print("Sorry, I didn't understand that. Please try again.")

# Preprocess the text
tokens = nltk.word_tokenize(text)
tokens = [token for token in tokens if token not in stop_words]
tokens = [stemmer.stem(token) for token in tokens]
tokens = [lemmatizer.lemmatize(token) for token in tokens]

print(tokens)
