import  requests
import boto3
import json
import os
running_process=[]
data = json.dumps(running_process).encode('utf8')


s3 = boto3.resource('s3')

response = requests.post("https://yo1gmy11ah.execute-api.ap-southeast-1.amazonaws.com/Prod/process", data=data,
                         headers={"x-api-key": "9f0043addf877477c0e2aed76284ba37d63e8658f551c2c7b2e2102d"})
with open('D:/Screenshot2.jpg', 'rb') as z:
  a= z.read()




if response.ok:
     print(response.json())
     upload=response.json()

     r=requests.post(upload, files=a)
     print(r.text)

else:
    print(response.status_code)
    print(response.reason)
