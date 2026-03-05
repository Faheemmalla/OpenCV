import cv2

# 1. Image load aur Grayscale conversion (Contours hamesha binary/grayscale par achha kaam karte hain)
img = cv2.imread("triangle.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 2. Thresholding: Image ko Black & White (Binary) banana zaroori hai
_, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

# --- SYNTAX: cv2.findContours(image, retrieval_mode, approximation_method) ---
# image: Source binary image.
# retrieval_mode (cv2.RETR_TREE): Yeh saare contours nikalta hai aur unka "family tree" (hierarchy) banata hai.
# approximation_method (cv2.CHAIN_APPROX_SIMPLE): Yeh memory bachata hai. 
# Agar ek seedhi line hai, toh uske saare points ke bajaye sirf corners/endpoints save karta hai.

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# --- SYNTAX: cv2.drawContours(target_image, contours_list, contour_index, color, thickness) ---
# target_image: Jis image par outline draw karni hai (img).
# contours_list: Jo contours findContours se mile.
# contour_index (-1): Iska matlab hai "saare" contours draw karo. Agar 0 likhte toh sirf pehla draw hota.
# color (0, 255, 0): BGR format mein Green color.
# thickness (3): Line ki motayi.

cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

cv2.imshow("Contours Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()