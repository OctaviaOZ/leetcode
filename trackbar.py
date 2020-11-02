import cv2 as cv
import argparse
import os
import numpy as np

OUTPUT_FOLDER_IMAGES = os.path.sys.path[00]

def change(x):
    # print(x)
    pass

def trackbar(image_path: object):

    switch = '0: OFF\n 1: ON'

    original = cv.imread(image_path)
    # Canny edge detection.
    #edges = cv.Canny(img, 50, 100)

    img = np.zeros(original.shape, np.uint8)
    cv.namedWindow("image")

    cv.createTrackbar('B', 'image', 0, 255, change)
    cv.createTrackbar('G', 'image', 0, 255, change)
    cv.createTrackbar('R', 'image', 0, 255, change)

    cv.createTrackbar(switch, 'image', 0, 1, change)

    while True:
        cv.imshow("image", img)
        k = cv.waitKey(1) & 0xFF
        if k == 27:
            break

        b = cv.getTrackbarPos('B', 'image')
        g = cv.getTrackbarPos('G', 'image')
        r = cv.getTrackbarPos('R', 'image')
        s = cv.getTrackbarPos(switch, 'image')

        if s == 0:
            img[:] = 0
        else:
            img[:] = [b, g, r]

    cv.destroyAllWindows()


if __name__ == '__main__':

    # PARAMETERS
    parser = argparse.ArgumentParser()
    parser.add_argument("--image_name", type=str, help="process image", required=True)
    args = parser.parse_args()

    if args.image_name:
        image_path = args.image_name

        IMAGE_PATH = OUTPUT_FOLDER_IMAGES + "\\" + image_path

        if os.path.exists(IMAGE_PATH):
            trackbar(image_path=IMAGE_PATH)
        else:
            print(f"\n{IMAGE_PATH} not exists")
    else:
        print("\nDid not find --folder_name argument")