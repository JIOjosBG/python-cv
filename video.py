import cv2
import numpy as np

cv2.namedWindow("preview")

cap = cv2.VideoCapture(0)

if cap.isOpened():
    # try to get the first frame
    rval, frame = cap.read()
else:
    rval = False

while rval:
    blue=frame
    (h, w, d) = frame.shape
    (hb, wb, db) = blue.shape


    rval, frame = cap.read()
    """
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    strange = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imshow("gray", gray)
    cv2.imshow("Strange", strange)
    cv2.imshow("preview", frame)
    """
    for i in range(h):
        for j in range(w):
            BB = blue[i][j][0]
            BG = blue[i][j][1]
            BR = blue[i][j][2]
            if not (BB > 225):
                if not (BG > 50 and BG<100):
                    if not (BR > 50 and BR<100):
                        pass
                        #blue[i][j][0], blue[i][j][1], blue[i][j][2] = 0, 0, 0
    cv2.imshow("blue", blue)
    cv2.imshow("preview", frame)
    key = cv2.waitKey(20)


    #print(R,G,B)
    if key == 27:
        for i in range(h):
            for j in range(w):



                R = frame[i][j][2]
                G = frame[i][j][1]
                B = frame[i][j][0]
                if blue[i][j][0]!=0 and i==h-1:
                    print(blue[i][j][0], blue[i][j][1], blue[i][j][2])
        print(h,w,d)
        break
cap.release()
cv2.destroyAllWindows()











