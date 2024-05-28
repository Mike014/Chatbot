
import numpy as np
from scipy.signal import stft

def compute_stft(x, fs, window, nperseg, noverlap):
    """
    Compute the Short-Time Fourier Transform of a signal.

    Parameters:
    x (numpy array): The input signal
    fs (float): The sampling frequency in Hz
    window (str or tuple or array_like): Desired window to use
    nperseg (int): Length of each segment
    noverlap (int): Number of points to overlap between segments

    Returns:
    f (numpy array): Array of sample frequencies
    t (numpy array): Array of segment times
    Zxx (numpy array): STFT of x
    """
    f, t, Zxx = stft(x, fs, window, nperseg, noverlap)
    return f, t, Zxx

def compute_istft(Zxx, fs, window, nperseg, noverlap):
    """
    Compute the Inverse Short-Time Fourier Transform of a spectrum.

    Parameters:
    Zxx (numpy array): STFT of the input signal
    fs (float): The sampling frequency in Hz
    window (str or tuple or array_like): Desired window to use
    nperseg (int): Length of each segment
    noverlap (int): Number of points to overlap between segments

    Returns:
    t (numpy array): Array of output data times
    x (numpy array): iSTFT of Zxx
    """
    t, x = istft(Zxx, fs, window, nperseg, noverlap)
    return t, x