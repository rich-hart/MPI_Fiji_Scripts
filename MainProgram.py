#!/usr/bin/env python
# encoding: utf-8
"""
MainProgram.py

Created by Richard Hart on 2013-08-02.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import os
from ij import IJ, ImagePlus, ImageStack 
from ij.plugin.frame import RoiManager
from operator import itemgetter, attrgetter
from ij.gui import PolygonRoi, Roi
from ij.process import ImageStatistics
RED=0
GREEN=1
BLUE=2

imp = None

#load an image stack
def LoadData():
	file_path = "open=/home/rhart/Desktop/Cell_Data/Data_Set_2/Fused_68_690004.tif "
	IJ.run("Image Sequence...", file_path+"number=103 starting=1 increment=1 scale=100 file=[] sort")
	imp = IJ.getImage()
	imp.setTitle("Loaded Image")

	
def Extract_Red_Channel(color):
	IJ.selectWindow("Loaded Image");
	imp = IJ.getImage()
	stack = imp.getImageStack()  
	print "number of slices:", imp.getNSlices()  
	# A list of red slices  
	reds = []  
	# Iterate each slice in the stack  
	for i in xrange(1, imp.getNSlices()+1):  
	  # Get the ColorProcessor slice at index i  
	  cp = stack.getProcessor(i)
	  # Get its green channel as a FloatProcessor  
	  fp = cp.toFloat(color, None)  
	  # ... and store it in a list  
	  reds.append(fp)  
	# Create a new stack with only the green channel  
	stack2 = ImageStack(imp.width, imp.height)  
	for fp in reds:  
	  stack2.addSlice(None, fp)  
	# Create a new image with the stack of green channel slices  
	imp2 = ImagePlus("Red channel", stack2)  
	# Set a green look-up table:  
	IJ.run(imp2, "Red", "")  
	imp2.show()  	


def Processing_Type_1():
	IJ.selectWindow("Red channel");
	IJ.run("Duplicate...", "title=[Red channel Processed 1] duplicate range=1-103");
	IJ.selectWindow("Red channel Processed 1");
	#IJ.setAutoThreshold("Default dark");
	#IJ.run("Enhance Contrast...", "saturated=0.4 normalize process_all");
	#IJ.run("16-bit");
	IJ.run("Convert to Mask", "method=Huang background=Dark calculate");
	IJ.run("Dilate","stack")
	IJ.run("Dilate","stack")
	IJ.run("Close-","stack")
	IJ.run("Erode","stack")
	IJ.run("Erode","stack")
	IJ.run("Despeckle", "stack");
	


def ConnectedRegions():
	IJ.selectWindow("Red channel Processed 1");
	IJ.run("Find Connected Regions", "allow_diagonal display_image_for_each display_one_image display_results regions_for_values_over=100 minimum_number_of_points=100000 stop_after=3");


regions_array=[]
rm = RoiManager()
def RoiSelection(index):
	imp_roi = IJ.getImage()
	#IJ.run("Invert", "stack");
	IJ.run("Fill Holes", "stack");
	IJ.run("Create Selection");
	rm.runCommand("add")
	rm.runCommand("split")
	#number_selected=rm.getCount()
	IJ.run("Select None");
	rm.runCommand("deselect")
	#rm.select(0)
	#print number_selected
	roi_array=rm.getRoisAsArray()
	max_roi=None
	max_points=-1
	for roi in roi_array:
	  polygon=roi.getPolygon()
	  if polygon is not None:
		stats = imp_roi.getStatistics(ImageStatistics.AREA)
		number_of_points = polygon.npoints
		if max_points < stats.area:
			max_points=number_of_points
			max_roi=roi
	#print max_points
	#sorted_roi_array=sorted(roi_array, key=methodcaller('getLength'), reverse=True)
	#length_array=[]
	#index=0
	#for roi in roi_array:
	#	index=index+1
	#	length_array.append((index,roi.getLength()))
	#sorted_length_array=sorted(length_array, key=itemgetter(0))
	rm.runCommand("Select All")
	rm.runCommand("Delete")
	#for roi in roi_array:
	interpolated_polygon=max_roi.getInterpolatedPolygon(20,True)
	roi_polygon=PolygonRoi(interpolated_polygon,Roi.POLYGON)
	roi_polygon.setName(str(index))
	roi_polygon.setImage(imp)
	roi_polygon.setPosition(index)
	regions_array.append(roi_polygon)
	#rm.addRoi(roi_polygon)
	#imp = IJ.getImage()
	#roi = imp.getRoi()
	#p = roi.getPolygon()
	#peterimeter = roi.getLength()
	#p.npoints
	#rm.sort()
	#rm.split();
	#print rm 
	#for i in range(1,p.npoints):
	#	print "(" + str(p.xpoints[i]) + "," + str(p.ypoints[i]) + ")"
	#IJ.run("Create Selection");
	#IJ.run("Make Band...", "band=9");
	#roi = imp.getRoi()
	#p=roi.getPolygon()
	#print "Total number of points in ROI " + str(p.npoints)


def LoadRoi():
	IJ.selectWindow("Loaded Image")
	rm.runCommand("Select All")
	rm.runCommand("Deselect")
	index = 0
	for rio_polygon in regions_array:
		index=index+1
		rm.addRoi(rio_polygon)
		IJ.run("Next Slice [>]")
	rm.moveRoisToOverlay(imp)
	#sdas

def main():
	LoadData()
	Extract_Red_Channel(RED)
	Processing_Type_1()
	#ConnectedRegions()
	for i in range(1,103):
		IJ.selectWindow("Red channel Processed 1")
		IJ.run("Next Slice [>]")
		RoiSelection(i)
	LoadRoi()


if __name__ == '__main__':
	main()

