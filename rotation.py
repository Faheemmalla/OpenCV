#syntax
#centre->(x,y) bhjte hai aur bolte hai kaise rotate krna hai(clockwise ya anticlockwise)
#hum w and h ko //2 to get exact centre (// yaane decimal nhi aayega integer divisin krta hai) isse perfectly spin hota hai 
# angle->in degrees kis amout se rotate krna hai 90->acw and -90 yaane anticlockwise
# scale->how much to zoom in or zoom out during rotation 1.0 yaane same size , 0.5 yaane adha krdo
#synatx second ka
# image-> orginal image kiya 
#M-> jo formula create kiya
# and width and height as a tuple pass krna hai(ye naya size hoga orginal image ka )

import cv2
image = cv2.imread("filename.jpeg")
if image is None:
    print("Could not load image")
else:
     (h,w) = image.shape[:2]
     center=(w//2,h//2)
     #func1 (syntax explain above)
     M = cv2.getRotationMatrix2D(center,90,1.0)
     rotated=cv2.warpAffine(image,M,(w,h))
     cv2.imshow("Original image",image)
     cv2.imshow("Rotated 90 degree",rotated)
     cv2.waitKey(0)
     cv2.destroyAllWindows()
     
