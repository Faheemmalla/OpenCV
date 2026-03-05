import cv2
image = cv2.imread("filename.jpeg")

if image is None:
    print("Image is not Working")
else:
    print("image loaded Sucessfully")
    pt1 = (50,50)
    pt2 = (250,200)
    color = (255,0,0)
    thickness = 3
    cv2.rectangle(image,pt1,pt2,color,thickness)
    cv2.imshow("Rectangle",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()