import cv2

img = cv2.imread('test.jpg', 1)
print(img)

cv2.imshow('image', img)

cv2.waitKey(2000)

cv2.destroyAllWindows()

funcs = dir(cv2)
for f in funcs:
	print(f)

