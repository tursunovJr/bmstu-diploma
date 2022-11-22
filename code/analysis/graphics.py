import cv2 as cv
import numpy as np
from matplotlib import cm, colors, pyplot as plt
from statistics import mean 

img = cv.imread('099010.png',0)
# real_img = cv.imread('real3.jpeg',0)
# fake_img = cv.imread('fake3.png',0)

f = np.fft.fft2(img)
# f_real = np.fft.fft2(real_img)
# f_fake = np.fft.fft2(fake_img)

fshift = np.fft.fftshift(f)
# fshift_real = np.fft.fftshift(f_real)
# fshift_fake = np.fft.fftshift(f_fake)

magnitude_spectrum = 20*np.log(np.abs(fshift))
# magnitude_spectrum_real = 20*np.log(np.abs(fshift_real))
# magnitude_spectrum_fake = 20*np.log(np.abs(fshift_fake))


delta_real = mean(magnitude_spectrum[int(len(magnitude_spectrum)/2)])
# delta_fake = mean(magnitude_spectrum_fake[int(len(magnitude_spectrum_fake)/2)])

print("Delta Real = ", delta_real)
# print("Delta Fake = ", delta_fake)


sum = 0 
# sum_fake = 0

for i in magnitude_spectrum[int(len(magnitude_spectrum)/2)]:
    sum += abs(delta_real-i)
print("Относ Sum = ", sum/int(len(magnitude_spectrum[int(len(magnitude_spectrum)/2)])))
print("Sum = ", sum)
# print("Sum Fake = ", sum_fake/int(len(magnitude_spectrum_real[int(len(magnitude_spectrum_real)/2)])))


# plt.rcParams["figure.autolayout"] = True
# fig, axs = plt.subplots()
# Fs = 1/00.1
# axs.set_title("Magnitude Spectrum")
# axs.magnitude_spectrum(magnitude_spectrum[int(len(magnitude_spectrum)/2)], Fs=Fs, color='C1')

# plt.show()
