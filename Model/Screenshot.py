
import time


# Get the time and date
timestr = time.strftime("%Y%m%d-%H%M%S")
class window():
    import pyautogui
    # Take screenshot
    pic = pyautogui.screenshot()

    # Save the image
    pic.save( str(timestr) + '.png')

class linux():
    import numpy as np
    import pyautogui
    import imutils
    import cv2
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite( str(timestr) + '.png', image)

