import cv2
import serial
face_cascade = cv2.CascadeClassifier('fullbody.xml')
COM_PORT = 'COM15'  
BAUD_RATES = 9600
ser = serial.Serial(COM_PORT, BAUD_RATES) 
cap = cv2.VideoCapture(1)

while True:
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 1)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y+50), (x+w, y+h), (255, 0, 0), 4)
        print(x,y,w,h)
        if x<150 :
            print("too left")
            ser.write(b'1\n')
        elif x>420 :
            print("too  right")
            ser.write(b'2\n')
        else:
            ser.write(b'0\n')

    cv2.imshow('img', img)

    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
cap.release()
