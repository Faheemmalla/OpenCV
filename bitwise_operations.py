import cv2
import numpy as np

# Do black images create karna (300x300 size)
img1 = np.zeros((300, 300), dtype="uint8")
img2 = np.zeros((300, 300), dtype="uint8")

# img1 par ek white circle draw karna
cv2.circle(img1, (150, 150), 100, 255, -1)

# img2 par ek white rectangle draw karna
cv2.rectangle(img2, (100, 100), (255, 255), 255, -1)

# 1. BITWISE AND: Dono images ka common part (jahan dono white hain)
bitwise_and = cv2.bitwise_and(img1, img2)

# 2. BITWISE OR: Dono images ka total area (jahan koi bhi ek white hai)
bitwise_or = cv2.bitwise_or(img1, img2)

# 3. BITWISE NOT: Image ko ulta karna (White becomes Black, Black becomes White)
# Fix: Screenshot mein cv2.bitwise_or likha tha, use cv2.bitwise_not hona chahiye
bitwise_not = cv2.bitwise_not(img1)

# Results dikhane ke liye
cv2.imshow("Circle", img1)
cv2.imshow("Rectangle", img2)
cv2.imshow("AND", bitwise_and)
cv2.imshow("OR", bitwise_or)
cv2.imshow("NOT", bitwise_not)

cv2.waitKey(0)
cv2.destroyAllWindows()