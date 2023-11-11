# -*- coding: utf-8 -*-
"""
save_vol.py

Loads in the phase-coherence images and saves a 3D volume as a .npz file
"""

import numpy as np 
import cv2 as cv 
from os.path import join
import os

#path of the images
path = r'Images'
folder = r'cropped' 
saving_folder = r'Results'

in_path=join(path,folder)
entries = os.listdir(in_path)
image_path = join(in_path,entries[28]) #Selected image
savedimage_path = join(path,saving_folder)
I=cv.imread(image_path,0)
vol = np.zeros((I.shape[0],I.shape[1],len(entries)),np.uint8)

for ith in range (len(entries)):
    print(f"Loading image {image_path}")
    image_path = join(in_path,entries[ith])
    I = cv.imread(image_path,0)
    vol[:,:,ith] = I

# Write the sorted coordinates to the CSV file
npz_file = 'vol.npz'
print(f"Saving {npz_file}")
np.savez(npz_file, vol=vol)
print("Done!")
