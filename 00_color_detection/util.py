import cv2
import numpy as np

#The input is an array with the values of the color in BGR, and returns 2 np.arrays with the min and max values of the HSV range 
def define_limits(color):
    c = np.uint8([[color]]) #converts the color array to a np.array, so the cv2 functions work
    c_hsv = cv2.cvtColor(c, cv2.COLOR_BGR2HSV) #Converts the color to hsv format

    #creates a tuple with hsv min and max values in Hue, Saturation and Value
    min_value = (c_hsv[0][0][0] - 20, 100, 100) 
    max_value = (c_hsv[0][0][0] + 20, 255, 255)

    #converts the tuples to np.array format
    min_value = np.array(min_value, dtype=np.uint8)
    max_value = np.array(max_value, dtype=np.uint8)

    return min_value, max_value