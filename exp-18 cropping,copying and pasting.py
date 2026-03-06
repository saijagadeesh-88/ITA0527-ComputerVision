import cv2
image = cv2.imread("image.jpg")
if image is None:
    print("Error: image.jpg not found")
    exit()
height, width = image.shape[:2]
print("Image Size:", width, "x", height)
x1 = width // 4
y1 = height // 4
x2 = width // 2
y2 = height // 2
roi = image[y1:y2, x1:x2].copy()
new_x = width // 2
new_y = height // 2
roi_h, roi_w = roi.shape[:2]
if new_y + roi_h <= height and new_x + roi_w <= width:
    image[new_y:new_y+roi_h, new_x:new_x+roi_w] = roi
else:
    print("ROI too large to paste at selected location")
    exit()
cv2.imshow("Cropped ROI", roi)
cv2.imshow("Final Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("roi_output.jpg", image)
print("Cropping, Copying and Pasting Done Successfully!")