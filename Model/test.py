import requests



response = requests.post("https://yo1gmy11ah.execute-api.ap-southeast-1.amazonaws.com/Prod/process",
                         headers={"x-api-key": "9f0043addf877477c0e2aed76284ba37d63e8658f551c2c7b2e2102d"})


files = {'file': ('D:\\Screenshot.png', open('D:\\20181005-084629.png', 'rb'), 'image/png', {'Expires': '0'})}
if response.ok:
        print(response.json())
        upload = response.json()

        r = requests.post(upload, files=files)
        print(r.text)

else:
        print(response.status_code)
        print(response.reason)
