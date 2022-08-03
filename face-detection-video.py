# เปิดวีดีโอด้วย OpenCV
# การบันทึกวีดีโอ

import cv2

cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture('batteryfire.mp4')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
face_model = cv2.CascadeClassifier('face-detect-model.xml')
#cap_gray = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)
#faces = face_model.detectMultiScale(cap_gray)

result = cv2.VideoWriter('face-detector-output.avi',fourcc,20.0,(640,480)) # ชื่อ ระบุ fourcc ระบุ framerate ระบุขนาด

while cap.isOpened():
    ref, frame = cap.read() # รับภาพจากกล้อง frame ต่อ frame

    if ref == True:
        cap_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # เปลี่ยนภาพสีเป็นขาว เทา ดำ
        faces = face_model.detectMultiScale(cap_gray)

        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (255,255,0), 2)

        cv2.imshow('face-detector-output', frame)
        result.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('e'):
            break
    else:
        break

result.release()
cap.release()
cv2.destroyAllWindows()