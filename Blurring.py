import cv2

star=cv2.imread("opencv-assets-main/star addition.jpeg")
diamond=cv2.imread("opencv-assets-main/diamond addition.jpeg")
vidcol1=cv2.imread("opencv-assets-main/videocollage1.jpg")
vidcol2=cv2.imread("opencv-assets-main/videocollage2.jpg")
people=cv2.imread("opencv-assets-main/people.jpeg")
resizedppl=cv2.imread("opencv-assets-main/resized people.jpg")
bilateral=cv2.imread("opencv-assets-main/bilateral.jpg")
swp=cv2.imread("opencv-assets-main/salt and pepper grains.jpeg")

# # addition
# add=cv2.addWeighted(vidcol1,1,vidcol2,0.5,0)
# cv2.imshow("window1",add)
# cv2.waitKey(0)

# # subtraction
# sub=cv2.subtract(vidcol1,vidcol2)
# cv2.imshow("window2",sub)
# cv2.waitKey(0)

# # resize
# resize=cv2.resize(people,(1501,1134))
# cv2.imwrite("resized people.jpg",resize)

# # overlay after resizing
# add2=cv2.addWeighted(vidcol1,1,resizedppl,0.2,0)
# cv2.imshow("window3",add2)
# cv2.waitKey(0)

# # common blur
# blur=cv2.GaussianBlur(bilateral,(31,31),sigmaX=3,dst=0)
# cv2.imshow("window4",blur)
# cv2.waitKey(0)

# # mid blur
# mb=cv2.medianBlur(swp,5)
# cv2.imshow("window5",mb)
# cv2.waitKey(0)

# bilateral blur
bb=cv2.bilateralFilter(bilateral,9,sigmaColor=35,sigmaSpace=25)
cv2.imshow("window6",bb)
cv2.waitKey(0)
