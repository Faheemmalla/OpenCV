     #flipcode-0->vertically flip yaane top to bottum
     # 1-> horizantally left to rihght
     # -1 -> yaane both
#flipped-> just a variable

import cv2
image = cv2.imread("filename.jpeg")
if image is None:
    print("Could not load image")
else:
     flipped0 = cv2.flip(image,0)
     flipped1 = cv2.flip(image,1)
     flipped_1 = cv2.flip(image,-1)
     cv2.imshow("original",image)
     cv2.imshow("Horizantal",flipped0)
     cv2.imshow("vertical",flipped1)
     cv2.imshow("both",flipped_1)
     cv2.waitKey(0)
     cv2.destroyAllWindows()