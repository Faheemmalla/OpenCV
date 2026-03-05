import cv2

# Image load karna (Grayscale mein zaroori hai)
img = cv2.imread("filename.jpeg", cv2.IMREAD_GRAYSCALE)

# cv2.threshold syntax: (src, thresh_value, max_value, type)
# ret: Optimal threshold value (is case mein wahi return karega jo aapne 120 diya hai)
# thresh_img: Output binary image
ret, thresh_img = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)

cv2.imshow("Original Image", img)
cv2.imshow("Thresholded Image", thresh_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
THRESHOLDING:
Thresholding ek image segmentation technique hai jisme hum image ko simplify karte hain. 
Iska maqsad background aur foreground (object) ko alag karna hota hai pixels ko 
sirf do values (0 ya 255) mein convert karke.
Aapne Threshold Value 120 set ki hai. Computer har pixel ko aise check karega:
1. Agar Pixel Value < 120 (e.g., 90 or 50) -> Result: 0 (Black)
2. Agar Pixel Value > 120 (e.g., 130 or 180) -> Result: 255 (White)
"""