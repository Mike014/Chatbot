import numpy as np
import matplotlib.pyplot as plt
from pydub import AudioSegment
from pydub.playback import play
from Fourier_Analysis import FFT, zero_padding, IDFT

def generate_gaussian_noise(duration, sample_rate=44100, mean=0, std_dev=1):
    n_samples = int(duration * sample_rate)
    return np.random.normal(mean, std_dev, n_samples)

def generate_pink_noise(duration, sample_rate=44100):
    n_samples = int(duration * sample_rate)
    # Generate white noise
    white_noise = generate_gaussian_noise(duration, sample_rate)
    # Compute the FFT of the white noise
    white_noise_freq = FFT(white_noise, real=True)
    # Generate the pink filter
    frequencies = np.fft.rfftfreq(n_samples)
    pink_filter = 1 / np.sqrt(frequencies[1:])
    pink_filter = np.concatenate(
        ([0], pink_filter, np.zeros(n_samples // 2 - len(pink_filter)))
    )
    # Apply the pink filter to the white noise in frequency domain
    pink_noise_freq = white_noise_freq * pink_filter
    # Convert back to time domain using the inverse FFT
    pink_noise = np.fft.irfft(pink_noise_freq)
    pink_noise /= np.max(np.abs(pink_noise))
    return pink_noise  # np.fft.irfft always returns real output

def generate_brown_noise(duration, sample_rate=44100):
    n_samples = int(duration * sample_rate)
    # Generate white noise
    white_noise = generate_gaussian_noise(duration, sample_rate)
    # Compute the FFT of the white noise
    white_noise_freq = FFT(white_noise, real=True)
    # Generate the brown filter
    frequencies = np.fft.rfftfreq(n_samples)
    frequencies[0] = 1e-10  # Avoid division by zero
    brown_filter = 1 / frequencies
    brown_filter[0] = 0  # Set the first element to zero to avoid infinity
    # Apply the brown filter to the white noise in frequency domain
    brown_noise_freq = white_noise_freq * brown_filter
    # Convert back to time domain using the inverse FFT
    brown_noise = np.fft.irfft(brown_noise_freq)
    # Normalize the signal to prevent clipping
    
    return brown_noise  # np.fft.irfft always returns real output

def generate_uncorrelated_uniform_noise(duration, sample_rate=44100, low=-1, high=1):
    n_samples = int(duration * sample_rate)
    return np.random.uniform(low, high, n_samples)

# if __name__ == "__main__":
#     # Generate pink noise
#     duration = 5  # seconds
#     pink_noise = generate_brown_noise(duration)
#     # Normalize the signal to prevent clipping
#     pink_noise /= np.max(np.abs(pink_noise))
#     # Convert to 16-bit PCM WAV
#     pink_noise_wav = (pink_noise * 32767).astype(np.int16)
#     # Create an audio segment
#     audio_segment = AudioSegment(
#         pink_noise_wav.tobytes(), frame_rate=44100, sample_width=2, channels=1
#     )
#     # Play the audio segment
#     play(audio_segment)
#     # Plot the pink noise
#     plt.figure()
#     plt.plot(pink_noise)
#     plt.title("Pink Noise Signal")
#     plt.xlabel("Time (samples)")
#     plt.ylabel("Amplitude")
#     plt.show()
