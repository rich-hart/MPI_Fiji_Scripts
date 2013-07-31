IJ.selectWindow("Red channel");
IJ.run("Duplicate...", "title=[Red channel Processed] duplicate range=1-103");
IJ.selectWindow("Red channel Processed");
IJ.run("16-bit");
IJ.run("Enhance Contrast...", "saturated=0.4 normalize process_all use");
IJ.run("Convert to Mask", "method=Huang background=Dark calculate");
IJ.run("Despeckle", "stack");