import cv2

img = cv2.imread('test.png')
print (img.shape)
img = cv2.resize(img, (500, 500))
print (img.shape)

cv2.imshow('Ressults', img)
cv2.waitKey(10000)