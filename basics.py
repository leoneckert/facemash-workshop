### ------
### open a image:
import cv2
import sys
# path = "data/face.jpg"
path = sys.argv[1]
img = cv2.imread(path)
print "[+] Opened image from:", path
cv2.imshow("face", img)



### ------
### detect a face
import dlib
detector = dlib.get_frontal_face_detector()
rects = detector(img)
print "[+] Number of faces found:", len(rects)
print "[i] Position of first face", rects[0] # gives top left and bottom right point: [(29, 61) (101, 133)]
# ------
# draw rectangle:
img_with_rect = img.copy()
x, y, h, w = rects[0].left(), rects[0].top(), rects[0].width(), rects[0].height()
cv2.rectangle(img_with_rect, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow("face with rectangle", img_with_rect)
# ------
# crop an image:  #http://stackoverflow.com/questions/15589517/how-to-crop-an-image-in-opencv-using-python
crop_img = img[y:y+h,x:x+w]
cv2.imshow("face_cropped", crop_img)



### ------
### get facial landmarks
import numpy as np
PREDICTOR_PATH = "shape_predictor_68_face_landmarks.dat"
predictor = dlib.shape_predictor(PREDICTOR_PATH)
landmarks = np.matrix([[p.x, p.y] for p in predictor(img, rects[0]).parts()])
# draw facial landmarks
img_with_landmarks = img.copy()
for idx, point in enumerate(landmarks):
    pos = (point[0, 0], point[0, 1])
    cv2.circle(img_with_landmarks,pos, 1, (0,0,255), -1)
cv2.imshow("aaron with landmarks", img_with_landmarks)
cv2.waitKey(0)
