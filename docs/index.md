# Documentation for botpapy
```python
import botpapy.botpapy as bp
```
[Window Class](#window-class)

[Image Class](#image-class)

[General Functions](#general-functions)

[Rect Class](#rect-class)

[Match Class](#match-class)

[Color Class](#color-class)

# Tutorial
```python
import time
import botpapy.botpapy as bp
# open an Microsoft Edge window (can't be minimized, but on 2nd desktop)
w1 = bp.Window("Edge", 2) # create window object #
img = w1.takeScreenshot() # create image with takeScreenshot
img.show() # show the image
r = bp.Rect((300,10),30,30) # create Rectangle from point (x,y) and width,height
tpl = img.copy(r) # copy with rectangle as argument takes subimage
tpl.show() # show created template
matches = bp.findMatches(img, tpl, 0.95, 2) # opencv to find matches with treshhold and maximum count
c = bp.Color("red") # create a color to mark matches
bp.markMatches(img,matches, c) # mark the matches on the image
img.show() # show the result
w1.mouseClick(matches[0].center) # click the found match once
time.sleep(0.5) # give program time to react
w1.takeScreenshot().show() # show result
```

____
# Window Class
Create a Window to handle, might also pass hex id (as number) of window.

If a name is passed and mutliple windows are found (checks for substring), a dialogue for the choice between them (and a screenshot of each) will be opened.

If the result is a black screen try a different layer.
```python
# Window = Window(name, layer:int = 1)
w1 = bp.Window("Chrome") # create Window from name
w1 = bp.Window(0x504f4) # create Window from hex id
```

## takeScreenshot
Takes screenshot of windows
```python
# Image = window.takeScreenshot()
img = w1.takeScreenshot
```
returns: `Image`

## mouseClick
Sends a mouse click event to a window
```python
# window.mouseClick((x,y),button="left") # or button="right","middle"
w1.mouseClick((120,33)) # uses left by default
w1.mouseClick((612,340), button="right")
```

## click
Directly left click a template, given a threshhold
```python
# window.click(tpl: Image, trsh: float)
tpl = bp.Image("tpl.png")
w1.click(tpl, 0.95)
```

## moveMouse
Send a mouse move to a location event
```python
# window.moveMouse((x,y))
w1.moveMouse((300,300))
```

## hoverMouse
Move mouse multiple times around a specific point. Might be needed to create a hover reaction from some windows.
```python
# window.hoverMouse((x,y), iterations:int)
w1.hoverMouse((300,300), 5)
```

## pressButtons
Send a sequence of button press events
```python
# window.pressButtons(s:str)
w1.pressButtons("asd")
```

## holdButton
Hold a button for a certain amount of seconds (is blocking)
```python
# window.holdButton(c:str[len==1], time:float)
w1.holdButton("a", 3) # hold button a for 3 seconds
```

___
# Image Class
Read, create, store and show images. Opencv images are used, underlying datastructure: ndarray
```python
# Image = Image(name:str)
img1 = bp.Image("test.png") # create Image from file
img2 = w1.takeScreenshot() # create Image by taking a screenshot
img = img1 # create Image from other Image
```

## save
Save an image.
```python
# image.save(name:str)
img.save("result.png")
```

## getSize/size
Get dimensions of an image
```python
# width, height = image.getSize()
r = img.getSize()
w,h = img.size
```
returns `[width, height]`

## getPixelColor
Get the color of a pixel at a position.
```python
# c:Color = image.getPixelColor((x,y))
col = img.getPixelColor((42,42))
```
returns `Color`

## setPixelColor
Set the color of a pixel at a position.
```python
# c:Color = image.setPixelColor((x,y), c:Color)
col = bp.Color("red")
img.setPixelColor((42,42),col)
```

## copy
Copy an image, option to take subarea.
```python
# img2:Image = image.copy(r:Rect)
img4 = img.copy()
r = bp.Rect((40,30),120,600)
img5 = img.copy(r)
```
returns `Image`

## show
Displays an image until any key is pressed.
```python
# image.show()
img4.show()
```

## isolateColorRange
Isolate a certain color range to possibly make matching easier. Stores the created mask back in the image object.
```python
# image.isolateColorRange(c1:Color, c2:Color, keep_color: bool)
c1 = bp.Color((41, 145, 43), hsv=True)
c2 = bp.Color((180, 218, 210), hsv=True)
img4.isolateColorRange(c1, c2) # returns black/white image
img5.isolateColorRange(c1, c2, True) # returns colored image
```

___
# General Functions
Functions that are in no particular class

## findMatches
Function to find maximum coordinates of template matching of template on image with minimum threshhold and maximum number
```python
# List(Match) = botpapy.findMatches(img:Image, tpl:Image, trsh, max:int)
img = w1.takeScreenshow()
tpl = bp.Image("tpl_1.png")
matches = bp.findMatches(img, tpl, 0.95, 3)
```
returns: `List(Match)` - List of Match objects

## markMatches
Used to mark found matches on the image.
```python
# markMatches(img:Image, matches, color:Color, thickness:int = 2)
matches = bp.findMatches(img, tpl, 0.95, 3)
img.markMatches(img, machtes, bp.Color("red"), 1)
```

## crangeTester
Used to choose hsv colors to isolate a color range from an image. Opens file dialogue if no file is parsed.
```python
# bp.crangeTest(filename: str)
bp.crangeTest()
bp.crangeTest("img.png")
```

## listWindows
Function to print all window names, to resolve eventual confusion of not found windows.
```python
# bp.listWindows(visible: bool)
bp.listWindows()
```

___
# Rect Class
Class to store coordinates of a rect. Can be created by one point, width and height or two points (the order of the two points doesn't matter).

```python
# Rect r = bp.Rect((x,y),(x,y))
# Rect r = bp.Rect((x,y),width,height)
r1 = bp.Rect((300,300),50,50)
r2 = bp.Rect((50,50),(300,25))
```

## getCenter/center
Returns the center point of the rect.

```python
# (x,y) = rect.getCenter()
x,y = rect.center
r = rect.getCenter()
```
returns: `(x,y)`

## getTopLeft/topleft
Returns the top left point of the rect.
```python
# (x,y) = rect.getTopLeft()
x,y = rect.topleft
r = rect.getTopLeft()
```
returns: `(x,y)`

___
# Match Class
Stores found matches in a match object using a Rect and its score.
```python
# Match m = bp.Match(rect: Rect, score)
r = bp.Rect((0,0),(300,100))
m = bp.Match(r, 0.97)
```

## getCenter/center
Returns the center point of the match (its rect).
```python
# (x,y) = match.getCenter()
x,y = m.center
r = m.getCenter()
```
returns: `(x,y)`

## getRect
Returns the Rect which the match is based on.
```python
# Rect r = match.getRect()
r = match.getRect()
```
returns: `Rect`

___
# Color Class
Stores a color in its rgb and hsv values. These can be passed as one tuple or three individual values. Initialization also with five very simple color names possible.
```python
# Color col = bp.Color("red") # or black, blue, green, white
# Color col = bp.Color(r,g,b)
# Color col = bp.Color(h,s,v, hsv=True)
blue = bp.Color("blue")
green = bp.Color(0,255,0)
hsvcolor = bp.Color(25,60,230, hsv=True)
```

## getRGB/rgb
Used to get the rgb values of the color.
```python
# (r,g,b) = col.getRGB()
r,g,b = col.rgb
res = col.getRGB()
```

## getBGR/bgr
Used to get the bgr values of the color.
```python
# (b, g, r) = col.getBGR()
b,g,r = col.bgr
res = col.getBGR()
```

## hsv
Used to get the hsv values of the color.
```python
# (h, s, v) = col.hsv
h,s,v = col.hsv
```