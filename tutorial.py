import time
import botpapy.botpapy as bp

# open an Microsoft Edge window (can't be minimized, but on 2nd desktop)
w1 = bp.Window("Edge", 3) # create window object
img = w1.takeScreenshot() # create image with takeScreenshot
img.show() # show the image
r = bp.Rect((400,0),30,30) # create Rectangle from point (x,y) and width,height
tpl = img.copy(r) # copy with rectangle as argument takes subimage
tpl.show() # show created template
matches = bp.findMatches(img, tpl, 0.95, 1) # opencv to find matches with treshhold and maximum count
c = bp.Color("red") # create a color to mark matches
bp.markMatches(img,matches, c) # mark the matches on the image
img.show() # show the result
w1.mouseClick(matches[0].center) # click the found match once
time.sleep(0.1) # give edge time to react
w1.takeScreenshot().show() # show result
