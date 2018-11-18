#!/usr/bin/env python

import sys
import cv2 as cv

# The path where all image resources all loaded
PS1_RESOURCE_PATH = sys.exec_prefix + "/../rsc/ps1/"

def main():
    img = cv.imread(PS1_RESOURCE_PATH + 'ps1-input0.png')
    cv.imshow('Input0', img)

    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    main()