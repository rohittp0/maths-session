import math
import random

import cv2
import numpy
import numpy as np


def print_result(title):
    print(title)
    print("Inside = ", inside)
    print("Outside = ", limit - inside)
    print("Total = ", limit)
    print("Fraction = ", inside / limit)
    print("Pi = ", inside / limit * 4, "\n")


img = numpy.ones((260, 260, 3), dtype=numpy.uint8) * 255

img = cv2.rectangle(img, (5, 5), (255, 255), (255, 0, 0), -1)
img = cv2.circle(img, (130, 130), 125, (0, 0, 255), -1)

limit = 10000

x_y = np.copy(img)
inside = 0

for i in range(limit):
    x = random.randint(5, 255)
    y = random.randint(5, 255)
    point = x, y
    x_y = cv2.circle(x_y, point, 1, (0, 255, 0), -1)

    if (point[0] - 130) ** 2 + (point[1] - 130) ** 2 < 125 ** 2:
        inside += 1

print_result("Random x and y coordinates")

r_th = np.copy(img)
inside = 0

for i in range(limit):
    r = random.randint(0, 250)
    th = math.radians(random.randint(0, 90))
    point = round(r * math.cos(th)) + 5, round(r * math.sin(th)) + 5

    if i % 2 == 0:
        point = 260 - point[0], 260 - point[1]

    r_th = cv2.circle(r_th, point, 1, (0, 255, 0), -1)

    if (point[0] - 130) ** 2 + (point[1] - 130) ** 2 < 125 ** 2:
        inside += 1

print_result("Random r and theta")

r_fn = np.copy(img)
inside = 0

for i in range(limit):
    x = i % 250 + 5
    y = random.randint(5, 255)
    point = x, y

    r_fn = cv2.circle(r_fn, point, 1, (0, 255, 0), -1)

    if (point[0] - 130) ** 2 + (point[1] - 130) ** 2 < 125 ** 2:
        inside += 1

print_result("Random function")

cv2.imshow("Random x and y", x_y)
cv2.imshow("Random r and theta", r_th)
cv2.imshow("Random function", r_fn)
cv2.waitKey()
