import cv2 

image_path = "./images/bird.jpg"

#reading image
img = cv2.imread(image_path)

#visualizing image
cv2.imshow('image', img)
cv2.waitKey(0)
