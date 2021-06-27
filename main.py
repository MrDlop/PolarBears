import argparse
from cv2 import cv2

parser = argparse.ArgumentParser()
parser.add_argument('opened_file', type=str)
parser.add_argument('changed_file', type=str)
args = parser.parse_args()
opened_file, changed_file = args.opened_file(), args.changed_file()
