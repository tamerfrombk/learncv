#!/usr/bin/env python
import sys
import cv2 as cv

# The path where all image resources all loaded from
LEARNCV_RESOURCE_PATH = sys.exec_prefix + "/../rsc/"

def cvread(path):
    ''' A convenience method that reads images using OpenCV from the resource path '''
    return cv.imread(LEARNCV_RESOURCE_PATH + path)

def showAndWait(title, img):
    cv.imshow(title, img)
    cv.waitKey(0)
    cv.destroyAllWindows()

def split(img):
    ''' Return three brand new images representing each color channel of the image. Returned order is B, G, R '''
    bgr = cv.split(img)
    return bgr[0], bgr[1], bgr[2]

def blend(i1, i2, alpha = 0.5):
    ''' A simple blending of two images using linear blending. Both images must be same size and type. '''
    return cv.addWeighted(i1, alpha, i2, 1 - alpha, 0.0)

def main():
    print("Resource path: %s" % LEARNCV_RESOURCE_PATH)
    lena = cvread('lena.png')
    fruit = cvread('fruit.png')

    b, g, r = split(lena)
    cv.imshow('Lena B', b)
    cv.imshow('Lena G', g)
    cv.imshow('Lena R', r)

    cv.imshow('Combined', blend(lena, fruit, 0))
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    main()