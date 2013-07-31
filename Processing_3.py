IJ.selectWindow("Red channel");
IJ.run("Duplicate...", "title=[Red channel Processed] duplicate range=1-103");
IJ.selectWindow("Red channel Processed");
IJ.run("Convert to Mask", "method=MinError background=Dark calculate");
IJ.run("Invert", "stack");
IJ.run("Despeckle", "stack");
IJ.run("Invert", "stack");