import cv2

img_path = "./images/birds.jpg" 
img = cv2.imread(img_path)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#thresholding inverting colors
ret, img_threshold = cv2.threshold(img_gray, 120, 255, cv2.THRESH_BINARY_INV)

#getting the contours
contours, hierarchy = cv2.findContours(img_threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    if cv2.contourArea(cnt) > 20:
        #cv2.drawContours(img, cnt, -1, (0,255,0), 1)
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 3)

cv2.imshow("img", img)
cv2.imshow("img1", img_threshold)
cv2.waitKey(0)