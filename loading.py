import cv2
image = cv2.imread("filename.jpeg")
if image is not None:
    cv2.imshow("Image Showing",image)
    cv2.waitKey(0) # 0 ka matlab jabtak na user kuch bhi press kare keybopard pe tab tak image dhikte rahegi
    cv2.destroyAllWindows()
else:
    print("image loaded sucessfully")