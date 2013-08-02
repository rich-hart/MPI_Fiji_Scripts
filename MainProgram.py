#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Richard Hart on 2013-08-02.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import os
from ij import IJ, ImagePlus, ImageStack  

def LoadData():
	IJ.run("Image Sequence...", "open=/home/rhart/Desktop/Cell_Data/Data_Set_2/Fused_68_690004.tif number=103 starting=1 increment=1 scale=100 file=[] sort")
	

def main():
	pass


if __name__ == '__main__':
	main()

