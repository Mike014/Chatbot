# -*- coding: utf-8 -*-

# Import standard libraries
import sys
import time
import speech_recognition as sr

# Add paths for custom modules
sys.path.append('c:\\users\\pc\\source\\repos\\chatbot\\chatbot\\dsp')
sys.path.append("c:\\users\\pc\\source\\repos\\chatbot\\chatbot\\nltk")

# Import custom modules
from Audio_Input import AudioInput
from AdvancedFourier import FFT
from Tokenizing_Words import Tokenizer
from Text_Classification import TextClassification

class VoiceRecognition:
    def __init__(self):
        self.audio_input = AudioInput()
        self.tokenizer = Tokenizer()
        self.text_classification = TextClassification()
        self.recognizer = sr.Recognizer()

        train_set, test_set = self.text_classification.split_data()
        self.text_classification.train_model(train_set)

    def recognize(self):
        self.audio_input.start_recording()
        time.sleep(self.audio_input.record_seconds)  
        audio_data = self.audio_input.stop_recording()

        audio_data = audio_data.flatten() 
        fft_data = FFT(audio_data)

        self.tokenizer.set_text(str(fft_data))
        words = self.tokenizer.tokenize_word()

        if self.text_classification is not None: 
            info = self.text_classification.classify(words)
        else:
            info = "error: text_classification is none"

        return info

    def audio_to_text(self):
        with sr.AudioFile(self.audio_input.filename) as source:
            audio = self.recognizer.record(source)
        try:
            print("recognizing...")
            return self.recognizer.recognize_google(audio, language='it-IT')
        except sr.UnknownValueError:
            return "could not understand audio"
        except sr.RequestError as e:
            return "could not request results; {0}".format(e)

if __name__ == '__main__':
    voice_recognition = VoiceRecognition()
    recognized_audio = voice_recognition.recognize()
    print("Recognized audio: ", recognized_audio)
    audio_to_text = voice_recognition.audio_to_text()
    print("Audio to text: ", audio_to_text)
    




