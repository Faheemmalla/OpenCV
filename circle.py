import cv2
image = cv2.imread("filename.jpeg")

if image is None:
    print("Image is not Working")
else:
    print("image loaded Sucessfully")
    color = (255,0,0)
    thickness = -1
    cv2.circle(image,(150,150),50,color,thickness)
    cv2.imshow("Circle",image)
    cv2.waitKey(0) 
    cv2.destroyAllWindows()
    #logic written in notebook