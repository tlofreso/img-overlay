import numpy as np
import cv2


image = cv2.imread("tesla.jpg")

overlay = image.copy()
text = image.copy()
output = image.copy()

cv2.rectangle(overlay, (20, 20), (300, 150), (55, 55, 55), -1)
cv2.rectangle(overlay, (20, 980), (250, 1060), (55, 55, 55), -1)

# cv2.putText(text, "White", (25, 1055), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 3)

cv2.addWeighted(overlay, .6, output, 1 - .6, 0, output)
# output2 = output.copy()
# cv2.addWeighted(text, 1, output, 1 - 1, 0, output2)


cv2.imwrite("output.jpg", output)
# cv2.imwrite("output2.jpg", output2)

# loop over the alpha transparency values
# for alpha in np.arange(0, .6, 0.1)[::-1]:
#     overlay = image.copy()
#     output = image.copy()
    
#     cv2.rectangle(overlay, (20, 20), (250, 150), (55, 55, 55), -1)
#     cv2.rectangle(overlay, (20, 980), (180, 1060), (55, 55, 55), -1)

#     cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)


#     #print("alpha={}, beta={}".format(alpha, 1 - alpha))
#     cv2.imwrite("Output.jpg", output)
#     #cv2.waitKey(0)