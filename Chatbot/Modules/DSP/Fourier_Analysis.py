import numpy as np
from math import gcd

def compute_exponential(N, inverse=False):
    """
    Compute the complex exponential for DFT or IDFT

    Parameters:
    N (int): The length of the signal
    inverse (bool): Whether to compute the exponential for the DFT (False) or IDFT (True)

    Returns:
    e (numpy array): The computed complex exponential
    """
    n = np.arange(N)
    k = n.reshape((N, 1))
    if inverse:
        return np.exp(1j * 2 * np.pi * k * n / N)
    else:
        return np.exp(-2j * np.pi * k * n / N)
    
def DFT(x):
    """
    Compute the Discrete Fourier Transform of a signal

    Parameters:
    x (numpy array): The input signal

    Returns:
    X (numpy array): The DFT of the signal
    """
    N = len(x)
    e = compute_exponential(N)
    return np.dot(e, x)

def IDFT(X):
    """
    Compute the Inverse Discrete Fourier Transform of a spectrum

    Parameters:
    X (numpy array): The input spectrum

    Returns:
    x (numpy array): The IDFT of the spectrum
    """
    N = len(X)
    e = compute_exponential(N, inverse=True)
    return np.dot(e, X) / N

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

def FFT(x, real=False):
    """
    Compute the Fast Fourier Transform of the signal.

    Parameters:
    x (numpy array): The input signal
    real (bool): Whether the signal is real. If True, compute only half of the FFT.

    Returns:
    X (numpy array): The FFT of the signal
    """
    if real:
        X = np.fft.rfft(x)
    else:
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
    
    # Ensure x and h have the same length
    N = max(len(x), len(h))
    x = zero_padding(x, N)
    h = zero_padding(h, N)
    
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

    T = (round(T1) * round(T2)) / gcd(round(T1), round(T2))

    n = np.arange(int(T))
    x1 = A1 * np.cos(2 * np.pi * f1 * n / fs)
    x2 = A2 * np.cos(2 * np.pi * f2 * n / fs)

    x = x1 + x2

    X = DFT(x)

    return X

# if __name__ == '__main__':
#     x = np.array([1, 2, 3, 4])
#     X = DFT(x)
#     print(X)
#     x_reconstructed = IDFT(X)
#     print(x_reconstructed)
#     energy_time, energy_freq = energy_conservation(x)
#     print(energy_time, energy_freq)
#     X_db = amplitude_in_decibels(X)
#     print(X_db)
#     X_unwrapped = phase_unwrapping(X)
#     print(X_unwrapped)
#     is_real, is_even = verify_symmetry(x)
#     print(is_real, is_even)
#     h = np.array([0.5, 0.5])
#     y = apply_filter(x, h)
#     print(y)
#     X = FFT_zero_padding(x)
#     print(X)
#     x1 = np.array([1, 2, 3, 4])
#     x2 = np.array([5, 6, 7, 8])
#     y = apply_linearity(x1, x2, 2, 3)
#     print(y)
#     X = apply_shift(x, 2)
#     print(X)
#     X_real, X_imag, X_mag, X_phase = apply_symmetry(x)
#     print(X_real, X_imag, X_mag, X_phase)
#     x1 = np.array([1, 2, 3, 4])
#     x2 = np.array([5, 6, 7, 8])
#     X = apply_convolution(x1, x2)
#     print(X)
#     X = minimize_energy_spread(1, 10, 2, 20, 100, 1)
#     print(X)


