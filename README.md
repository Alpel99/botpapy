# Python Library to automate tasks with template matching in (non-visible) windows 
### heavily inspired by [Botfather](https://botfather.io/)  
### uses win32gui -> only works on windows

# Features
* List window titles
* Select window by name/title
    * if multiple found -> choice dialogue
* Taking Screenshots of window
* Use python cv2 wrapper for template matching
* Send mouse/keyboard events to window
* Isolate color ranges

# Classes
* Window
* Image
* Match
* Rect
* Color
* Points should be used as tuples (x,y)
* General functions:
    * findWindow, listWindows
    * findMatches, markMatches
    * crangeTest

# Documentation
* (coming soon): see Github Pages

# General
* Some windows might not generate any image while minimized:
    * move them to a second desktop in windows `⊞ Win + Tab`
    * keep them "open" there
* If there are only black squares as pictures try a different layer variable for _checkWindowNames_
* This is (not yet) tested on a bigger scale:
    * definitely not full functionality for controls
    * might have bugs
    * performance might be horrible

# Dependencies
* `pip install numpy opencv-python Pillow pywin32`
* hope nothing is missing


