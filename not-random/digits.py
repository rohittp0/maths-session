import random
import csv

import numpy as np
import matplotlib.pyplot as plt


def count_digits(nums):
    count = [0] * 10
    for no in nums:
        for digit in str(no):
            count[int(digit)] += 1

    return count


human_input = [347453785684687467946945796976595355673567835654735673]
phone_numbers = np.ndarray.flatten(np.array([*csv.reader(open("phones.csv"))]))
random_numbers = [random.randint(0, 1_000_000) for i in range(100)]
natural_numbers = [*range(1500)]

p, ((a1, a2), (a3, a4)) = plt.subplots(2, 2)

a1.bar(range(10), count_digits(human_input))
a1.set_title("Human")

a2.bar(range(10), count_digits(phone_numbers))
a2.set_title("Phone Numbers")

a3.bar(range(10), count_digits(random_numbers))
a3.set_title("Random")

a4.bar(range(10), count_digits(natural_numbers))
a4.set_title("Natural Numbers")

p.tight_layout()
p.show()
