import datetime
import json
import threading
from time import sleep

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

            try:

                s3 = boto3.client('s3')
                photo = Screenshot+'.png'
                s3.put_object(
                    Bucket=self.api,
                    Key=photo,
                    ContentType='image/png'
                )
                url = s3.generate_presigned_url('get_object', Params={'Bucket': self.api, 'Key': photo})
                response = requests.get(url)

            except Exception as e:
                print(e)
            sleep(5)

    run('a')
