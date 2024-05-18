# -*- coding: utf-8 -*-

# Import standard libraries
import sys
import time
import joblib
import speech_recognition as sr
import threading  # Add this line

# Add paths for custom modules
sys.path.append('c:\\users\\pc\\source\\repos\\chatbot\\chatbot\\dsp')
sys.path.append("c:\\users\\pc\\source\\repos\\chatbot\\chatbot\\nltk")

# Import custom modules
from Audio_Input import AudioInput
from AdvancedFourier import FFT
from Tokenizing_Words import Tokenizer
from Text_Classification import TextClassification

class VoiceRecognition:
    def __init__(self, model, vectorizer):
        self.tokenizer = Tokenizer()
        self.text_classification = TextClassification(model, vectorizer)
        self.recognizer = sr.Recognizer()

        train_set, test_set = self.text_classification.split_data()
        self.text_classification.train_model(train_set)

    def recognize(self, audio_data):
        audio_data = audio_data.flatten() 
        fft_data = FFT(audio_data)

        self.tokenizer.set_text(str(fft_data))
        words = self.tokenizer.tokenize_word()

        if self.text_classification is not None: 
            info = self.text_classification.classify(words)
        else:
            info = "error: text_classification is none"

        return info

    def audio_to_text(self, filename):
        with sr.AudioFile(filename) as source:
            audio = self.recognizer.record(source)
        try:
            print("recognizing...")
            return self.recognizer.recognize_google(audio, language = 'en-US')
        except sr.UnknownValueError:
            return "could not understand audio"
        except sr.RequestError as e:
            return "could not request results; {0}".format(e)

# if __name__ == '__main__':
#     model = joblib.load('model.pkl')
#     vectorizer = joblib.load('vectorizer.pkl')
#     voice_recognition = VoiceRecognition(model, vectorizer)
#     audio_input = AudioInput()
#     done_event = threading.Event()  # Create an Event object
#     while True:
#         audio_input.start_recording(done_event)  # Pass the Event object
#         done_event.wait()  # Wait for the Event to be set
#         audio_data = audio_input.stop_recording()
#         recognized_audio = voice_recognition.recognize(audio_data)
#         print("Recognized audio: ", recognized_audio)
#         audio_to_text = voice_recognition.audio_to_text(audio_input.filename)
#         print("Audio to text: ", audio_to_text)
#         time.sleep(1)  # Wait for 1 second before starting the next recording
    
    
    
    
      
    
    




