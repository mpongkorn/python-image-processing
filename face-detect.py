import cv2

img = cv2.imread('people-walking.jpeg')
#img_resize = cv2.resize(img, (400,600))
face_model = cv2.CascadeClassifier('face-detect-model.xml') # โหลดมาจาก Github เป็น model ที่เขา teach ไว้แล้ว
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #แปลงสีเป็นเทา-ดำ
faces = face_model.detectMultiScale(img_gray) 

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (255,255,0), 2)

cv2.imshow('People walking face detector', img)
cv2.waitKey(0)
cv2.destroyAllWindows()