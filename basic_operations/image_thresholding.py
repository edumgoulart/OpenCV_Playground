import cv2

img_path = "./images/handwritten.png" #bird or handwritten are good examples
img = cv2.imread(img_path)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#thresholding
ret, img_threshold = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)
img_adaptivethreshold = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 10)


cv2.imshow("img", img)
cv2.imshow("img1", img_threshold)
cv2.imshow("img2", img_adaptivethreshold)
cv2.waitKey(0)