import cv2
import face_recognition 
import os
import serial 
import time
# Initialize Arduino
arduino = serial.Serial('COM9', 9600) # Adjust COM port 
time.sleep(2)
# Load authorized face(s) 
authorized_images = [] 
authorized_names = []
path = 'authorized_faces' # Folder containing authorized face images 
for filename in os.listdir(path):
img=face_recognition.load_image_file(f"{path}/{filename} 
")
encoding = face_recognition.face_encodings(img)[0] 
authorized_images.append(encoding) 
authorized_names.append(os.path.splitext(filename)[0])
# Start webcam
cap = cv2.VideoCapture(0) 
while True:
ret, frame = cap.read() 
if not ret:
continue
rgb_frame=cv2.cvtColor(frame, 
cv2.COLOR_BGR2RGB)
face_locations=face_recognition.face_locations(rgb_frame) 
face_encodings=face_recognition.face_encodings(rgb_frame, face_locations)
match_found = False
for face_encoding in face_encodings: 
matches=face_recognition.compare_faces(authorized_images, face_encoding)
if True in matches: 
match_found = True 
break
# Send signal to Arduino 
if match_found:
arduino.write(b'G') 
print("Authorized face - Sent G")
else:
arduino.write(b'R') 
print("Unauthorized face - Sent R")
# Show window
for (top, right, bottom, left) in face_locations:
color = (0, 255, 0) if match_found else (0, 0, 255) 
cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
cv2.imshow("Smart Door Lock", frame) 
if cv2.waitKey(1) == 27: # ESC to quit
break 
cap.release()
cv2.destroyAllWindows() 
arduino.close()
