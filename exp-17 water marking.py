import cv2
import numpy as np
original = cv2.imread("goku.jpg")
if original is None:
    print("Error: goku.jpg not found")
    exit()
watermark = cv2.imread("goku.jpg")
if watermark is None:
    print("Error: watermark image not found")
    exit()
h, w = original.shape[:2]
watermark = cv2.resize(watermark, (int(w*0.3), int(h*0.3)))
wh, ww = watermark.shape[:2]
x = w - ww - 10
y = h - wh - 10
roi = original[y:y+wh, x:x+ww]
alpha = 0.4
blended = cv2.addWeighted(roi, 1-alpha, watermark, alpha, 0)
original[y:y+wh, x:x+ww] = blended
cv2.imshow("Watermarked Goku Image", original)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("goku_watermarked.jpg", original)

print("Watermark added to goku.jpg successfully!")