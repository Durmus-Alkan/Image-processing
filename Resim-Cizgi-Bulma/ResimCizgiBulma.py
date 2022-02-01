#İlk çalıştırılma sırasında yaklaşık 15 saniye beklemek gerekiyor.
#q ile çıkılabilir. Çarpi tuşu ile çıkılamaz

import cv2
import numpy as np

kamera=cv2.VideoCapture(0)
kamera.set(cv2.CAP_PROP_FRAME_WIDTH,640)
kamera.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

def nothing(x):
    pass

cv2.namedWindow('image')

cv2.createTrackbar('Trashold 1','image',0,255,nothing)
cv2.createTrackbar('Trashold 2','image',0,255,nothing)

while True:
    t1 = cv2.getTrackbarPos('Trashold 1', 'image')
    t2 = cv2.getTrackbarPos('Trashold 2', 'image')
    ret,goruntu=kamera.read()
    canny = cv2.Canny(goruntu, t1,t2)
    cv2.imshow('image', canny)
    k = cv2.waitKey(1) & 0xFF


    if cv2.waitKey(25) & 0xFF ==ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()

