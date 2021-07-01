import cv2
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('opened_file', type=str)
parser.add_argument('changed_file', type=str)
args = parser.parse_args()
opened_file, result_img = args.opened_file(), args.changed_file()

img = cv2.imread(opened_file)
img = cv2.cvtColor(img, cv2.COLOR_BGR2XYZ)
img = cv2.medianBlur(img, 5)
lower = np.array((80, 80, 80), np.uint8)  # нужно менять этот дипазон
upper = np.array((113, 132, 114), np.uint8)  # и этот тоже
mask1 = cv2.inRange(img, lower, upper)
lower = np.array((115, 120, 120), np.uint8)  # нужно менять этот дипазон
upper = np.array((120, 125, 125), np.uint8)  # и этот тоже
mask2 = cv2.inRange(img, lower, upper)
lower = np.array((55, 58, 58),np.uint8)
upper = np.array((74, 74, 74), np.uint8)
mask3 = cv2.inRange(img, lower, upper)
mask = cv2.bitwise_or(mask2, mask1)
mask = cv2.bitwise_or(mask3, mask)
contrs, hier = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contrs, -1, (0, 0, 0), 1)
img = cv2.cvtColor(img, cv2.COLOR_XYZ2BGR)
cv2.imwrite("Image.jpg", img)