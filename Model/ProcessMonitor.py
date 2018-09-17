import datetime
import json
import threading
from time import sleep
import platform
import psutil
import requests
from Model.Screenshot import *
import boto3
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
            if(platform.system()=='Windows'):
                window()
            else:
                linux()
            s3 = boto3.resource('s3')
            bucket = s3.Bucket('')
            obj = bucket.Object(self.key )

            try:
                with open('filename', 'rb') as data:
                    obj.upload_fileobj(data)
            except Exception as e:
                print(e)

            sleep(5)

