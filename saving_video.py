import cv2  
# OpenCV library import kar rahe hain
# Ye computer vision aur camera handling ke liye use hoti hai


camera = cv2.VideoCapture(0)  
# System ka default webcam open kar rahe hain
# 0 = primary camera (agar external ho toh 1, 2 bhi ho sakta hai)


frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))  
# Camera se current video frame ki width le rahe hain
# int() isliye kyunki ye float deta hai aur hume integer chahiye

frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))  
# Camera se current video frame ki height le rahe hain


codec = cv2.VideoWriter_fourcc(*'XVID')  
# Video encoding format define kar rahe hain
# XVID ek common codec hai jo .avi file ke liye use hota hai


recorded = cv2.VideoWriter("my_video.avi", codec, 20, (frame_width, frame_height))  
# VideoWriter object bana rahe hain jo video file create karega
# "my_video.avi" = file ka naam
# codec = encoding format
# 20 = FPS (20 frames per second)
# (frame_width, frame_height) = video size


while True:  
    # Infinite loop taaki recording continuously chalti rahe

    success, image = camera.read()  
    # Camera se ek frame (image) capture kar rahe hain
    # success = True/False (frame mila ya nahi)
    # image = actual frame (numpy array)

    if not success:  
        # Agar frame capture nahi hua
        break  
        # Loop stop kar do

    recorded.write(image)  
    # Jo frame mila hai usko video file me save kar do

    cv2.imshow("Recording live", image)  
    # Live video screen par show kar rahe hain
    # Window ka naam: "Recording live"

    if cv2.waitKey(1) & 0xFF == ord('q'):  
        # Agar user ne 'q' key press ki
        break  
        # Recording stop kar do


camera.release()  
# Camera resource free kar rahe hain

recorded.release()  
# Video file properly close kar rahe hain (warna corrupt ho sakti hai)

cv2.destroyAllWindows()  
# Saare OpenCV windows band kar rahe hain