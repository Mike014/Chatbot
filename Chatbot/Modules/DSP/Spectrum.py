import numpy as np
from AdvancedFourier import FFT

def genMagnitudeSpectrum(x):
    """
    Generate the magnitude spectrum of a signal.

    Parameters:
    x (numpy array): The input signal

    Returns:
    X_mag (numpy array): The magnitude spectrum of the signal
    """
    X = FFT(x)
    X_mag = np.abs(X)
    return X_mag
