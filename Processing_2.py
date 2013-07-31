IJ.selectWindow("Red channel");
IJ.run("Duplicate...", "title=[Red channel Processed] duplicate range=1-103");
IJ.selectWindow("Red channel Processed");
IJ.run("Sharpen", "stack");
IJ.run("16-bit");
IJ.run("Enhance Contrast...", "saturated=0.4 normalize equalize process_all");
IJ.run("Convert to Mask", "method=MaxEntropy background=Dark calculate");
