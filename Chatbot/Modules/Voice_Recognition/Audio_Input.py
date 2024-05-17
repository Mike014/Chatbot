import pyaudio
import wave
import numpy as np
import sys
sys.path.append('C:\\Users\\PC\\source\\repos\\Chatbot\\Chatbot\\DSP')
from AdvancedFourier import FFT

class AudioInput:
    def __init__(self, filename="output.wav", rate=44100, chunk=1024, record_seconds=3):
        self.filename = filename
        self.rate = rate
        self.chunk = chunk
        self.record_seconds = record_seconds
        self.p = pyaudio.PyAudio()
        self.frames = []
        self.stream = None

    def start_recording(self):
        self.stream = self.p.open(format=pyaudio.paInt16,
                                  channels=1,
                                  rate=self.rate,
                                  input=True,
                                  frames_per_buffer=self.chunk)

        print("Start recording...")

    def stop_recording(self):
        print("Stop Recording...")

        for i in range(0, int(self.rate / self.chunk * self.record_seconds)):
            data = self.stream.read(self.chunk)
            self.frames.append(data)

        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

        wf = wave.open(self.filename, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(self.p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(self.rate)
        wf.writeframes(b''.join(self.frames))
        wf.close()
        return self.get_audio_data()

    def get_audio_data(self):
        audio_data = np.frombuffer(b''.join(self.frames), dtype=np.int16)
        return audio_data

    def get_fourier_transform(self):
        audio_data = self.get_audio_data()
        fourier_transform = FFT(audio_data)
        return fourier_transform
    
# if __name__ == '__main__':
#     audio_input = AudioInput()
#     audio_input.start_recording()
#     audio_input.stop_recording()
#     print(audio_input.get_fourier_transform())


    