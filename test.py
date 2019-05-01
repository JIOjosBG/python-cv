import cv2
import numpy as np


# load the input image and show its dimensions, keeping in mind that
# images are represented as a multi-dimensional NumPy array with
# shape no. rows (height) x no. columns (width) x no. channels (depth)
image = cv2.imread("multy.jpg")
(h, w, d) = image.shape

    
print("width={}, height={}, depth={}".format(w, h, d))

# access the RGB pixel located at x=50, y=100, keepind in mind that
# OpenCV stores images in BGR order rather than RGB

image
red=0
green=0
blue=0
for i in range(h):
    for j in range(w):
        (B, G, R) = image[i, j]
        red=red+R
        green=green+G
        blue=blue+B
mypixels=h*w
totalred=red/mypixels-red/mypixels%1
totalgreen=green/mypixels-green/mypixels%1
totalblue=blue/mypixels-blue/mypixels%1
print("red=",totalred," green=",totalgreen," blue=",totalblue)


# display the image to our screen -- we will need to click the window
# open by OpenCV and press a key on our keyboard to continue execution
cv2.imshow("Image", image)
cv2.waitKey(0)

