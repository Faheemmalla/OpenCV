import cv2

# Image ko grayscale (black and white) mode mein load karna zaroori hai edge detection ke liye
img = cv2.imread("filename.jpeg", cv2.IMREAD_GRAYSCALE)

# cv2.Canny function syntax: cv2.Canny(image, threshold1, threshold2)
# 50: Lower Threshold (Isse kam intensity wale gradients reject ho jayenge)
# 150: Upper Threshold (Isse zyada intensity wale gradients pakka edges maane jayenge)
edges = cv2.Canny(img, 50, 150)

# Windows mein results dikhane ke liye
cv2.imshow("Original Image", img)
cv2.imshow("Edges", edges)

# Keyboard press ka wait karega aur phir saare windows band kar dega
cv2.waitKey(0)
cv2.destroyAllWindows()