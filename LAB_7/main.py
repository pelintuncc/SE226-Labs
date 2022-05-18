import cv2
import numpy as np
img = cv2.imread('Photos/cat.jpeg')
cv2.imshow('Cat', img)
(b, g, r) = cv2.split(img)
cv2.imshow("Blue", b)
cv2.imshow("Green", g)
cv2.imshow("Red", r)

print(img.shape)

minimum = np.array([10, 20, 30])
maximum = np.array([240, 245, 250])
r = cv2.inRange(img, minimum, maximum)

merge = cv2.merge([b, g, r])
cv2.imshow("Combined Picture", merge)

cv2.waitKey(0)
cv2.destroyAllWindows()