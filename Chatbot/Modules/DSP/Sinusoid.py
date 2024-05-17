import numpy as np

def genSine(A, f, phi, fs, t):
    """
    Generate a real sinusoid given the amplitude, frequency, initial phase, sampling rate, and duration.

    Parameters:
    A (float): The amplitude of the sinusoid
    f (float): The frequency of the sinusoid in Hz
    phi (float): The initial phase of the sinusoid in radians
    fs (float): The sampling frequency of the sinusoid in Hz
    t (float): The duration of the sinusoid in seconds

    Returns:
    x (numpy array): The generated sinusoid
    """
    n = np.arange(fs * t)
    x = A * np.cos(2 * np.pi * f * n / fs + phi)
    return x

def genComplexSine(k, N):
    """
    Generate the complex sinusoid used in DFT computation.

    Parameters:
    k (int): The frequency index of the complex sinusoid
    N (int): The length of the complex sinusoid in samples

    Returns:
    cSine (numpy array): The generated complex sinusoid
    """
    n = np.arange(N)
    cSine = np.exp(-1j * 2 * np.pi * k * n / N)
    return cSine
