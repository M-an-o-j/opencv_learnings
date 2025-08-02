import cv2

img = cv2.imread("../image.jpg")
cv2.imshow("My example image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("image_copy.jpg",img)