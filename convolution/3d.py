import numpy as np
from matplotlib.image import imread
import matplotlib.pyplot as plt
from scipy import signal

kernel = np.array([[[-7] * 3, [4] * 3, [-11] * 3],
                   [[0] * 3, [6]*3, [10] * 3],
                   [[5] * 3, [8] * 3, [3] * 3]
                   ])

image = imread('image.png')

cvt = signal.convolve(image, kernel, mode='same')
cvt = (cvt - np.min(cvt)) / (np.max(cvt) - np.min(cvt))

fig, (ax_orig, ax_mag) = plt.subplots(1, 2)
ax_orig.imshow(image)
ax_orig.set_title('Original')
ax_orig.set_axis_off()

ax_mag.imshow(cvt)
ax_mag.set_title('Output')
ax_mag.set_axis_off()

fig.show()
