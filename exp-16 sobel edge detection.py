import cv2
import numpy as np
image = cv2.imread("image.jpg")
if image is None:
    print("Error: Could not load image.")
    exit()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
sobel_x = cv2.convertScaleAbs(sobel_x)
sobel_y = cv2.convertScaleAbs(sobel_y)
sobel_combined = cv2.magnitude(
    sobel_x.astype(np.float32),
    sobel_y.astype(np.float32)
)
sobel_combined = cv2.convertScaleAbs(sobel_combined)
cv2.imshow("Original Image", image)
cv2.imshow("Sobel X (Horizontal Edges)", sobel_x)
cv2.imshow("Sobel Y (Vertical Edges)", sobel_y)
cv2.imshow("Sobel Combined (Gradient Magnitude)", sobel_combined)
cv2.imwrite("sobel_x.jpg", sobel_x)
cv2.imwrite("sobel_y.jpg", sobel_y)
cv2.imwrite("sobel_combined.jpg", sobel_combined)
cv2.waitKey(0)
cv2.destroyAllWindows()