import cv2

image = cv2.imread("filename.jpeg")

blurred = cv2.GaussianBlur(image, (7,7), 0)
#kernel size (7,7) = kitne pixels ko mix karna hai (area)
#Sigma = kitna mix karna hai (intensity)
cv2.imshow("Original Image", image)
cv2.imshow("Blurred Image", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()
#logic in notebook