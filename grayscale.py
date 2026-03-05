import cv2
image = cv2.imread("filename.jpeg")
if image is not None:
    #to convert black n wite to gray
    #gray:- variable name
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    # COLOR_BGR2GRAY color full ko gray mai convert krta hai(yaane black and white image mai convert krta hai)
    #now see
    cv2.imshow("Grayscale Image",gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Could not load the Image")