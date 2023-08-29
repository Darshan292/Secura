import face_recognition
import os, sys
import cv2
import numpy as np 
import math
from dotenv import load_dotenv
# YES
load_dotenv()dflkcjsdc
sdfas
fsafsdfsda
sfdsdfdasd

def face_recognised(face_distance, face_match_threshold = 0.6):
    range = (1.0-face_match_threshold)
    linear_value = (1.0 - face_distance)/(range * 2.0)

    if face_distance > face_match_threshold:
        return str(round(linear_value * 100, 2))+"%"
    else:
        value = (linear_value + ((1.0-linear_value)*math.pow((linear_value-0.5)*2, 0.2)))*100
        return str(round(value, 2))+ '%'
    

class FaceRecognize:
    face_location = []
    face_encodings = []
    face_names = []
    known_face_encoding = []
    known_face_names = []
    names_in_frame = []
    process_current_frame = True

    def __init__(self):
        self.encode_face()


    def encode_face(self):
        for image in os.listdir(os.getenv('People_images_path')):
            face_image = face_recognition.load_image_file(os.path.join(os.getenv('People_images_path'), image))
            face_encoding = face_recognition.face_encodings(face_image)[0]

            self.known_face_encoding.append(face_encoding)
            self.known_face_names.append(os.path.splitext(image)[0])

        print(self.known_face_names)

    
    def run_recognition(self):
        
        video_capture = cv2.VideoCapture(0)


        if not video_capture.isOpened():
            sys.exit('Video Source Not Found')
        
        while True:
            ret, frame = video_capture.read()

            if self.process_current_frame:
                small_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
                rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

                self.face_location = face_recognition.face_locations(rgb_small_frame)
                self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_location)

                self.face_names = []
                for face_encoding in self.face_encodings:
                    matches = face_recognition.compare_faces(self.known_face_encoding, face_encoding)
                    name = 'Unknown'
                    confidence  = '0.0'

                    face_distances = face_recognition.face_distance(self.known_face_encoding, face_encoding)
                    best_match_index = np.argmin(face_distances)

                    if matches[best_match_index]:
                        name = self.known_face_names[best_match_index]
                        confidence = face_recognised(face_distances[best_match_index])
                    
                    self.face_names.append(f'{name} ({confidence})')

            self.process_current_frame = not self.process_current_frame

            for(top, right, bottom, left), name in zip(self.face_location, self.face_names):
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                cv2.rectangle(frame, (left,top), (right, bottom), (0, 0, 255), 2)
                cv2.rectangle(frame, (left,bottom-35), (right, bottom), (0, 0, 255), -1)
                cv2.putText(frame, name, (left+6, bottom-6), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,255,255), 1)

            cv2.imshow('Face Recognition', frame)

            if cv2.waitKey(1) == ord('o'):
                return self.face_names
            if cv2.waitKey(1) == ord('q'):
                break
        video_capture.release()




