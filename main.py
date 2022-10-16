# install opencv-python
# haarcascade_frontalface_default.xml

import cv2

# the face classifier
cascade_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# camera access
cap = cv2.VideoCapture(0)

# to make the detection stay
while True:
    ret, img = cap.read()
    print(ret)

# converting color to greyscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detecting the multiscale
    faces = cascade_face.detectMultiScale(gray, 1.3, 4)


# for the grid of the rectangle
    for (x, y, w, h) in faces :
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 4)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

# conditions
    cv2.imshow('Face Detector', img)
    k = cv2.waitKey(30) & 0xff

    if k == 27:
        break

cap.release()

# will close the all the windows popping up
cv2.destroyAllWindows()


























