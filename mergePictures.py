import numpy as np
import cv2

img = cv2.imread('lena.jpg')

print(img.shape)
print(img.size)
print(img.dtype)
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

cv2.imshow('image', img)
cv2.imshow('roi', ball)
cv2.waitKey(0)
cv2.destroyAllWindows()
