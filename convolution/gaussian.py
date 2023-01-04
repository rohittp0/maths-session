"""
f(x) = 1 / (sigma * sqrt(2 * pi)) * exp(-0.5 * (x - mu) / sigma)
"""

import numpy as np
import matplotlib.pyplot as plt


def gaussian_kernel(size, sigma):
    """
    :param size: int
    :param sigma: float
    :return: numpy.ndarray
    """
    x, y = np.mgrid[-size // 2 + 1:size // 2 + 1, -size // 2 + 1:size // 2 + 1]
    g = np.exp(-((x ** 2 + y ** 2) / (2.0 * sigma ** 2)))
    return g / g.sum()


kernel_5_1 = gaussian_kernel(5, 1)

plt.imshow(kernel_5_1, cmap='autumn', interpolation='nearest')
plt.show()

kernel_5_2 = gaussian_kernel(5, 2)

plt.imshow(kernel_5_2, cmap='autumn', interpolation='nearest')
plt.show()

kernel_5_3 = gaussian_kernel(5, 3)

plt.imshow(kernel_5_3, cmap='autumn', interpolation='nearest')
plt.show()
