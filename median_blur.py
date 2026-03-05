#Har pixel ki jagah, uske surrounding pixels ka median (middle value) le leta hai
#Jaise 3x3 area mein 9 pixels honge, unko sort karke jo beech wali value hogi, wahi naya pixel banega
import cv2

image = cv2.imread("filename.jpeg")

blurred = cv2.medianBlur(image, 11)

cv2.imshow("Original", image)
cv2.imshow("Clean Image", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()