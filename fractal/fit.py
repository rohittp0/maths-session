import math
import random

from matplotlib import pyplot as plt

scales = [
    lambda x: (1/2)*math.sin(5*x) + 0.2,
    lambda x: (1/3)*math.cos(x),
    lambda x: (1/5)*math.exp(-2*x) + 0.2,
    lambda x: (1/5)*math.sin(x)*math.exp(x) + 0.1
]


def get_coefficients(n,d, x, y):
    del_x = (x[-1] - x[0])

    a = (x[n] - x[n-1]) / del_x
    e = (x[-1]*x[n-1] - x[0]*x[n]) / del_x
    c = (y[n] - y[n-1] - d*(y[-1] - y[0])) / del_x
    f = (x[-1]*y[n-1] - x[0]*y[n] - d*(x[-1]*y[0] - x[0]*y[-1])) / del_x

    return a, e, c, f


def main():
    x = [0, 1 / 3, 1 / 2, 3 / 4, 1]
    y = [1 / 5, 1 / 2, 1 / 3, 3 / 4, 1 / 2]

    coefficients = [get_coefficients(n, scales[n - 1](x[n]), x, y) for n in range(1, len(x))]

    point = (0, 0)
    # plt.axis([0, 100, 0, 100])
    plt.plot(x, y, "ro", markersize=2)

    for _ in range(1000):
        n = random.randint(0, len(x) - 2)

        a, e, c, f = get_coefficients(n, scales[n - 1](point[0]), x, y)
        point = (a * point[0] + e, c * point[0] + scales[n](point[0]) * point[1] + f)

        plt.plot(*point, '.', markersize=1)

    plt.show()


if __name__ == '__main__':
    main()
