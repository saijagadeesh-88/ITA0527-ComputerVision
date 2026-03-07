import cv2 
import numpy as np  
image = cv2.imread("goku.jpg", cv2.IMREAD_GRAYSCALE) 
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)) 
blackhat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel) 
cv2.imshow("Original Image", image) 
cv2.imshow("Black Hat Image", blackhat) 
cv2.waitKey(0) 
cv2.destroyAllWindows()