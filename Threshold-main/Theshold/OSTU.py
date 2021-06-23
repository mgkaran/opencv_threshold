import cv2

img=cv2.imread(r'C:\Users\sange\Downloads\news.jpg')
gray_conversion=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray_show=cv2.imshow("Gray image",gray_conversion)
cv2.waitKey(0)
value,OSTU=cv2.threshold(gray_conversion,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print("The Threshold Value={}".format(value))
cv2.imshow("Newspaper",OSTU)
cv2.waitKey(0)
cv2.imwrite("ostu.jpg",OSTU)
