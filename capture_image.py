import cv2

video_capture = cv2.VideoCapture(0)

known_face_names = [
    "Suresh"
]

# Grab a single frame of video
ret, frame = video_capture.read()

# Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
rgb_frame = frame[:, :, ::-1]

cv2.imshow('Video', rgb_frame)

cv2.imwrite('Suresh.jpg', rgb_frame)