import cv2

#reading video
video_path = "./videos/bird.mp4"

video = cv2.VideoCapture(video_path)

#visualizing video

ret = True #If ret is true it is because the video.read() function is working
while ret:
    ret, frame = video.read() #At the end of the video ret will become false

    if ret:
        cv2.imshow('frame', frame)
        cv2.waitKey(40)

video.release()
cv2.destroyAllWindows()