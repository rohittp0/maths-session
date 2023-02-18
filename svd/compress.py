import io

import cv2
import numpy as np
from scipy import misc
# Load image
img = cv2.imread('noise.webp', 0)
# Calculate U (u), Σ (s) and V (vh)
u, s, vh = np.linalg.svd(img, full_matrices=False)
# Remove sigma values below threshold (200)
s_cleaned = np.array([si if si > 200 else 0 for si in s])
# Calculate A' = U * Σ (cleaned) * V
img_compressed = np.array(np.dot(u * s_cleaned, vh), dtype=int)
# convert the image to uint8
img_compressed = cv2.convertScaleAbs(img_compressed)
# Show the image using cv2
cv2.imshow('Compressed', img_compressed)
cv2.imshow('Original', img)
cv2.waitKey(0)

# Compare the sizes of the images in kb
_, buffer = cv2.imencode(".jpg", img)
buffer = io.BytesIO(buffer)
print('Original image size: ', buffer.getbuffer().nbytes / 1024, 'kb')

_, buffer = cv2.imencode(".jpg", img_compressed)
buffer = io.BytesIO(buffer)
print('Compressed image size: ', buffer.getbuffer().nbytes / 1024, 'kb')
