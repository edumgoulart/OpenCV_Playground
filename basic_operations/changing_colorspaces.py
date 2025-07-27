import cv2

img_path = "./images/bird.jpg"
img = cv2.imread(img_path)

# Changing color spaces
# BGR is the default in OpenCV
# RGB is standard in most other libraries
# HSV is good for color detection because it separates color from brightness

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


cv2.imshow("img", img)
cv2.imshow("img_rgb", img_rgb)
cv2.imshow("img_hsv", img_hsv)
cv2.waitKey(0)