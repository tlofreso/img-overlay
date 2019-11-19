import cv2

image = cv2.imread("tesla.jpg")

overlay = image.copy()
output = image.copy()

cv2.rectangle(overlay, (20, 20), (300, 150), (55, 55, 55), -1)
cv2.rectangle(overlay, (20, 980), (250, 1060), (55, 55, 55), -1)

cv2.addWeighted(overlay, .6, output, 1 - .6, 0, output)

cv2.imwrite("output.jpg", output)
