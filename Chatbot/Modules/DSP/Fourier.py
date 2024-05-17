import numpy as np

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