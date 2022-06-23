import cv2


cap = cv2.VideoCapture(0) #카메라

while True:
    retval, frame = cap.read()
    
    if retval == False:
        break
    
    cv2.imshow('frame', frame)
    
    if cv2.waitKey() == 27:
        break;

cap.release()
cap.destroyAllWindows()

