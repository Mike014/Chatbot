import re
import sys
import numpy as np
import matplotlib.pyplot as plt
import pyaudio
import random
sys.path.append('C:\\Users\\PC\\source\\repos\\Chatbot\\Chatbot\\DSP')
sys.path.append('C:\\Users\\PC\\source\\repos\\Chatbot\\Chatbot\\Regex')

from Sinusoid import genSine
from Noise_Generation import generate_gaussian_noise
from Fourier_Analysis import DFT
from Sound_Synthesis import generate_melody_, generate_chord
from Regex_Search import RegexSearch
from Regex_Pattern import compile_and_search

chords = {
    "c major": [261.63, 329.63, 392.00],  # C, E, G
    "d minor": [293.66, 349.23, 440.00],  # D, F, A
    "e minor": [329.63, 392.00, 493.88],  # E, G, B
    "f major": [349.23, 440.00, 523.25],  # F, A, C
    "g major": [392.00, 493.88, 587.33],  # G, B, D
    "a minor": [440.00, 523.25, 659.25],  # A, C, E
    "b diminished": [493.88, 587.33, 698.46],  # B, D, F
}

notes = {
    "c": {"frequency": 261.63, "amplitude": 1.0},  # C
    "d": {"frequency": 293.66, "amplitude": 1.0},  # D
    "e": {"frequency": 329.63, "amplitude": 1.0},  # E
    "f": {"frequency": 349.23, "amplitude": 1.0},  # F
    "g": {"frequency": 392.00, "amplitude": 1.0},  # G
    "a": {"frequency": 440.00, "amplitude": 1.0},  # A
    "b": {"frequency": 493.88, "amplitude": 1.0},  # B
    "c#": {"frequency": 277.18, "amplitude": 1.0},  # C#
    "d#": {"frequency": 311.13, "amplitude": 1.0},  # D#
    "f#": {"frequency": 369.99, "amplitude": 1.0},  # F#
    "g#": {"frequency": 415.30, "amplitude": 1.0},  # G#
    "a#": {"frequency": 466.16, "amplitude": 1.0},  # A#    
}

def play_audio(wave, fs=48000):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=fs, output=True)
    stream.write(wave.astype(np.float32).tobytes())
    stream.stop_stream()
    stream.close()
    p.terminate()

class Soundbot:
    def __init__(self):
        self.intents = {
            'generate_sine': compile_and_search(r'generate sine with frequencies (\d+(?:,\d+)*) and amplitude (\d+) and duration (\d+)'),
            'generate_noise': compile_and_search(r'generate noise with duration (\d+)'),
            'apply_dft': compile_and_search(r'apply dft'),
            'generate_chord': compile_and_search(r'generate a chord of (\w+ \w+)'),
            'generate_melody': compile_and_search(r'generate a melody from (\w+) in (\w+) direction')
        }
       
    def generate_sine_intent(self, frequencies, amplitude, duration_sine):
        frequencies = list(map(int, frequencies.split(',')))
        if any(f <= 0 for f in frequencies) or amplitude <= 0:
            raise ValueError("Frequencies and amplitude must be positive.")
        sine_wave = sum(genSine(amplitude, f, 0, 44100, duration_sine) for f in frequencies)
        plt.plot(sine_wave[:44100])  # plot the first second of the signal
        plt.show()
        
        # Play the sine wave
        play_audio(sine_wave)
        return f"Sine wave generated with frequencies {frequencies} Hz, amplitude {amplitude} and duration {duration_sine} seconds"
    
    def generate_noise_intent(self, duration):
        if duration <= 0:
            raise ValueError("Duration must be positive.")
        noise = generate_gaussian_noise(duration)
        
        # Plot the first second of the signal
        plt.plot(noise[:44100])
        plt.show()
        
        # Play the noise
        play_audio(noise)
        
        return f"Noise generated with duration {duration} seconds"
    
    def apply_dft_intent(self):
        dft = DFT([0, 1, 0, -1])
        return f"DFT applied to the signal [0, 1, 0, -1]"

    def generate_chord_intent(self, chord):
        chord = chord.lower()  
        if chord not in chords:
            raise ValueError("Chord not found")
        frequencies = chords[chord]
        amplitudes = [0.6, 0.6, 0.6]  
        fs = 48000
        t = 3
        chord_wave = generate_chord(chords[chord], amplitudes, fs, t)
        # plt.plot(chord_wave[:44100])  # plot the first second of the signal
        # plt.show()
        
        # Play the chord
        play_audio(chord_wave, fs)

        return f"Chord {chord} generated"
     
    def generate_melody_intent(self, note, direction):
        fs = 48000  
        t = 1
        
        if note in notes:
            sorted_notes = sorted(notes, key=lambda x: notes[x]["frequency"])
            note_index = sorted_notes.index(note)
            if direction == "ascending":
                melody_notes = sorted_notes[note_index:]
            elif direction == "descending":
                melody_notes = sorted_notes[note_index::-1]
            else:
                raise ValueError("Direction must be 'ascending' or 'descending'.")
            melody_wave = np.array([])
            for _ in range(len(melody_notes)):
                note = random.choice(melody_notes)
                melody_notes.remove(note)  # remove the note from the list to avoid repeating it
                amplitude = notes[note]["amplitude"]
                frequency = notes[note]["frequency"]
                print(f"Generating {note} with frequency {frequency} Hz")
                melody_wave = np.append(melody_wave, generate_melody_(amplitude, frequency, fs, t))
            plt.plot(melody_wave[:44100])  # plot the first second of the signal   
            plt.show()
            
            play_audio(melody_wave, fs)  
            return f"Melody from {note} scale generated in {direction} direction"
        else:
            raise ValueError("Note not found")
        
    def match_reply(self, reply):
        for intent, pattern in self.intents.items():
            found_match = pattern.search(reply)
            if found_match:
                if intent == 'generate_sine':
                    frequencies = found_match.group(1)  
                    amplitude = int(found_match.group(2))  
                    duration_sine = int(found_match.group(3))
                    return self.generate_sine_intent(frequencies, amplitude, duration_sine)
                elif intent == 'generate_noise':
                    duration = int(found_match.group(1))
                    return self.generate_noise_intent(duration)
                elif intent == 'apply_dft':
                    return self.apply_dft_intent()
                elif intent == 'generate_chord':
                    chord = found_match.group(1)
                    return self.generate_chord_intent(chord)
                elif intent == 'generate_melody':
                    scale = found_match.group(1)
                    direction = found_match.group(2)
                    return self.generate_melody_intent(scale, direction)
        raise ValueError("I'm sorry, I'm not sure how to help you.")
                    
    def handle_conversation(self):
        try:
            while True:
                user_input = input("Generate a sound: ")
                if not isinstance(user_input, str):
                    raise TypeError("Please enter a valid string.")
                response = self.match_reply(user_input)
                print(response)
                if user_input == 'quit':
                    break
        except ValueError as e:
            print(f"ValueError: {e}")
        except TypeError as e:
            print(f"TypeError: {e}")

if __name__ == '__main__':
    bot = Soundbot()
    bot.handle_conversation()

