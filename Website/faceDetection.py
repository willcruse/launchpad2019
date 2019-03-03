"""Face Detection program used to trigger the arduino program"""
# Libraries
import cv2 # Open CV
import sys
import time

""" In order for the face detection to work, a cascade file is needed.
    In this program, the Haar cascade is used, for added accuracy  """
cascPath = "HaarCascade.xml" # File taken from OpenCV 3.4
faceCascade = cv2.CascadeClassifier(cascPath)
video_capture = cv2.VideoCapture(0)
time.sleep(2) # Sleeps for 2 seconds to allow for comms to set up
faceCounter = 0
limit = 50 # Waits for 50 frames of the person being in view before setting off
sleepCounter = 500
sleepLimit = 500

while True:
    found = False
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(grayFrame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    # Draw a rectangle around the faces
    colourArray = [[255,0,0],[0,255,0],[0,0,255],[255,255,0],[0,255,255],[255,0,255],[255,255,255],[0,0,0]]
    colourIndex = 0
    if sleepCounter > sleepLimit:
        for (x, y, width, height) in faces:
        # Loops through the faces and draws a box around them
            colour = colourArray[colourIndex]
            cv2.rectangle(frame, (x, y), (x + width, y + height), (colour), 2) # Maybe different 
            if width > 100: # Checks to see if they're "close"
                faceCounter += 1
                if faceCounter > limit: # User has to be "close" for 50 frames (~5 seconds) before triggering
                    found = True
            else:
                counter = 0
                
            if colourIndex >= len(colourArray)-1:
                colourIndex = 0
            else:
                colourIndex += 1
                
        # Display the resulting frame
        cv2.imshow('Face Detection Cam', frame)
    else:
        sleepCounter += 1
    
    if found:
        print("Face detected! \nProgram started!")
        faceCounter = 0
        found = False
        sleepCounter = 0
        #time.sleep(30) # Timer to stop the person from being seen multiple times 
        
    if len(faces) == 0: # Resets the counter if no face is detected
        counter = 0
        
    if cv2.waitKey(1) & 0xFF == ord('q'): # Stops the program if q is pressed
        break
    
# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
