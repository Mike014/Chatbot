# -*- coding: utf-8 -*-
# Import standard libraries
import sys
from token import COMMA
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
import joblib
import time
import uuid
from pydub import AudioSegment
from pydub.playback import play
from pydub.utils import mediainfo
import re
import threading
import pygame  # Replace simpleaudio with pygame
from queue import Queue

# Add paths for custom modules
sys.path.append('C:\\Users\\PC\\source\\repos\\Chatbot\\Chatbot\\Voice_Recognition')
sys.path.append('C:\\Users\\PC\\source\\repos\\Chatbot\\Chatbot\\DSP')

# Import custom modules
from Voice_Recognition import VoiceRecognition
from Audio_Input import AudioInput
from AdvancedFourier import FFT, amplitude_in_decibels
from Spectrum import genMagnitudeSpectrum
from Tokenizing_Words import tokenize
from StopWords import RemoveStopWords
from Stemming import Stemmer
from Lemmatizing import lemmatize
from Sinusoid import genSine

# Initialize the pygame mixer
pygame.mixer.init()
duration = 3.# Duration in seconds 

# Initialize a queue to hold the audio files
audio_files = Queue()

# Function to generate a sinusoid
def generate_sinusoid(frequency):
    # Stop any previous audio
    pygame.mixer.music.stop()

    fs = 48000  # Sample rate
    t = np.linspace(0, duration, fs, endpoint=False)  # Time array
    y = genSine(0.5, frequency, 0, fs, duration)  # Generate sinusoid using genSine
    y = (y * 32767).astype(np.int16)  # Convert to int16
    plt.plot(t[:1000], y[:1000])  # Plot first 1000 samples
    plt.show()

    # Generate a unique filename
    filename = 'temp_{}.wav'.format(uuid.uuid4())

    # Write the audio data to a WAV file
    with open(filename, 'wb') as fid:
        write(fid, fs, y)
    
    # Add the filename to the queue
    audio_files.put(filename)

    # Load the WAV file into an AudioSegment
    audio = AudioSegment.from_wav(filename)
    
    # Get the duration of the audio in seconds
    audio_info = mediainfo(filename)
    audio_duration = float(audio_info['duration'])

    # Play the audio
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # Remove the filename from the queue
    audio_files.get()

# prepare_command with NLP techniques
def prepare_command(command):
    command = ' '.join(tokenize(command))
    command = ' '.join(RemoveStopWords(command).remove())
    command = ' '.join(Stemmer(command).stem())
    command = ' '.join(lemmatize(command))  
    return command

# Initialize a queue to hold the commands
commands = Queue()

# Main function
def main():
    # Load the model and vectorizer
    model = joblib.load('model.pkl')
    vectorizer = joblib.load('vectorizer.pkl')

    # Create an instance of VoiceRecognition
    voice_recognition = VoiceRecognition(model, vectorizer)

    # Create an instance of AudioInput
    audio_input = AudioInput()
    
    done_event = threading.Event()

    # Start a new recording
    audio_input.start_recording(done_event)
    done_event.wait()  # Wait for the recording to finish
    done_event.clear()  # Reset the Event object

    # Stop the recording after it has finished
    audio_data = audio_input.stop_recording()

    # Recognize the audio
    recognized_audio = voice_recognition.recognize(audio_data)
    print("Recognized audio: ", recognized_audio)
    
    if not recognized_audio or len(recognized_audio) == 0:
        print("No audio recognized")
        audio_input.stop_recording()  # Stop the recording if no audio was recognized
        return

    # Convert the audio to text
    audio_to_text = voice_recognition.audio_to_text(audio_input.filename)
    if audio_to_text == "could not understand audio" or audio_to_text == "could not request results":
        print(audio_to_text)
        audio_input.stop_recording()  # Stop the recording if the audio could not be converted to text
        return

    # Split the recognized text into separate commands
    commands_list = audio_to_text.split('generate sine')

    # Clear the queue and add the new commands to the queue
    commands.queue.clear()
    for command in commands_list:
        commands.put(command)

    command = commands.get()
    # Check if the command is empty
    if not command.strip():
        commands.task_done()

    # Prepare the command
    command = prepare_command(command)

    # Transform the command using the vectorizer
    command_vectorized = vectorizer.transform([command])

    # Use the model to make a prediction
    prediction = model.predict(command_vectorized)

    print("The prediction for the new command is: ", prediction)
    
    # Check the prediction
    while prediction[0] == 'generate_sine_wave':
        
        # Check if the queue is empty
        match = re.search(r'\d+', command)
        if match:
            frequency = int(match.group())
            pygame.mixer.music.stop()
            generate_sinusoid(frequency)
            print("Command: ", command)
            print("Match: ", match)
            print(list(commands.queue))
    
            commands.task_done()
            command = None 
            break

        else:
            print("Frequency not found in command")
            commands.task_done()
            commands.task_done()
    
    else:
        print("Command not recognized")
        if not commands.empty():
            command = commands.get()
            print("Next command: ", command)
            
    command = None
    
# Main script
if __name__ == "__main__":
    main()