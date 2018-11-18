#!/usr/bin/env python

import sys
import cv2 as cv
import numpy as np
import random as rd

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

def nChannels(img):
    ''' Return the number of channels an image has '''
    n = len(img.shape)
    return 1 if n == 2 else img.shape[2]

def intensify(img, scalar):
    ''' Intensify each color channel in the image by applying a scalar value. This returns a new image. '''
    for i in range(0, nChannels(img)):
        img[:,:,i] = [x * scalar for x in img[:,:,i]]

def boxBlur(img, ksize = 3):
    ''' Use a normalized box filter to blur the image. This returns a new image. '''
    return cv.boxFilter(img, -1, (ksize, ksize))

def gausBlur(img, sigmaX, sigmaY = 0.0, ksize = 3):
    ''' Uses a gaussian box filter to blur the image. This returns a new image. '''
    return cv.GaussianBlur(img, (ksize, ksize), sigmaX, sigmaY)

def median(img, ksize = 3):
    return cv.medianBlur(img, ksize)

def saltAndPepper(img, prob):
    result = np.zeros(img.shape, np.uint8)
    thres = 1 - prob
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            n = rd.random()
            if n < prob:
                result[i][j] = 0
            elif n > thres:
                result[i][j] = 255
            else:
                result[i][j] = img[i][j]
    return result

def templateMatch(mask, img, method = cv.TM_CCOEFF_NORMED):
    ''' Return the coefficient image from the template matching and the original image overlaid with a rectangle showing the area of highest match. '''
    res = cv.matchTemplate(img, mask, method)
    minV, maxV, minLoc, maxLoc = cv.minMaxLoc(res)
    
    # These two methods use the lowest score as the best match
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        topLeft = minLoc
    else:
        topLeft = maxLoc

    h, w, c = mask.shape[::]
    bottomRight = (topLeft[0] + w, topLeft[1] + h)
    return res, cv.rectangle(img, topLeft, bottomRight, 255)

def main():
    print("Resource path: %s" % LEARNCV_RESOURCE_PATH)
    lena = cvread('lena.png')
    fruit = cvread('fruit.png')
    lips = cvread('lips.png')

    cv.imshow('Combined', blend(lena, fruit, 0))
    cv.imshow('Fruit', fruit)
    cv.imshow('Box Blurred Fruit', boxBlur(fruit, 10))
    cv.imshow('Gaussian Blurred Fruit', gausBlur(fruit, 5.0, 5.0, 11))
    cv.imshow('Median Blurred Fruit', median(fruit, 11))
    cv.imshow('Salt and Pepper', saltAndPepper(fruit, 0))
    cv.imshow('Blended salt and pepper lena', blend(lena, saltAndPepper(lena, 0.03)))

    template, result = templateMatch(lips, lena)
    cv.imshow('Lena template', template)
    cv.imshow('Lena lips', result)

    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    main()