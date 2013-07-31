from ij import IJ, ImagePlus, ImageStack  
  
# Load a stack of images: a fly brain, in RGB  
IJ.run("Image Sequence...", "open=/home/rhart/Desktop/Cell_Data/Data_Set_2/Fused_68_690004.tif number=103 starting=1 increment=1 scale=100 file=[] sort");
