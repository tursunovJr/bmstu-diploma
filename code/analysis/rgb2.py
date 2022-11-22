import cv2 as cv
import numpy as np
from matplotlib import cm, colors, pyplot as plt

img = cv.imread('fake.jpeg',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))
plt.subplot(121),plt.imshow(img)
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap='Greys')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()
