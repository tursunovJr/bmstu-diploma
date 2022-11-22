import cv2 as cv
import numpy as np
from matplotlib import cm, colors, pyplot as plt
from scipy import signal

img = cv.imread('fake.jpeg',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))

# b, a = signal.butter(8, 0.2, 'lowpass')   # Конфигурационный фильтр 8 указывает порядок фильтра

# filtedData = signal.filtfilt(b, a, magnitude_spectrum[int(len(magnitude_spectrum)/2)])  # данные - это сигнал, который нужно отфильтровать
filtedData = magnitude_spectrum[int(len(magnitude_spectrum)/2)]

plt.rcParams["figure.autolayout"] = True
fig, axs = plt.subplots()
# Fs = 1/00.1
axs.set_title("Fake image")
axs.magnitude_spectrum(filtedData, color='C1')

plt.show()