import cv2
import numpy as np
import pywt

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Haar wavelet transform
    coeffs = pywt.dwt2(gray, 'haar')
    cA, (cH, cV, cD) = coeffs

    # Threshold the horizontal and vertical detail coefficients
    cH[np.abs(cH) < 30] = 0
    cV[np.abs(cV) < 30] = 0

    # Inverse wavelet transform to get edge map
    edge_map = pywt.idwt2((cA, (cH, cV, cD)), 'haar')

    # Threshold the edge map to remove noise
    edge_map[edge_map < 100] = 0

    # Display the edge map
    cv2.imshow('Edge Map', edge_map)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
