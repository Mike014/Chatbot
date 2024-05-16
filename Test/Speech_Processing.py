# -*- coding: utf-8 -*-
import speech_recognition as sr
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from googletrans import Translator
from nltk.corpus import wordnet

lemmatizer = WordNetLemmatizer()
stopwords = set(stopwords.words('english'))

r = sr.Recognizer()
translator = Translator()

def lemmatize(word):
    lemma = lemmatizer.lemmatize(word, pos='v')  # Verbs
    if lemma == word:
        lemma = lemmatizer.lemmatize(word, pos='n')  # Nouns
    if lemma == word:
        lemma = lemmatizer.lemmatize(word, pos='a')  # Adjectives
    return lemma

try:
    with sr.Microphone() as source:
        print("D\xEC qualcosa!")
        while True: 
            audio = r.record(source, duration=10)
            print("Registrazione terminata.")
            
            text = r.recognize_google(audio, language='it-IT')
            print("Hai detto: " + text)

            translated = translator.translate(text, src='it', dest='en')
            print("In inglese: " + translated.text)

            tokens = nltk.word_tokenize(translated.text)
            tokens = [token for token in tokens if token not in stopwords]
            tokens = [lemmatize(token) for token in tokens] 

            freq_dist = nltk.FreqDist(tokens)

            for word, freq in freq_dist.items():
                print(f'{word}: {freq}')
except Exception as e:
    print("Si \xe8 verificato un errore:", str(e))
    




    
   




