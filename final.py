import cv2
import numpy as np
import imutils
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--open-file', dest="opened_file", default=None, type=str)
parser.add_argument('-d', '--directory', dest="directory", default=None, type=str)
parser.add_argument('changed_file', type=str)
args = parser.parse_args()
opened_file, result_img, directory = args.opened_file, args.changed_file, args.directory
if opened_file is not None:
    flag_file = True
elif directory is not None:
    flag_file = False


def main(opened_file, result_img):
    img = cv2.imread(opened_file)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2XYZ)
    img = cv2.medianBlur(img, 5)
    lower = np.array((115, 120, 120), np.uint8)
    upper = np.array((120, 125, 125), np.uint8)
    mask2 = cv2.inRange(img, lower, upper)
    lower = np.array((80, 80, 80), np.uint8)
    upper = np.array((113, 132, 114), np.uint8)
    mask1 = cv2.inRange(img, lower, upper)
    lower = np.array((55, 58, 58), np.uint8)
    upper = np.array((74, 74, 74), np.uint8)
    mask3 = cv2.inRange(img, lower, upper)
    mask = cv2.bitwise_or(mask2, mask1)
    mask = cv2.bitwise_or(mask3, mask)
    contrs = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contrs = imutils.grab_contours(contrs)
    for c in contrs:
        M = cv2.moments(c)
        try:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
        except ZeroDivisionError:
            N = M["m00"]
            N += 1
            cX = int(M["m10"] / N)
            cY = int(M["m01"] / N)
        cv2.circle(img, (cX, cY), 7, (250, 128, 114), -1)

    img = cv2.cvtColor(img, cv2.COLOR_XYZ2BGR)
    cv2.imwrite(result_img, img)


def main_1(opened_file, result_img, flag):
    if flag:
        main(opened_file, result_img)
    else:
        for imagePath in os.listdir(opened_file):
            main(imagePath, os.path.join(result_img, 'result' + imagePath))


if __name__ == '__main__':
    main_1(opened_file, result_img, flag_file)
