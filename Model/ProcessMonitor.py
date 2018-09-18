import datetime
import json
import threading
from time import sleep

# import psutil
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
            '''running_process = []
            for proc in psutil.process_iter(attrs=['pid', 'name']):
                if proc.info['name'] in self.black_list_process:
                    print("killed ", proc.info)
                    proc.kill()
                    ps = ProcessEvent(proc, datetime.datetime.now(), True)
                else:
                    ps = ProcessEvent(proc, datetime.datetime.now(), False)
                running_process.append(ps.event)'''
            try:

                s3 = boto3.client('s3')

                fields = {"acl": "public-read"}

                conditions = [
                    {"acl": "public-read"},
                    ["content-length-range", 30, 1000]
                ]

                post = s3.generate_presigned_post(
                    Bucket=self.api,
                    Key=self.key,
                    Fields=fields,
                    Conditions=conditions

                )
                
                files = {Screenshot: 'rb'}
                response = requests.post(post["https://" + self.api + "/process"], data=post["fields"], files=files,
                                         headers={"x-api-key": self.key})

                if response.ok:
                    self.black_list_process = list(map(lambda x: x.strip(), response.json().split(",")))
                else:
                    print(response.status_code)
                print(response.reason)
            except Exception as e:
                print(e)
            sleep(5)
