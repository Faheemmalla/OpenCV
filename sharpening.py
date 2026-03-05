import cv2
import numpy as np

image = cv2.imread("filename.jpeg")
# Kernel ka sum 1 hona chahiye
kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])

sharpened = cv2.filter2D(image, -1, kernel)
cv2.imshow("Sharpened", sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Sharpening se image ke edges (kinare) aur details zyada prominent ho jate hain. Isse image clear, tight aur crisp lagti hai.
#more explaniation in notebook

