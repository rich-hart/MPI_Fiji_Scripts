from ij.plugin.frame import RoiManager
from operator import itemgetter, attrgetter
from ij.gui import PolygonRoi, Roi
true=1
false=0
IJ.run("Invert", "stack");
IJ.run("Fill Holes", "stack");
IJ.run("Create Selection");
rm = RoiManager()
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
    number_of_points = polygon.npoints
    if max_points < number_of_points:
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


rm.addRoi(roi_polygon)


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