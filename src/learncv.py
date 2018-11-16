#!/usr/bin/env python
import sys
import cv2 as cv

# The path where all image resources all loaded from
LEARNCV_RESOURCE_PATH = sys.exec_prefix + "/../rsc/"

def cvread(path):
    ''' A convenience method that reads images using OpenCV from the resource path '''
    return cv.imread(LEARNCV_RESOURCE_PATH + path)

def main():
    print("Resource path: %s" % LEARNCV_RESOURCE_PATH)
    img = cvread('lena.png')
    print(img)

if __name__ == '__main__':
    main()