import pyaudio
import wave
import time
import threading
import numpy as np
import sys
sys.path.append('C:\\Users\\PC\\source\\repos\\Chatbot\\Chatbot\\DSP')
from AdvancedFourier import FFT

class AudioInput:
    def __init__(self, filename="output.wav", rate=44100, chunk=1024, record_seconds=7):
        self.filename = filename
        self.rate = rate
        self.chunk = chunk
        self.record_seconds = record_seconds
        self.p = pyaudio.PyAudio()
        self.frames = []
        self.stream = None

    def start_recording(self, done_event):
        self.p = pyaudio.PyAudio()
        try:
            self.stream = self.p.open(format=pyaudio.paInt16,
                                  channels=1,
                                  rate=self.rate,
                                  input=True,
                                  frames_per_buffer=self.chunk)
            print("Start recording...")
            threading.Thread(target=self.record, args=(done_event,)).start()
        except OSError as e:
            print("Error: ", e)
            return None
    
    def record(self, done_event):
        for i in range(0, int(self.rate / self.chunk * self.record_seconds)): # Loop through the audio data
            data = self.stream.read(self.chunk) # Read the audio data
            self.frames.append(data) # Append the audio data to the frames list
        done_event.set() # Set the Event object to signal that the recording is done
        done_event.clear() # Clear the Event object
            
    def stop_recording(self):
        print("Stop Recording...")
        
        if self.stream is None:
            print("Error: stream is None")
            return None
        
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
        
        wf = wave.open(self.filename, 'wb') # Open the WAV file
        wf.setnchannels(1) # Set the number of channels
        wf.setsampwidth(self.p.get_sample_size(pyaudio.paInt16)) # Set the sample width
        wf.setframerate(self.rate) # Set the frame rate
        wf.writeframes(b''.join(self.frames)) # Write the frames to the WAV file
        wf.close() # Close the WAV file
        return self.get_audio_data() # Return the audio data
        
    def get_audio_data(self):
        audio_data = np.frombuffer(b''.join(self.frames), dtype=np.int16) # Convert the frames to a NumPy array
        return audio_data

    def get_fourier_transform(self):
        audio_data = self.get_audio_data()
        fourier_transform = FFT(audio_data)
        return fourier_transform
    
# if __name__ == '__main__':
#     audio_input = AudioInput()
#     done_event = threading.Event()  # Create an Event object
#     audio_input.start_recording(done_event)  # Pass the Event object to start_recording
#     time.sleep(7)  # Wait for 7 seconds
#     audio_input.stop_recording()
#     print(audio_input.get_fourier_transform())


      