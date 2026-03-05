import cv2
image = cv2.imread("filename.jpeg")
#image.shape give us (height,width,color channel)
#agr grayscale hai tab bas height aur width aayegi kyu ki wo 1 he hota hai but bgr mai 3 aata hai
if image is not None:
    h,w,c = image.shape
    print(f"Image loaded:\nHeight:{h}\nWidth:{w}\nChannels:{c}")
else:
    print("Could not load Image")