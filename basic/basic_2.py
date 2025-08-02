import cv2

cap = cv2.VideoCapture("../video_file.mp4") #for webcam use 0

while True:
    success, frame = cap.read()
    if not success:
        break
    cv2.imshow("video", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()