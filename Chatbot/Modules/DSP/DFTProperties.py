import numpy as np
from fractions import gcd
from Fourier import DFT, IDFT

def apply_linearity(x1, x2, a, b):
    """
    Apply the property of linearity to two signals.
    
    Parameters:
    x1 (numpy array): The first input signal
    x2 (numpy array): The second input signal
    a (float): The scaling factor for the first signal
    b (float): The scaling factor for the second signal
    
    Returns:
    y (numpy array): The output signal after applying linearity
    """
    y = a * x1 + b * x2
    return y

def apply_shift(x, n0):
    """
    Apply the shift property of the DFT to the signal x.

    Parameters:
    x (numpy array): The input signal
    n0 (int): The amount to shift the signal

    Returns:
    X (numpy array): The DFT of the shifted signal
    """
    x_shifted = np.roll(x, -n0)
    X = DFT(x_shifted)
    return X 

def apply_symmetry(x):
    """
    Apply the symmetry property of the DFT to the signal x.

    Parameters:
    x (numpy array): The input signal

    Returns:
    X (numpy array): The DFT of the signal with applied symmetry property
    """
    X = DFT(x)
    X_real = np.real(X)
    X_imag = np.imag(X)
    X_mag = np.abs(X)
    X_phase = np.angle(X)
    return X_real, X_imag, X_mag, X_phase

def apply_convolution(x1, x2):
    """
    Apply the convolution property of the DFT to the signals x1 and x2.

    Parameters:
    x1, x2 (numpy arrays): The input signals

    Returns:
    X (numpy array): The DFT of the convolution of x1 and x2
    """
    x = np.convolve(x1, x2, mode='same')
    X = DFT(x)
    return X

def minimize_energy_spread(A1, f1, A2, f2, fs, t):
    """
    Minimize the energy spread in the DFT of two sinusoids.

    Parameters:
    A1, A2 (float): The amplitudes of the sinusoids
    f1, f2 (float): The frequencies of the sinusoids in Hz
    fs (float): The sampling frequency in Hz
    t (float): The duration of the sinusoids in seconds

    Returns:
    X (numpy array): The DFT of the combined sinusoids
    """
    
    T1 = fs / f1
    T2 = fs / f2

    T = (T1 * T2) / gcd(T1, T2)

    n = np.arange(int(T))
    x1 = A1 * np.cos(2 * np.pi * f1 * n / fs)
    x2 = A2 * np.cos(2 * np.pi * f2 * n / fs)

    x = x1 + x2

    X = DFT(x)

    return X


