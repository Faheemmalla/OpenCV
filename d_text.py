import cv2
image = cv2.imread("filename.jpeg")

if image is None:
    print("Image is not Working")
else:
    print("image loaded Sucessfully")
    color = (255,0,0)
    thickness = 3
    cv2.putText(image,"kanye is GOAT",(50,300),cv2.FONT_HERSHEY_COMPLEX,1.2,color,thickness)
    cv2.imshow("Circle",image)
    cv2.waitKey(0) 
    cv2.destroyAllWindows()
    #logic written in notebook