import csv
import cv2
import numpy as np
from datetime import datetime

import face_recognition  # Third-party import 

vid_cap = cv2.VideoCapture(0)
from datetime import datetime

vid_cap = cv2.VideoCapture(0)

# Load known faces and encodings outside the loop for efficiency
known_face_names = ['me', 'akshay']
known_face_encodings = []
for name in known_face_names:
    face_image = face_recognition.load_image_file(f'faces/{name}.jpg')
    face_encoding = face_recognition.face_encodings(face_image)[0]
    known_face_encodings.append(face_encoding)

students = known_face_names.copy()

face_locations = []
face_encodings = []

now = datetime.now()
currentDate = now.strftime('%Y-%M-%D')
f = open(f'{currentDate}.csv', 'w+', newline='')
lnwriter = csv.writer(f)

while True:
    _, frame = vid_cap.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Find faces and encodings in the frame
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distance)

        if matches[best_match_index]:
            name = known_face_names[best_match_index]
            # Add attendance record (logic for recording can be added here)
            lnwriter.writerow([name, datetime.now().strftime('%H:%M:%S')])
        if name in known_face_names: 
            font = cv2. FONT_HERSHEY_SIMPLEX
            bottomLeftCorner0fText = (10, 100)
            fontScale = 1.5
            fontColor = (255, 0, 0)
            thickness =3
            lineType =2
            cv2. putText(frame, name + " Present", bottomLeftCorner0fText, font, fontScale, fontColor, thickness,lineType)
            if name in students:
                students. remove (name)
                current_time = now. strftime ("%H-%M%S")
                lnwriter. writerow([name,current_time])
        cv2.imshow('Attendance', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break



