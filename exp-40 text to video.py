import cv2
import easyocr

def extract_text_from_video(video_path):

    reader = easyocr.Reader(['en']) 
    cap = cv2.VideoCapture(video_path)

    frame_no = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_no += 1

        # detect text in frame
        results = reader.readtext(frame)

        for (bbox, text, prob) in results:
            print("Frame:", frame_no)
            print("Detected Text:", text)
            print("---------------------")

    cap.release()


extract_text_from_video("car.mp4")