import numpy as np
import cv2

cap = cv2.VideoCapture(0)

i = 0
while(True):
    #Capture fram-by-frame
    ret, frame = cap.read()

    #Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Display the resulting frame
    cv2.imshow('frame', gray)
    if i>5:
        print("Saving....")
        print('focusedtest' + str(int(i)) + '.jpg')
        cv2.imwrite('unfocused_test/unfocused_' + str(int(i)) + '.jpg', frame)

    i += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#When everything done, release the Capture
cap.release()
cv2.destroyAllWindows()
