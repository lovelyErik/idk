import cv2
imageContainer=cv2.imread("yum.jpg")
cv2.imshow("displayimage",imageContainer)
cv2.waitKey(0)

print(imageContainer)
