import cv2
import numpy as np

image_path = '/Users/gizemgullu/Downloads/theImage.jpeg'
image = cv2.imread(image_path)

b, g, r = cv2.split(image)

cv2.imshow('Blue Image', b)
cv2.imshow('Green Image', g)
cv2.imshow('Red Image', r)


redBlueImage = cv2.merge([b, np.zeros_like(b), r])
cv2.imshow("Red and Blue Image:", redBlueImage)

originalImage = cv2.merge([b, g, r])
cv2.imshow('New Image:', originalImage)


cv2.waitKey(0)
cv2.destroyAllWindows()