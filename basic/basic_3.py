import cv2

img = cv2.imread("../image.jpg")

#resize
# resized = cv2.resize(img, (300,200)) # (width, height)
# cv2.imshow("My example image",resized)

#crop
cropped = img[100:300, 200:400]  # [y1:y2, x1:x2]
cv2.imshow("My example image",cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()