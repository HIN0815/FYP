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
            running_process = []
            for proc in psutil.process_iter(attrs=['pid', 'name']):
                if proc.info['name'] in self.black_list_process:
                    print("killed ", proc.info)
                    proc.kill()
                    ps = ProcessEvent(proc, datetime.datetime.now(), True)
                else:
                    ps = ProcessEvent(proc, datetime.datetime.now(), False)
                running_process.append(ps.event)
            try:
                if (platform.system() == 'Windows'):
                    screen=window()
                else:
                    screen =linux()
                # Get the service client
                s3 = boto3.client('s3')

                # Make sure everything posted is publicly readable
                fields = {"acl": "public-read"}

                # Ensure that the ACL isn't changed and restrict the user to a length
                # between 10 and 100.
                conditions = [
                    {"acl": "public-read"},
                    ["content-length-range", 10, 100]
                ]

                # Generate the POST attributes
                post = s3.generate_presigned_post(
                    Bucket='bucket-name',
                    Key=self.key,
                    Fields=fields,
                    Conditions=conditions
                )

                files = {"file": screen}
                response = requests.post(post["url"], data=post["fields"], files=files)
                if response.ok:
                    self.black_list_process = list(map(lambda x: x.strip(), response.json().split(",")))
                else:
                    print(response.status_code)
                    print(response.reason)
            except Exception as e:
                print(e)
            sleep(5)
