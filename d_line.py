import cv2
image = cv2.imread("filename.jpeg")

if image is None:
    print("Image is not Working")
else:
    print("image loaded Sucessfully")
    #pt1-> start
    #pt2->end
    # points ki value as per the size rakhte hai ausse zaayda nai
    pt1 = (50,100)
    pt2 = (300,100)
    color = (255,0,0)
    #thickness of line
    thickness = 4
    cv2.line(image,pt1,pt2,color,thickness)
    cv2.imshow("Line Drawing",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #logic written on notebook