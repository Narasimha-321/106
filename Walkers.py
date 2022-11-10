import cv2


# Create our body classifier
body_classifier = cv2.CascadeClassifier('haarcascade_fullbody.xml')

# Initiate video capture for video file
cap = cv2.VideoCapture('walking.avi')

# Loop once video is successfully loaded
while(True):
    
    # Read first frame
    ret, frame = cap.read()
    faces = face_cascade.detectMultiScale(gray,1.1,4)
    print(faces)
    #Convert Each Frame into Grayscale

    # Pass frame to our body classifier
    bodies = body_classifier.detectMultiScale(gray, 1.2,3)
    
    # Extract bounding boxes for any bodies identified
    
    for (x,y,w,h) in bodies:
       cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    if cv2.waitKey(1) == 32: 
        break

cap.release()
cv2.destroyAllWindows()
