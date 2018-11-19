#!/usr/bin/env python

import sys
import cv2 as cv

# The path where all image resources all loaded
PS1_INPUT_PATH = sys.exec_prefix + "/../rsc/ps1/input/"

# The path where we write all result images
PS1_OUTPUT_PATH = sys.exec_prefix + "/../rsc/ps1/output/"

def read(path, mode = cv.IMREAD_COLOR):
    return cv.imread(PS1_INPUT_PATH + path, mode)

def write(path, img):
    cv.imwrite(PS1_OUTPUT_PATH + path, img)

def prob1():
    img = read('ps1-input0.png', cv.IMREAD_GRAYSCALE)
    edge = cv.Canny(img, 100, 200)
    write('ps1-1-a-1.png', edge)

def main():
    prob1()

if __name__ == '__main__':
    main()