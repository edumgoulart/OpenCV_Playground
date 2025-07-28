import cv2
from util import define_limits

color = [0,255,255] #Defines which color you want to detect

webcam = cv2.VideoCapture(0)
while True:
    ret, frame = webcam.read()

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    min_value, max_value = define_limits(color)

    mask = cv2.inRange(hsv_frame, min_value, max_value) # returns a binary img, if the pixel is in the hsv range returns white, else black

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        if cv2.contourArea(cnt) > 500:
            #cv2.drawContours(img, cnt, -1, (0,255,0), 1)
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 3)

    cv2.imshow("webcam", frame)
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
