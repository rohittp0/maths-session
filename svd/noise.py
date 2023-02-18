import numpy as np
import cv2

# Load the image
img = cv2.imread('noise.webp', 0)
# flatten the image
# img = img.flatten()
# Calculate U (u), Σ (s) and V (vh)
u, s, vh = np.linalg.svd(img, full_matrices=False)
# Remove sigma values below threshold (250)
s_cleaned = np.array([si if si > 250 else 0 for si in s])
# Calculate A' = U * Σ (cleaned) * V
img = np.array(np.dot(u * s_cleaned, vh), dtype=int)

# convert the image to uint8
img = cv2.convertScaleAbs(img)

# Show the image using cv2
cv2.imshow('Deionised', img)
cv2.imshow('Original', cv2.imread('noise.webp', 0))
cv2.waitKey(0)
