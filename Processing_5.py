IJ.selectWindow("Red channel");
IJ.run("Duplicate...", "title=[Red channel Processed 5] duplicate range=1-103");
IJ.selectWindow("Red channel Processed 5");
IJ.run("16-bit");
IJ.run("Auto Threshold", "method=[Try all] white");