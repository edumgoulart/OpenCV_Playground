import cv2

img_path = "./images/bird.jpg"
img = cv2.imread(img_path)

#resinzing
resized_img = cv2.resize(img, (1840,1480))

#visualizing
print(img.shape)
print(resized_img.shape)

cv2.imshow('img', img)
cv2.imshow('resized_img', resized_img)
cv2.waitKey(0)