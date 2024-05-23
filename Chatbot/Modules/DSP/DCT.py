import numpy as np
import matplotlib.pyplot as plt

def dct_iv(ys):
    """
    Compute the Type-IV Discrete Cosine Transform of a signal.

    Parameters:
    ys (numpy array): The input signal

    Returns:
    amps (numpy array): The DCT of the signal
    """
    N = len(ys)
    PI2 = np.pi * 2
    ts = (0.5 + np.arange(N)) / N
    fs = (0.5 + np.arange(N)) / 2
    args = np.outer(ts, fs)
    M = np.cos(PI2 * args)
    amps = np.dot(M, ys) / 2
    return amps

def inverse_dct_iv(amps):
    """
    Compute the inverse Type-IV Discrete Cosine Transform of a signal.

    Parameters:
    amps (numpy array): The DCT of the signal

    Returns:
    ys (numpy array): The inverse DCT of the signal
    """
    return dct_iv(amps) * 2

if __name__ == '__main__':
    x = np.array([1.0, 2.0, 3.0, 4.0])
    X = dct_iv(x)
    plt.figure()
    plt.plot(x, label='x')
    plt.plot(X, label='X')
    plt.legend()
    plt.show()
    y = inverse_dct_iv(X)
    plt.figure()
    plt.plot(x, label='x')
    plt.plot(y, label='y')
    plt.legend()
    plt.show()


    

    



    
