import cv2

def count_faces(image_path):

    image = cv2.imread(image_path)

    if image is None:
        print("Error: Image not found or path is wrong")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    print("Number of faces detected:", len(faces))

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Face Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


image_path = r"C:\Users\T.V.SAI JAGADEESH\Downloads\cv lab\faces.jpg"
count_faces(image_path)