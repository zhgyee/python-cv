import sys
import cv2

def main(argv):
    if len(argv) < 3:
        print("usage:bootlogoconvert origin.bmp result.raw")
        return
    print("converting:" + argv[1])
    img = cv2.imread(argv[1])
    fo = open(argv[2], "wb")
    height = img.shape[0]
    width = img.shape[1]
    channels = img.shape[2]
    alpha = b'\xff'
    for row in range(height):
        for col in range(width):
            fo.write(img[row, col])
            fo.write(alpha)
    fo.close()
    
if __name__ == '__main__':
	main(sys.argv)
