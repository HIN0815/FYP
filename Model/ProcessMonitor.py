import datetime
import json
import threading
from time import sleep

import psutil
import requests
from Model.Screenshot import *
from Model.Event import ProcessEvent


class ProcessMonitor(threading.Thread):

    def __init__(self, api: str, key: str):
        super().__init__()
        self.name = "ProcessMonitor"
        self.api = api
        self.key = key
        self.black_list_process = []

    def run(self):
        while True:

            try:

                response = requests.post("https"+self.api+"/process",
                                         headers={ "x-api-key": self.key})

                files = {
                    'file': ('D:\\Screenshot.png',
                             open('D:\\Screenshot.png', 'rb'), 'image/png', {'Expires': '0'})}
                if response.ok:
                    print(response.json())
                    upload = response.json()

                    r = requests.post(upload, files=files)
                    print(r.text)

                else:
                    print(response.status_code)
                    print(response.reason)


            except Exception as e:
                print(e)
            sleep(5)

    
