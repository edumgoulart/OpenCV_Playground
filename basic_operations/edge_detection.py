import cv2

image_path = "./images/bird.jpg"
img = cv2.imread(image_path)


#edge detection
img_edge = cv2.Canny(img, 120, 350)

#visualizing image
cv2.imshow('image', img)
cv2.imshow('image_edge', img_edge)
cv2.waitKey(0)