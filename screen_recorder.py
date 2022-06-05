# pip install Pillow
from PIL import ImageGrab
import numpy as np



while True:
     img = ImageGrab.grab(bbox=(0,0,1280,720))
     img_np = np.array(img)
     
