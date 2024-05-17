# -*- coding: utf-8 -*-

# Import standard libraries
import sys
import numpy as np
import matplotlib.pyplot as plt

# Add paths for custom modules
sys.path.append('C:\\Users\\PC\\source\\repos\\Chatbot\\Chatbot\\Voice_Recognition')
sys.path.append('C:\\Users\\PC\\source\\repos\\Chatbot\\Chatbot\\DSP')

# Import custom modules
from Voice_Recognition import VoiceRecognition
from Audio_Input import AudioInput
from AdvancedFourier import FFT, amplitude_in_decibels
from Spectrum import genMagnitudeSpectrum

# Function definitions
def generate_sinusoid():
    t = np.linspace(0, 1, 500, endpoint=False)
    y = np.sin(2 * np.pi * 5 * t)
    plt.plot(t, y)
    plt.show()

def main():
    # Crea un'istanza di VoiceRecognition
    voice_recognition = VoiceRecognition()

    # Riconosce l'audio
    recognized_audio = voice_recognition.recognize()
    print("Recognized audio: ", recognized_audio)

    # Converte l'audio in testo
    audio_to_text = voice_recognition.audio_to_text()
    print("Audio to text: ", audio_to_text)

    # Se il comando riconosciuto è "genera sinusoide", genera una sinusoide
    if audio_to_text == "test":
        generate_sinusoid()

    # Crea un'istanza di AudioInput
    audio_input = AudioInput()

    # Inizia la registrazione
    audio_input.start_recording()

    # Ferma la registrazione dopo 3 secondi e ottiene i dati audio
    audio_data = audio_input.stop_recording()

    # Ottiene la trasformata di Fourier dei dati audio
    fft_data = FFT(audio_data)

    # Converte l'ampiezza dello spettro in decibel e la stampa
    print("Amplitude in decibels: ", amplitude_in_decibels(fft_data))

    # Genera lo spettro di ampiezza dei dati audio e lo stampa
    print("Magnitude spectrum: ", genMagnitudeSpectrum(audio_data))

# Main script
if __name__ == "__main__":
    main()


