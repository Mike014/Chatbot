import numpy as np
from Fourier import DFT, IDFT

def energy_conservation(x):
    """
    Verify the energy conservation property of the DFT.

    Parameters:
    x (numpy array): The input signal

    Returns:
    energy_time (float): The energy of the signal in the time domain
    energy_freq (float): The energy of the signal in the frequency domain
    """

    energy_time = np.sum(np.abs(x)**2)

    X = DFT(x)

    energy_freq = np.sum(np.abs(X)**2) / len(X)
    return energy_time, energy_freq

def amplitude_in_decibels(X):
    """
    Convert the amplitude of the spectrum to decibels.

    Parameters:
    X (numpy array): The input spectrum

    Returns:
    X_db (numpy array): The spectrum in decibels
    """
    X_db = 20 * np.log10(np.abs(X))
    return X_db

def phase_unwrapping(X):
    """
    Unwrap the phase of the spectrum.

    Parameters:
    X (numpy array): The input spectrum

    Returns:
    X_unwrapped (numpy array): The unwrapped phase spectrum
    """
    X_unwrapped = np.unwrap(np.angle(X))
    return X_unwrapped

def zero_padding(x, N): 
    """
    Apply zero-padding to the signal.

    Parameters:
    x (numpy array): The input signal
    N (int): The total length of the signal after zero-padding

    Returns:
    x_padded (numpy array): The zero-padded signal
    """
    x_padded = np.pad(x, (0, N - len(x)))
    return x_padded

def FFT(x):
    """
    Compute the Fast Fourier Transform of the signal.

    Parameters:
    x (numpy array): The input signal

    Returns:
    X (numpy array): The FFT of the signal
    """
    X = np.fft.fft(x)
    return X

def apply_zero_phase_window(x, N):
    """
    Apply a zero-phase window to the signal.

    Parameters:
    x (numpy array): The input signal
    N (int): The length of the zero-phase window

    Returns:
    x_windowed (numpy array): The windowed signal
    """
    window = np.hanning(N)
    x_windowed = x * window
    return x_windowed

def analysis_synthesis(x):
    """
    Perform analysis and synthesis on the signal.

    Parameters:
    x (numpy array): The input signal

    Returns:
    y (numpy array): The reconstructed signal
    """
    X = FFT(x)
    y = np.fft.ifft(X)
    return np.real(y)

def optimal_zero_padding(x, f, fs):
    """
    Apply optimal zero-padding to the signal.

    Parameters:
    x (numpy array): The input signal
    f (float): The frequency of the signal in Hz
    fs (float): The sampling frequency in Hz

    Returns:
    X_padded (numpy array): The DFT of the zero-padded signal
    """
    
    T = fs / f

    N = int(np.ceil(len(x) / T) * T)
    
    x_padded = zero_padding(x, N)

    X_padded = DFT(x_padded)

    return X_padded

def verify_symmetry(x):
    """
    Verify the symmetry properties of the DFT for a real and even signal.

    Parameters:
    x (numpy array): The input signal

    Returns:
    is_real (bool): True if the signal is real, False otherwise
    is_even (bool): True if the signal is even, False otherwise
    """
    X = DFT(x)

    is_real = np.all(np.imag(X) == 0)

    is_even = np.all(X == X[::-1])

    return is_real, is_even

def apply_filter(x, h):
    """
    Apply a filter to the signal.

    Parameters:
    x (numpy array): The input signal
    h (numpy array): The filter

    Returns:
    y (numpy array): The filtered signal
    """
    
    X = DFT(x)
    H = DFT(h)
    
    Y = X * H

    y = IDFT(Y)

    return np.real(y)

def FFT_zero_padding(x):
    """
    Compute the FFT of the signal after zero-padding to a power of 2.

    Parameters:
    x (numpy array): The input signal

    Returns:
    X (numpy array): The FFT of the zero-padded signal
    """
    
    N = 2**np.ceil(np.log2(len(x)))

    x_padded = zero_padding(x, int(N))

    X = FFT(x_padded)

    return X
