
from winsound import PlaySound
import numpy as np
import scipy.signal as signal
from Sinusoid import genSine, genComplexSine
from Filters import butter_lowpass_filter
from scipy.signal import chirp
from pydub import AudioSegment
from pydub.playback import play
import matplotlib.pyplot as plt

def generate_harmonic_sound(frequencies, amplitudes, phi, fs, t):
    """
    Generate a harmonic sound signal given the frequencies, amplitudes, initial phase, sampling rate, and duration.

    Parameters:
    frequencies (list): The frequencies of the harmonics in Hz
    amplitudes (list): The amplitudes of the harmonics
    phi (float): The initial phase of the harmonics in radians
    fs (float): The sampling frequency of the harmonics in Hz
    t (float): The duration of the harmonics in seconds

    Returns:
    x (numpy array): The generated harmonic sound signal
    """
    x = np.zeros(int(fs * t))
    for f, A in zip(frequencies, amplitudes):
        x += A * genSine(1, f, phi, fs, t)
    return x

def generate_chord(frequencies, amplitudes, fs, t):
    """
    Generate a chord signal given the frequencies, amplitudes, sampling rate, and duration.

    Parameters:
    frequencies (list): The frequencies of the notes in Hz
    amplitudes (list): The amplitudes of the notes
    fs (float): The sampling frequency of the notes in Hz
    t (float): The duration of the notes in seconds

    Returns:
    x (numpy array): The generated chord signal
    """
    x = np.zeros(int(fs * t))
    for f, A in zip(frequencies, amplitudes):
        x += A * genSine(1, f, 0, fs, t)
    # Normalize the signal to prevent clipping
    x /= np.max(np.abs(x))
    return x

def generate_complex_chord(frequencies, amplitudes, fs, t):
    """
    Generate a complex chord signal given the frequencies, amplitudes, sampling rate, and duration.

    Parameters:
    frequencies (list): The frequencies of the notes in Hz
    amplitudes (list): The amplitudes of the notes
    fs (float): The sampling frequency of the notes in Hz
    t (float): The duration of the notes in seconds

    Returns:
    x (numpy array): The generated complex chord signal
    """
    x = np.zeros(int(fs * t))
    for f, A in zip(frequencies, amplitudes):
        x += A * genComplexSine(f, fs, t)
    # Normalize the signal to prevent clipping
    x /= np.max(np.abs(x))     
    return x

def generate_melody(frequencies, amplitudes, fs, t):
    """
    Generate a melody signal given the frequencies, amplitudes, sampling rate, and duration.

    Parameters:
    frequencies (list): The frequencies of the notes in Hz
    amplitudes (list): The amplitudes of the notes
    fs (float): The sampling frequency of the notes in Hz
    t (float): The duration of the notes in seconds

    Returns:
    x (numpy array): The generated melody signal
    """
    
    # if not isinstance(frequencies, list) or not isinstance(amplitudes, list):
    #     raise ValueError("Frequencies and amplitudes must be lists.")
        
    x = np.zeros(int(fs * t))
    for f, A in zip(frequencies, amplitudes):
        x += A * genSine(1, f, 0, fs, t)
    # Normalize the signal to prevent clipping
    x /= np.max(np.abs(x))
    return x

def generate_melody_(amplitude, frequency, fs, t):
    t = np.arange(fs*t)
    wave = amplitude * np.sin(2 * np.pi * frequency * t / fs)
    wave /= np.max(np.abs(wave))
    return wave
    
def generate_complex_melody(frequencies, amplitudes, fs, t):
    """
    Generate a complex melody signal given the frequencies, amplitudes, sampling rate, and duration.

    Parameters:
    frequencies (list): The frequencies of the notes in Hz
    amplitudes (list): The amplitudes of the notes
    fs (float): The sampling frequency of the notes in Hz
    t (float): The duration of the notes in seconds

    Returns:
    x (numpy array): The generated complex melody signal
    """
    x = np.zeros(int(fs * t))
    for f, A in zip(frequencies, amplitudes):
        x += A * genComplexSine(f, fs)  # Removed 't' from here
    # Normalize the signal to prevent clipping
    x /= np.max(np.abs(x))    
    return x

def generate_chirp(f0, f1, t, method='linear', fs=48000):
    """
    Generate a chirp signal.

    Parameters:
    f0 (float): The frequency of the signal at time=0.
    f1 (float): The frequency of the signal at time=t.
    t (float): The duration of the signal in seconds.
    method (str): The method of frequency variation ('linear', 'quadratic', 'logarithmic').
    fs (float): The sampling frequency of the signal in Hz.

    Returns:
    x (numpy array): The generated chirp signal.
    """
    times = np.linspace(0, t, int(fs * t), endpoint=False)
    x = chirp(times, f0, t, f1, method=method)
    # Normalize the signal to prevent clipping
    x /= np.max(np.abs(x))
    return x

def generate_sine_wave(frequency, amplitude, fs, t):
    """
    Generate a sine wave signal given the frequency, amplitude, sampling rate, and duration.

    Parameters:
    frequency (float): The frequency of the sine wave in Hz
    amplitude (float): The amplitude of the sine wave
    fs (float): The sampling frequency of the sine wave in Hz
    t (float): The duration of the sine wave in seconds

    Returns:
    x (numpy array): The generated sine wave signal
    """
    samples = np.arange(fs * t)
    x = amplitude * np.sin(2 * np.pi * frequency * samples / fs)
    return x

def generate_square_wave(frequency, amplitude, fs, t):
    """
    Generate a square wave signal given the frequency, amplitude, sampling rate, and duration.

    Parameters:
    frequency (float): The frequency of the square wave in Hz
    amplitude (float): The amplitude of the square wave
    fs (float): The sampling frequency of the square wave in Hz
    t (float): The duration of the square wave in seconds

    Returns:
    x (numpy array): The generated square wave signal
    """
    samples = np.arange(fs * t)
    x = amplitude * signal.square(2 * np.pi * frequency * samples / fs)
    return x

def generate_sawtooth_wave(frequency, amplitude, fs, t):
    """
    Generate a sawtooth wave signal given the frequency, amplitude, sampling rate, and duration.

    Parameters:
    frequency (float): The frequency of the sawtooth wave in Hz
    amplitude (float): The amplitude of the sawtooth wave
    fs (float): The sampling frequency of the sawtooth wave in Hz
    t (float): The duration of the sawtooth wave in seconds

    Returns:
    x (numpy array): The generated sawtooth wave signal
    """
    samples = np.arange(fs * t)
    x = amplitude * signal.sawtooth(2 * np.pi * frequency * samples / fs)
    return x

def generate_triangle_wave(frequency, amplitude, fs, t):
    """
    Generate a triangle wave signal given the frequency, amplitude, sampling rate, and duration.

    Parameters:
    frequency (float): The frequency of the triangle wave in Hz
    amplitude (float): The amplitude of the triangle wave
    fs (float): The sampling frequency of the triangle wave in Hz
    t (float): The duration of the triangle wave in seconds

    Returns:
    x (numpy array): The generated triangle wave signal
    """
    samples = np.arange(fs * t)
    x = amplitude * signal.sawtooth(2 * np.pi * frequency * samples / fs, width=0.5)
    return x

# test generate_melody a play it
if __name__ == "__main__":
    frequencies = [440, 493.88, 523.25, 587.33, 659.25, 698.46, 783.99, 880]
    amplitudes = [1, 1, 1, 1, 1, 1, 1, 1]
    fs = 44100
    t = 2
    melody = generate_melody(frequencies, amplitudes, fs, t)
    play_audio(melody, fs)
    plt.plot(melody[:44100])
    plt.show()

    










    

    








    

