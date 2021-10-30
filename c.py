import cv2
from IPython.display import Image, display
from ipywidgets import interact,widgets
import numpy as np

img = cv2.imread("p.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
num_channels = 1 if img.ndim == 2 else img.shape[2]
parts = {}

def imshow(img):
 ret,encoded=cv2.imencode(".png",img)
 display(Image(encoded))

def inRange(**kwargs):
 lower = tuple([int(l) for l, h in kwargs.values()])
 upper = tuple([int(h) for l, h in kwargs.values()])
 binary = cv2.inRange(img, lowerb=lower, upperb=upper)
 imshow(binary)

for i in range(num_channels):
 slider = widgets.SelectionRangeSlider(options=np.arange(256),index=(0, 255), description=f"channel {i}") 
 slider.layout.width = "400px"
 parts[f"channel{i}"] = slider

interact(inRange, **parts)

