import face_recognition
import os
import math
import cv2
import numpy as np
import sys
from ultralytics import YOLO
from dotenv import load_dotenv

load_dotenv()

model = YOLO("./models/l_version_1_30.pt")

classNames = ["fake", "real"]

class FaceRecognize:
    known_face_encoding = []
    known_face_names = []

    def __init__(self):
        self.encode_face()

    def encode_face(self):
        for image in os.listdir(os.getenv('People_images_path')):
            face_image = face_recognition.load_image_file(os.path.join(os.getenv('People_images_path'), image))
            face_encoding = face_recognition.face_encodings(face_image)[0]

            self.known_face_encoding.append(face_encoding)
            self.known_face_names.append(os.path.splitext(image)[0])

    def run_recognition(self):
        video_capture = cv2.VideoCapture("C:/Users/asus/Downloads/Test1 - Made with Clipchamp.mp4")
        # video_capture = cv2.VideoCapture(0)
        video_capture.set(3, 640)
        video_capture.set(4, 480)
        name=""
        cv2.namedWindow("Face Recognition", cv2.WINDOW_NORMAL)  # WINDOW_NORMAL allows resizing
        cv2.resizeWindow("Face Recognition", 1280, 720) 

        if not video_capture.isOpened():
            sys.exit('Video Source Not Found')

        while True:
            ret, frame = video_capture.read()
            if not ret:
                break  # Break the loop if no frame is read

            results = model(frame, stream=True, verbose=False)
            for r in results:
                boxes = r.boxes
                for box in boxes:
                    conf = math.ceil((box.conf[0] * 100)) / 100
                    cls = int(box.cls[0])
                    x1, y1, x2, y2 = box.xyxy.squeeze().tolist()

                    if conf > 0.6 and classNames[cls] == "real":  # Assuming class index 1 is for real face

                        # Crop the face from the frame using the coordinates
                        face_image = frame[int(y1):int(y2), int(x1):int(x2)]

                        # Convert the face_image to RGB format
                        face_image_rgb = cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB)

                        # Encode the detected face if face is found
                        face_encodings = face_recognition.face_encodings(face_image_rgb)
                        if len(face_encodings) > 0:
                            detected_face_encoding = face_encodings[0]

                            # Compare the detected face encoding with known authentic face encodings
                            face_distances = face_recognition.face_distance(FaceRecognize.known_face_encoding, detected_face_encoding)
                            best_match_index = np.argmin(face_distances)
                            face_distance = face_distances[best_match_index]

                            # Assuming face_distance_threshold is a value you define
                            if face_distance < 0.4:
                                # Face is recognized as authentic, draw a green box around it
                                name=str(FaceRecognize.known_face_names[best_match_index])
                                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                            else:
                                # Face is not recognized as authentic, draw a red box around it
                                name="Unknown"
                                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)
                        else:
                            print("No face detected in the provided image")
                    elif conf > 0.6 and classNames[cls] == "fake":
                        name="fake"
                        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)
                        cv2.putText(frame, "Fake", (int(x1)+6, int(y2)-6), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,255,255), 1)

            cv2.imshow('Face Recognition', frame)

            if cv2.waitKey(1) == ord('q'):
                break
            if cv2.waitKey(1)==ord('o'):
                return name

        video_capture.release()
        cv2.destroyAllWindows()

# Usage example
# if __name__ == "__main__":
#     face_recognizer = FaceRecognize()
#     face_recognizer.run_recognition()
