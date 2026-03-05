import cv2
image = cv2.imread("filename.jpeg")
if image is None:
    print("Image not found")
else:
    print("Image Loaded")
    resized = cv2.resize(image,(300,300))
    #syntax
    #resized = cv2.resize(source,nw size in tuple (width,heigt))
    #imshow image ko show krta hai
    cv2.imshow("Original Image",image)
    cv2.imshow("Resized Image",resized)
    #always save image after resizing 
    #warna overlap hota hai
    cv2.imwrite("resized_output.png",resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()