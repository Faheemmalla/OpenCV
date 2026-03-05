#1.1:- scale factor ies matlab kitna zoom 
# in krna hai jab face ddtect kr rahe ho yaane 10% smaller krta jaayega jab tak na face dhoond paaye
#5 yaane min neighbour matlab kitne strong clues chahiye before saying yes 3 pass karnege toh matlab loose checking
import cv2

face_cascade = cv2.CascadeClassifier("HaarCascadesModel/haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    """
    detectMultiScale() - scan & detect faces
    1.1 balance, not too slow, blind

    minNeighbors = 5
    """
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
    
    """
    

faces variable me detectMultiScale() se ek list/array aata hai.
Is list me har face ke liye ek tuple hota hai jisme 4 values hoti hain.

Format:
(x, y, w, h)

Example:
faces = [
    (100,150,80,80),   # face 1
    (250,120,90,90)    # face 2
]

Matlab camera ne 2 faces detect kiye.

Ab for loop kya karta hai:

for (x,y,w,h) in faces:
    matlab faces list ke har tuple ko ek ek karke uthao.

Iteration 1:
(x,y,w,h) = (100,150,80,80)

Iteration 2:
(x,y,w,h) = (250,120,90,90)

Har iteration me ye values milti hain:

x = face ka left se distance (starting x coordinate)
y = face ka top se distance (starting y coordinate)
w = face ki width
h = face ki height

Ab rectangle draw hota hai:

cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

(x,y)  
→ rectangle ka top-left corner

(x+w , y+h)
→ rectangle ka bottom-right corner

Example calculation:

(x,y,w,h) = (100,150,80,80)

top-left  = (100,150)

bottom-right =
(100+80 , 150+80)
(180 , 230)

Toh rectangle draw hoga:

(100,150) ------ (180,150)
     |               |
     |               |
     |               |
(100,230) ------ (180,230)

(0,255,0)
→ rectangle ka color (Green in BGR)

2
→ rectangle ki thickness

Final result:
jitne faces detect honge,
for loop utni baar chalega
aur har face ke around rectangle draw karega.
    """

    cv2.imshow("Webcam Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()