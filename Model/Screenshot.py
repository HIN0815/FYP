import time
import pyautogui

import time


class Screenshot():
    # Get the time and date
    timestr = time.strftime("%Y%m%d-%H%M%S")
    # Take screenshot
    pic = pyautogui.screenshot()

    # Save the image
    pic.save(str(timestr) + '.png')
