import cv2
import numpy
import pyttsx

engine = pyttsx.init() #initializing engine

load = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap=cv2.VideoCapture(0)

rec = cv2.createLBPHFaceRecognizer()
rec.load("recognizer/TraningData.yml") #loading the training data
font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,4,1,0,4)

f = open("datatext.txt","r")
user = {}
for x  in f:
        y,z = x.split(" ")
        user[y] = z.replace("\n","")

while(1):
    status,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = load.detectMultiScale(gray,1.3,5)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        id,conf = rec.predict(gray[y:y+h,x:x+w]) #returns id and confidence level
        print id
        if(conf>75):   #VERY IMP confidence level is checked
            name = "Unknown"
            
        else:
            name = user[str(id)]

        engine.say(name)
        engine.runAndWait()
        
        cv2.cv.PutText(cv2.cv.fromarray(img),str(name),(x,y+h),font,255)
        
    cv2.imshow('FaceDetect',img)
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

f.close()
cap.release()
cv2.destroyAllWindows()
    
