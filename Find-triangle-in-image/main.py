import numpy as np
import cv2
#cv2.findContours() kullandık. Bu, pixellerin aynı renkte sıralı olarak devam edip etmediğini buluyor

ucgen_sayi=0  #Üçgen sayısını saymak için

img = cv2.imread('shape3.png')
imgGry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Renkleri beyaz ve siyaha döndürdük

ret , thrash = cv2.threshold(imgGry, 240 , 255, cv2.CHAIN_APPROX_NONE)
contours , hierarchy = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours: #resimdeki tüm pixelleri tek tek geziyor. aynı olan pixeller olduğunda tutuyor. 3 noktada birleşmiş ise sürekli pixeller üçgen olarak sayıyor
    approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 5

    # 3 noktada birleşen ve arasında farklı renkte pixel bulunmayan resimleri üçgen olarak alıyor
    if len(approx) == 3:
        ucgen_sayi = ucgen_sayi+1

#Üçgen vardır ya da yoktur demek için if kullandım
if ucgen_sayi > 0:
    print("Resimde ", ucgen_sayi , " üçgen", "vardır")
else:
    print("Resimde üçgen yoktur")

#Resmi gösteriyor
cv2.imshow('shapes', img)
#resmin ekranda kalmasını sağlıyor
cv2.waitKey(0)
#resmin pencerede açılmasını sağlıyor
cv2.destroyAllWindows()