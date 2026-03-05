#top left upper corner se shuru
#yaxis->rows -> top to bottom(numbering from 0 to n-1) last size excluded
#xaxis->columns -> left to right(0 to m-1)
#syntax = image[starty:endy,startx;endx]
# slicing jaisaa
import cv2
image = cv2.imread("filename.jpeg")
if image is not None:
    #cropped just a variable
    cropped = image[100:200,50:150]
    cv2.imshow("Image Showing",cropped)
    cv2.waitKey(0) # 0 ka matlab jabtak na user kuch bhi press kare keybopard pe tab tak image dhikte rahegi
    cv2.destroyAllWindows()
else:
    print("image loaded sucessfully")