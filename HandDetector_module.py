import cv2
import mediapipe as mp
import time

class handDetect():
  def __init__(self, mode = False, max_hands=2,modelComplexity=1,min_detection_co = 0.5, min_tracing_co = 0.5):
    self.mode = mode
    self.max_hands = max_hands
    self.min_detection_co = min_detection_co
    self.min_tracing_co = min_tracing_co
    self.modelComplexity = modelComplexity

    self.np_hands = mp.solutions.hands
    self.mpDraw = mp.solutions.drawing_utils
    self.hands = self.np_hands.Hands(self.mode, self.max_hands, self.modelComplexity, self.min_detection_co, self.min_tracing_co)
    


  def findhands(self, img, draw=True):
    #convert bgr to rgb
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    #prosses hand in img
    result = self.hands.process(rgb_img)

    if result.multi_hand_landmarks:
      for handLm in result.multi_hand_landmarks:
        if draw:
          self.mpDraw.draw_landmarks(img, handLm, self.np_hands.HAND_CONNECTIONS)
    return img
    
    def findposition(self, img, handno=0, draw = False):
      result = self.hands.process(rgb_img)
      landmarklist = []
      if result.multi_hand_landmarks:
        myhand = result.multi_hand_landmarks[handno]
        for id, lm in enumerate(myhand.landmarks):
          h, w, c = img.shape
          cx, cy = int(lm.x*w), int(lm.y*h)
          landmarklist.append([id,cx,cy])
      return landmarklist

def main():
  cap = cv2.VideoCapture(0)#webcam
  #for fps count
  Currentime = 0
  previoustime = 0
  detector = handDetect()
  while True:
      #read image
      success, img = cap.read()
      img = detector.findhands(img)

      #fps
      Currentime = time.time()
      fps = 1/(Currentime-previoustime)
      previoustime = Currentime
      cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (0,0,0))

      #display img
      cv2.imshow('Image',img)

      #esc key to exit
      if cv2.waitKey(1) & 0xFF == 27:
          break


if __name__ == "__main__":
  main()
