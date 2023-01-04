import numpy as np
from matplotlib.image import imread
import matplotlib.pyplot as plt
from scipy import signal

kernel = [[1, 0, -1],
          [1, 0, -1],
          [1, 0, -1]
          ]


def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])


image = imread('image.png')
image = rgb2gray(image)

cvt = signal.convolve2d(image, kernel, boundary='symm', mode='same') * 10

fig, (ax_orig, ax_mag) = plt.subplots(1, 2)
ax_orig.imshow(image, cmap='gray')
ax_orig.set_title('Original')
ax_orig.set_axis_off()

ax_mag.imshow(cvt, cmap='gray')
ax_mag.set_title('Output')
ax_mag.set_axis_off()

fig.tight_layout()
fig.show()
