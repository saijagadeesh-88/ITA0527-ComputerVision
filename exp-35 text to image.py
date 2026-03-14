import numpy as np
import cv2
def add_text_to_image(image_size, text):
    height, width = image_size  
    image = np.ones((height, width, 3), dtype=np.uint8) * 255
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_thickness = 2
    text_color = (0, 0, 255)  
    text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
    text_x = (width - text_size[0]) // 2
    text_y = (height + text_size[1]) // 2
    cv2.putText(image, text, (text_x, text_y), font, font_scale, text_color, font_thickness)
    cv2.imshow("Image with Text", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
user_width = int(input("Enter image width: "))
user_height = int(input("Enter image height: "))
user_text = input("Enter the text to display: ")
add_text_to_image((user_height, user_width), user_text)