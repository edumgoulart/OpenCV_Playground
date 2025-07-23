import cv2

img_path = "./images/bird.jpg"
img = cv2.imread(img_path)

k_size = 15  # Size of the blur kernel; the larger the value, the blurrier the image becomes
#K_size has to be odd for the gaussianblur

#blurring
img_blur = cv2.blur(img,(k_size, k_size))
img_gaussianblur = cv2.GaussianBlur(img,(k_size, k_size),4)
img_medianblur = cv2.medianBlur(img,k_size)
#visualizing
cv2.imshow("img", img)
cv2.imshow("img_blur", img_blur)
cv2.imshow("img_Gaussianblur", img_gaussianblur)
cv2.imshow("img_Medianblur", img_medianblur)
cv2.waitKey(0)