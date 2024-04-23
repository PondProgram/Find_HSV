import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(1)

cv2.createTrackbar("Lower - Hue", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("Lower - Saturation", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("Lower - Value", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("Upper - Hue", "Trackbars", 179, 179, nothing)
cv2.createTrackbar("Upper - Saturation", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("Upper - Value", "Trackbars", 255, 255, nothing)

while True:
   
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("Lower - Hue", "Trackbars")
    l_s = cv2.getTrackbarPos("Lower - Saturation", "Trackbars")
    l_v = cv2.getTrackbarPos("Lower - Value", "Trackbars")
    u_h = cv2.getTrackbarPos("Upper - Hue", "Trackbars")
    u_s = cv2.getTrackbarPos("Upper - Saturation", "Trackbars")
    u_v = cv2.getTrackbarPos("Upper - Value", "Trackbars")
    cv2.namedWindow("Trackbars")
   
    lower_range = np.array([l_h, l_s, l_v])
    upper_range = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, lower_range, upper_range)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    mask_rgb = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

    stacked = np.hstack((frame, mask_rgb, res))
    resized_stacked = cv2.resize(stacked, None, fx=0.7, fy=0.7)
    cv2.imshow('Find_HSV', resized_stacked)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
