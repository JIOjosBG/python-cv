import cv2
import numpy as np

cv2.namedWindow("preview")

cap = cv2.VideoCapture(0)

if cap.isOpened():
    # try to get the first frame
    rval, frame = cap.read()
else:
    rval = False
old=frame
def a(arg1,arg2):
    return abs(int(str(arg1))-int(str(arg2)))
while rval:
    r,old=frame,frame
    (h, w, d) = frame.shape
    rval, frame = cap.read()
    cv2.imshow("preview", frame)
    for i in range(h):
        for j in range(w):
            if a(old[i][j][2],frame[i][j][2])+a(old[i][j][1],frame[i][j][1])+a(old[i][j][0],frame[i][j][0])>150:
                r[i][j][0],r[i][j][1],r[i][j][2]=0,0,0
            else:
                r[i][j][0],r[i][j][1],r[i][j][2]=255,255,255
    cv2.imshow("new", r)
    key = cv2.waitKey(20)
    if key == 27:
        print(h,w,d)
        break
cap.release()
cv2.destroyAllWindows()











