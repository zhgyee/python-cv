import cv2

img = cv2.imread("bootlogo.bmp")

fo = open("result.dat", "wb")

print(img.shape)
height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]
alpha = b'\xff'
for row in range(height):
    for col in range(width):
        #for c in range(channels):
        fo.write(img[row, col])
        fo.write(alpha)

#cv2.namedWindow("test")
#cv2.imshow("test", img)
#cv2.waitKey(0)
fo.close()
cv2.destroyAllWindows()
