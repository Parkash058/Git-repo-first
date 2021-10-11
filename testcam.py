import cv2
import time # Time delay
cam = cv2.VideoCapture(1) #Streaming video reading Camera frames
time.sleep(1) # delay of 1 sec
while True:
    _,img = cam.read() #return two values /read cam
    cv2.imshow("CameraFeed", img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
#cv2.imwrite("imagefromCamera.jpg", img)
cam.release()
cv2.destroyAllWindows()



