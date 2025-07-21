import cv2

img_path = "./images/bird.jpg"
img = cv2.imread(img_path)

print(img.shape)
#cropping
cropped_img = img[30:380, 70:500]

#visualizing
cv2.imshow('image', img)
cv2.imshow('cropped_img', cropped_img)
cv2.waitKey(0)