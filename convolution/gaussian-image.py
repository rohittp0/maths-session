import cv2

img = cv2.imread("image.png")
blur = cv2.GaussianBlur(img, (9, 9), 8)

cv2.imshow("Original", img)
cv2.imshow("Blurred", blur)

cv2.waitKey()
