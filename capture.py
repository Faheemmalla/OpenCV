import cv2
#syntax : VideoCature(source)
#source:- 0 :- yaane laptop k web cam se
#1:-externally webcame
#cap:- just a variable
cap = cv2.VideoCapture(0)
#tab tak chalte rehga jab tak user koi key na press krde 
#isseliye while loop
while True:
    ret,frame = cap.read() # ret= True/False , frame=image
    # ye doo cheezian return karega True yaane image capture hui hai and False matlab gadbad and frame wo image return karega jo aus moment pe capture hui hai
    #cap.read() yaane aak image ko read krna hai camera mai se
    if not ret:
        #yaane ki agr true nhi hai
        print("could not read Frame")
        break
    cv2.imshow("WebCame Feed",frame)
    #quiting k liye
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # 1 k matlab 1 milisecond wait krke dhekna hai ki user ne kuch press kiya hai ya na kiya hai
        #agr q press kiya toh loop exit hoga and then video band
        #ord se ieski ASCII value
        break
    #.release() camera ko band krta hai
cap.release()
cv2.destroyAllWindows()

