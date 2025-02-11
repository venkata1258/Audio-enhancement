# -*- coding: utf-8 -*-
"""wavepad.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/107UzH8ughW3Uqa2nfPHRkqk3SU5auKDT
"""

!pip install librosa noisereduce matplotlib numpy scipy

# Import necessary modules
import librosa
import librosa.display
import noisereduce as nr
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from IPython.display import Audio

# Load the uploaded audio file
audio_path = "/content/mixkit-wildlife-environment-in-a-river-2456.wav"  # Path to the uploaded audio file
audio_data, sr = librosa.load(audio_path, sr=None)

# Display audio properties
print(f"Sample Rate: {sr}")
print(f"Duration: {librosa.get_duration(y=audio_data, sr=sr)} seconds")

# Play the original audio
print("Original Audio:")
display(Audio(audio_data, rate=sr))

# Visualize the original waveform
plt.figure(figsize=(14, 5))
librosa.display.waveshow(audio_data, sr=sr)
plt.title("Original Audio Waveform")
plt.show()

# Perform noise reduction
# Assuming the noise is constant throughout (adjust for your case)
reduced_noise = nr.reduce_noise(y=audio_data, sr=sr)

# Play the noise-reduced audio
print("Noise-Reduced Audio:")
display(Audio(reduced_noise, rate=sr))

# Visualize the noise-reduced waveform
plt.figure(figsize=(14, 5))
librosa.display.waveshow(reduced_noise, sr=sr)
plt.title("Noise-Reduced Audio Waveform")
plt.show()

# Save the noise-reduced audio as a WAV file
output_path = "/content/mixkit-wildlife-environment-in-a-river-2456.wav"
wavfile.write(output_path, sr, np.array(reduced_noise))
print(f"Noise-reduced audio saved as '{output_path}'")