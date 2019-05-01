import cv2
import numpy as np

cv2.namedWindow("preview")

cap = cv2.VideoCapture(0)

if cap.isOpened():
    # try to get the first frame
    rval, frame = cap.read()
else:
    rval = False


def a(arg1,arg2):
    return abs(int(str(arg1))-int(str(arg2)))

def avrg(list,index):
    if len(list)>0:
        total=0
        for i in range(len(list)):
            total+=list[i][index]
        return total/len(list)
    else:
        return 0



color=[93, 161, 95]
ok=list()
drawing=1
cdiff=int()
spots=list()
drawat=[0,0]
while rval:
    (h, w, d) = frame.shape
    rval, frame = cap.read()
    new=frame

    #print(frame[0][w-1][0],frame[0][w-1][1],frame[0][w-1][2])
    if drawing==1:
        for i in range(int(int(h-h%15)/15)):
            for j in range(int(int(w-w%15)/15)):
                cdiff=a(frame[i*15][j*15][0],color[0])+a(frame[i*15][j*15][1],color[1])+a(frame[i*15][j*15][2],color[2])
                if cdiff<50:
                    ok.append([i*15,j*15,cdiff])

        for j in range(3):
            for m in range(10):
                frame[avrg(ok,0)+m][avrg(ok,1)+m][j]=0
                frame[avrg(ok,0)-m][avrg(ok,1)-m][j]=0
                frame[avrg(ok,0)+m][avrg(ok,1)-m][j]=0
                frame[avrg(ok,0)-m][avrg(ok,1)+m][j]=0
        if len(ok)>0:
            spots.append([avrg(ok,0),avrg(ok,1),avrg(ok,2)])
        for i in range(len(spots)):
            for j in range(3):
                for x in range(2):
                    for y in range(2):
                        drawat[0]=x
                        drawat[1]=y
                        frame[spots[i][0]-x][spots[i][1]-y][j]=0
        ok=list()
    cv2.imshow("preview", frame)
    ok=list()
    key = cv2.waitKey(20)
    if key == 27:
        print(ok)
        print(h,w,d)

        break





cap.release()
cv2.destroyAllWindows()
