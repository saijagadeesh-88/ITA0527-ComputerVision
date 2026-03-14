import cv2

def reverse_video(input_path, output_path):

    cap = cv2.VideoCapture(input_path)

    if not cap.isOpened():
        print("Error: Cannot open video file")
        return

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Use AVI codec (more stable)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    frames = []

    # Read frames
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()

    # Reverse frames
    frames.reverse()

    # Write reversed frames
    for frame in frames:
        out.write(frame)

    out.release()

    print("Reversed video saved successfully:", output_path)


reverse_video("car.mp4", "reversed_video.avi")