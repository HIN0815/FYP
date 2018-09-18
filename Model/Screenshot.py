import time
import pyautogui
import numpy as np
import pyautogui
import imutils
import cv2
import time
import platform




class window():
    # Get the time and date
    timestr = time.strftime("%Y%m%d-%H%M%S")
    # Take screenshot
    pic = pyautogui.screenshot()

    # Save the image
    pic.save(str(timestr) + '.png')


class linux():
    timestr = time.strftime("%Y%m%d-%H%M%S")
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite(str(timestr) + '.png', image)


class Screenshot():
    if (platform.system() == 'Windows'):
        window()
    else:
        linux()