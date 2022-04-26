import cv2
import mediapipe as mp 
import time

cap = cv2.VideoCapture(0)#webcam

np_hands = mp.solutions.hands
hands = np_hands.Hands()
mpDraw = mp.solutions.drawing_utils

#for fps count
Currentime = 0
previoustime = 0

while True:
    #read image
    success, img = cap.read()
    h, w, c = img.shape

    #convert bgr to rgb
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    #prosses hand in img
    result = hands.process(rgb_img)
    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
           ''' for id,lm in enumerate(hand.landmark):
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id,cx,cy)
                if id ==0:
                    cv2.circle(img, (cx,cy), 10, (225,225,225))'''
            mpDraw.draw_landmarks(img, hand,np_hands.HAND_CONNECTIONS)


    #fps
    Currentime = time.time()
    fps = 1/(Currentime-previoustime)
    previoustime = Currentime
    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_SIMPLEX, 3, (0,0,0))
    
    #display img
    cv2.imshow('Image',img)

    #esc key to exit
    if cv2.waitKey(1) & 0xFF == 27:
        break
