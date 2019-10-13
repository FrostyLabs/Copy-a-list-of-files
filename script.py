#!/usr/bin/python3
"""
I made this short python script to copy "highlight"
pictures to upload to our Facebook page
"""
import os
from shutil import copyfile

# Directories
srcFolder = r'C:\\path\\to\\src\\'
dstFolder = r'C:\\path\\to\\dst\\'

# Define Images
imgList = ['IMG_4993.JPG', 'IMG_5060.JPG'] # example list with only 2 images

# Copy files to new folder
for file in os.listdir(srcFolder):
    if file in imgList:
        copyfile(srcFolder+file, dstFolder+file)
        print("[+] Copy of {} complete!".format(file))

# Count number of pictures
count=0
for i in imgs:
    count=count+1
print("Expect {} pictures to be moved".format(count))
