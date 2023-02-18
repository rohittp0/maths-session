import matplotlib.pyplot as plt


def v_function():
    x = list(range(0, 50))
    y = [0] * 50
    y[10:20] = list(range(0, 10))
    y[20:30] = [10] * 10
    y[30:40] = list(range(10, 0, -1))

    return x, y


def convolution(y, kernel):
    # Padding using 0
    y = [0] * (len(kernel) - 1) + y + [0] * (len(kernel) - 1)
    y_conv = []

    for i in range(len(y) - len(kernel) + 1):
        y_conv.append(sum([y[i + j] * kernel[j] for j in range(len(kernel))]))

    return y_conv[(len(kernel)) // 2:(-len(kernel) + 1) // 2]


def main():
    x, y = v_function()

    kernel = [0.2, 0.2, 0.2, 0.2, 0.2]

    v_convoluted_1 = convolution(y, kernel)
    v_convoluted_2 = convolution(v_convoluted_1, kernel)
    v_convoluted_3 = convolution(v_convoluted_2, kernel)

    plt.plot(x, y)
    plt.show()

    plt.plot(x, v_convoluted_1)
    plt.show()

    plt.plot(x, v_convoluted_2)
    plt.show()

    plt.plot(x, v_convoluted_3)
    plt.show()


if __name__ == "__main__":
    main()
