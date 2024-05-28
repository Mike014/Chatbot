import re
import numpy as np
import matplotlib.pyplot as plt
from pydub import AudioSegment
from pydub.playback import play
import sys
# Add paths for custom modules
sys.path.append('C:\\Users\\PC\\source\\repos\\Chatbot\\Chatbot\\Voice_Recognition')
sys.path.append('C:\\Users\\PC\\source\\repos\\Chatbot\\Chatbot\\DSP')
from Sound_Synthesis import generate_sine_wave
from Filters import butter_lowpass_filter
from DSP_Analysis import compute_spectrum

class Main:
    def __init__(self):
        self.matching_phrases = {'create_reese_bass': [r'.*create.*reese bass.*', r'.*make.*reese bass.*']}
        self.fs = 96000  # Sampling frequency

    def create_reese_bass(self, frequency, duration):
        A = 0.2  # Amplitude
        # detune = 5 # Detuning amount in Hz for the "beating" effect
        # mod_index = 0.01  # Lower modulation index for less noise

        # # Generate the carrier and modulating signals
        # carrier = generate_sine_wave(frequency, A, self.fs, duration)
        # modulator1 = generate_sine_wave(frequency + detune, A, self.fs, duration)

        # # Apply FM synthesis
        # reese_bass = np.sin(2 * np.pi * self.fs * carrier + mod_index * (modulator1))

        # Apply a low-pass filter
        cutoff = 300  # Lower cutoff frequency for less noise
        order = 8  # Higher order for steeper roll-off
        # reese_bass = butter_lowpass_filter(reese_bass, cutoff, self.fs, order)
        
        sine_wave = generate_sine_wave(frequency, A, self.fs, duration)
        sine_wave_filtered = butter_lowpass_filter(sine_wave, cutoff, self.fs, order)
        sine_wave_filtered_array = np.array(sine_wave_filtered)

        return sine_wave_filtered_array

    def respond_to(self, user_input):
        for intent, patterns in self.matching_phrases.items():
            for pattern in patterns:
                if re.match(pattern, user_input):
                    if intent == 'create_reese_bass':
                        reese_bass = self.create_reese_bass(40, 3)  # Create a Reese Bass at 40 Hz for 3 seconds
                        spectrum = compute_spectrum(reese_bass)
                        spectrum_array = np.array(spectrum)
                        reese_bass_sound = AudioSegment(reese_bass, frame_rate=self.fs, sample_width=2, channels=1)
                      
                        plt.figure()
                        plt.plot(spectrum_array)
                        plt.title("Reese Bass Signal")
                        plt.xlabel("Time (samples)")
                        plt.ylabel("Amplitude")
                        plt.show()
                        
                        play(reese_bass_sound)
             
                        return "Creating and playing a Reese Bass."
        return "I'm sorry, I didn't understand that. Could you please rephrase?"

if __name__ == "__main__":
    main = Main()
    while True:
        user_input = input("Please enter a command: ")
        response = main.respond_to(user_input)
        print(response)
        assert response != "I'm sorry, I didn't understand that. Could you please rephrase?", "Invalid command."
        


