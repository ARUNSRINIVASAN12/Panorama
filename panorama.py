import os
import cv2

path = "panorama"
images = []
for i in os.listdir(path):
    print(i)
    img = cv2.imread(f"{path}/{i}")
    img = cv2.resize(img, (0,0), None, 0.75, 0.75)
    images.append(img)

stitcher = cv2.Stitcher_create()
status, result = stitcher.stitch(images)

if status == cv2.STITCHER_OK :
    print("Panorama sucessfully created.")
    cv2.imshow("frame", result)
    cv2.waitKey(0)
else :
    print("Panorama unsuccessful")

   