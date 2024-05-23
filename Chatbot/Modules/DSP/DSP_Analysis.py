import numpy as np
from STFT import compute_stft, compute_istft
import matplotlib.pyplot as plt
from Fourier_Analysis import FFT, apply_zero_phase_window, analysis_synthesis, apply_filter

def compute_odf(x, fs, window, nperseg, noverlap):
    """
    Compute the onset detection function of a signal.

    Parameters:
    x (numpy array): The input signal
    fs (float): The sampling frequency in Hz
    window (str or tuple or array_like): Desired window to use
    nperseg (int): Length of each segment
    noverlap (int): Number of points to overlap between segments

    Returns:
    odf (numpy array): The onset detection function
    """
    f, t, Zxx = compute_stft(x, fs, window, nperseg, noverlap)
    odf = np.sum(np.abs(Zxx), axis=0)
    return odf

def extract_main_lobe(x, fs, window, nperseg):
    """
    Extract the main lobe of the magnitude spectrum of a window.

    Parameters:
    x (numpy array): The input signal
    fs (float): The sampling frequency in Hz
    window (str or tuple or array_like): Desired window to use
    nperseg (int): Length of each segment

    Returns:
    main_lobe (numpy array): The main lobe of the magnitude spectrum
    """
    # Compute FFT
    X = FFT(x)

    # Compute magnitude spectrum
    mag_spectrum = np.abs(X)
    
    # Extract main lobe
    main_lobe = mag_spectrum[:nperseg//2]
    
    return main_lobe

def compute_snr(original, reconstructed):
    """
    Compute the Signal-to-Noise Ratio (SNR) between the original and reconstructed signals.

    Parameters:
    original (numpy array): The original signal
    reconstructed (numpy array): The reconstructed signal

    Returns:
    snr (float): The Signal-to-Noise Ratio in dB
    """
    # Compute the power of the original signal
    power_original = np.sum(original**2)
    
    # Compute the power of the noise
    noise = original - reconstructed
    power_noise = np.sum(noise**2)
    
    # Compute the Signal-to-Noise Ratio (SNR) in dB
    snr = 10 * np.log10(power_original / power_noise)
    
    return snr

def compute_spectrum(x):
    """
    Compute the magnitude spectrum of a signal.

    Parameters:
    x (numpy array): The input signal

    Returns:
    spectrum (numpy array): The magnitude spectrum of the signal
    """
    # Compute FFT
    X = FFT(x)
    
    # Compute magnitude spectrum
    spectrum = np.abs(X)
    
    return spectrum

def apply_window(x, N):
    """
    Apply a zero-phase window to the signal.

    Parameters:
    x (numpy array): The input signal
    N (int): The length of the zero-phase window

    Returns:
    x_windowed (numpy array): The windowed signal
    """
    x_windowed = apply_zero_phase_window(x, N)
    return x_windowed

def filter_signal(x, h):
    """
    Apply a filter to the signal.

    Parameters:
    x (numpy array): The input signal
    h (numpy array): The filter

    Returns:
    y (numpy array): The filtered signal
    """
    y = apply_filter(x, h)
    return y

def compute_correlation(signal1, signal2):
    """
    Compute the correlation between two signals.

    Parameters:
    signal1 (numpy array): The first signal
    signal2 (numpy array): The second signal

    Returns:
    correlation (float): The correlation between the two signals
    """
    return np.correlate(signal1, signal2, mode='same')

def compute_serial_correlation(signal, lag=1):
    """
    Compute the serial correlation of a signal at a given lag.

    Parameters:
    signal (numpy array): The input signal
    lag (int): The lag at which to compute the correlation

    Returns:
    correlation (float): The serial correlation at the given lag
    """
    return np.correlate(signal[:-lag], signal[lag:], mode='valid')

def compute_autocorrelation(signal):
    """
    Compute the autocorrelation of a signal.

    Parameters:
    signal (numpy array): The input signal

    Returns:
    autocorrelation (numpy array): The autocorrelation of the signal
    """
    return np.correlate(signal, signal, mode='full')
    











