import cv2
import numpy as np
image = cv2.imread("goku.jpg")
if image is None:
    print("Error: image not found")
    exit()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
kernel = np.ones((5,5), np.uint8)
erosion = cv2.erode(binary, kernel, iterations=1)
cv2.imshow("Original Image", image)
cv2.imshow("Binary Image", binary)
cv2.imshow("Eroded Image", erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("eroded_image.jpg", erosion)
print("Erosion Operation Completed Successfully!")