import cv2
image = cv2.imread("filename.jpeg")
if image is not None:
    sucess = cv2.imwrite("output_file.png",image)
    if sucess:
        print("image saved Sucessfully as 'output_file.png'")
    else:
        print("Failed to save an image")
else:
    print('Error: Could not load image')
