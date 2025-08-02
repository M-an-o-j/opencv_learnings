import cv2

img = cv2.imread('../image.jpg')  # replace with your image path

#Convert BGR to Grayscale
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Gray", gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Convert BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()
