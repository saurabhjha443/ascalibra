import cv2
from datetime import datetime

vs= cv2.VideoCapture(0)
ret,frame1 = vs.read()
ret,frame2 = vs.read()
while True:
    if ret is True:
            diff=cv2.absdiff(frame1,frame2)
            gray=cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
            blur=cv2.GaussianBlur(gray,(5,5),0)
            _,thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
            dilated_frame=cv2.dilate(thresh, None, iterations=5)
            contours, _ =cv2.findContours(dilated_frame,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            for contour in contours:
                (x,y,z,h)=cv2.boundingRect(contour)
                if cv2.contourArea(contour)<800:
                #    cv2.putText(frame1, "Status:{}".format("No Movement"), (10,30), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 2)
                    continue
                cv2.rectangle(frame1,(x,y),(x+z,y+h),(0,255,0),2)
               # cv2.putText(frame1,"Status:{}".format("Movement"),(10,20),cv2.FONT_HERSHEY_PLAIN, 3 , (0,255,0),2)
                cv2.putText(frame1,str(datetime.now()),(40,60),cv2.FONT_HERSHEY_PLAIN, 3 , (0,255,0),2)
                cv2.imshow("Security",frame1)
                frame1=frame2
                ret,frame2=vs.read()
            if cv2.waitKey(10) & 0xFF == ord("q"):
                break

vs.release()
cv2.destroyAllWindows()

