import cv2
import matplotlib.pyplot as plt
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
def det_face(img):
    img_copy = img.copy()
    face_rects = face_cascade.detectMultiScale(img_copy)
    for x,y,w,h in face_rects:
        cv2.rectangle(img_copy,(x,y),(w+x,h+y),(255,0,0),5)
    return img_copy
cap = cv2.VideoCapture(0)
while True:
    ret,img = cap.read(0)
    img = det_face(img)
    cv2.imshow('face detect in video',img)
    k = cv2.waitKey(1)
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
