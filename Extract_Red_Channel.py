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
  fp = cp.toFloat(0, None)  
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

#

