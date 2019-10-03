#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 23:59:41 2019

@author: ritz
"""
import cv2

from cursive.image_straighten import image_straighten
from cursive.center_align import center_align
from cursive.segmentation import segmentation
from cursive.model_build import model_build
from cursive.recognition import recognition

build_model = 0 # Model already exists
def main(path):
    # img = cv2.imread('cursive/sample_images/c.png')
    img = cv2.imread(path)
    image_straighten(img)
    segmentation(img)
    folder='cursive/result/characters/'
    center_align(folder)
    
#    Fix model building and recognition later
    if (build_model != 0):
        model_build()
    rec_char = []
    rec_char = recognition()
    return rec_char

#if __name__ == '__main__':
#    main()